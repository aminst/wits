import sys
import numpy as np
import pandas as pd
import networkx as nx
import collections
import matplotlib.pyplot as plt
from backbone import *

def save_degree_hist(G, is_cut, reports_path):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degree_count = collections.Counter(degree_sequence)
    deg, cnt = zip(*degree_count.items())
    plt.figure(figsize=(20, 10))
    ax = plt.gca()
    plt.bar(deg, cnt, width=0.80, color="b")
    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.axes([0.4, 0.4, 0.5, 0.5])
    plt.axis("off")
    if is_cut:
        plt.savefig(reports_path + "/cut_degree_seq.png")
    else:
        plt.savefig(reports_path + "/initial_degree_seq.png")

def save_graph(G, is_cut, reports_path):
    plt.figure(figsize=(20, 20))
    nx.draw_networkx(G, pos=nx.layout.spring_layout(G), width=0.2)
    if is_cut:
        plt.savefig(reports_path + "/cut_graph.png")
    else:
        plt.savefig(reports_path + "/initial_graph.png")

def create_directed_graph(edgelist: pd.DataFrame, nodelist: pd.DataFrame):
    net = nx.DiGraph()
    nodes = []
    for i, row in nodelist.iterrows():
        attr_dict = {"label": row["country_iso3"]}
        for column in set(nodelist.columns) - {"country_iso3"}:
            attr_dict[column] = row[column]
        nodes.append((row["country_iso3"], attr_dict))
    net.add_nodes_from(nodes)
    
    for i, row in edgelist.iterrows():
        net.add_edge(row["source"], row["target"], weight = row["weight"])
    return net

def create_backbone_graph(net: nx.DiGraph, min_alpha_ptile = 0.5, min_degree = 1):
    graph = net.copy()
    alpha_measures = disparity_filter(graph)
    quantiles, num_quant = calc_alpha_ptile(alpha_measures)
    alpha_cutoff = quantiles[round(num_quant * min_alpha_ptile)]
    cut_graph(graph, min_alpha_ptile, min_degree)
    return graph

def get_nodes_list(G: nx.DiGraph, columns):
    data={}
    data["country_iso3"]=[x for x in G]
    for column in columns:
        data[column] = [G.nodes[x][column] for x in G.nodes()]
    return pd.DataFrame(data)

def main():
    """
    sample usage: python backbone_runner.py <nodelist_path> <edgelist_path> <min_alpha_ptile> <min_degree> <out_nodelist_path> <out_edgelist_path> <reports_path>
    """
    nodelist_path = sys.argv[1]
    edgelist_path = sys.argv[2]
    min_alpha_ptile = sys.argv[3]
    min_degree = sys.argv[4]
    out_nodelist_path = sys.argv[5]
    out_edgelist_path = sys.argv[6]
    reports_path = sys.argv[7]

    nodelist_df = pd.read_csv(nodelist_path)
    edgelist_df = pd.read_csv(edgelist_path)
    net = create_directed_graph(edgelist_df, nodelist_df)
    print("Initial graph edge count: {}".format(net.size()))
    print("Initial graph density: {}".format(nx.density(net)))

    cut_net = create_backbone_graph(net, min_alpha_ptile=float(min_alpha_ptile), min_degree=int(min_degree))
    print("Cut graph edge count: {}".format(cut_net.size()))
    print("Cut graph density: {}".format(nx.density(cut_net)))

    save_degree_hist(cut_net, True, reports_path)
    save_degree_hist(net, False, reports_path)
    save_graph(cut_net, True, reports_path)
    save_graph(net, False, reports_path)

    cut_edge_list = nx.convert_matrix.to_pandas_edgelist(cut_net).drop(columns = ["alpha_ptile", "alpha", "norm_weight"])
    cut_node_list = get_nodes_list(cut_net, set(nodelist_df.columns) - {"country_iso3"})
    cut_edge_list.to_csv(out_edgelist_path, index = False)
    cut_node_list.to_csv(out_nodelist_path, index = False)

if __name__ == '__main__':
    main()
