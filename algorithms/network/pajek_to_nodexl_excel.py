# -*- coding:utf-8 -*-

# 将pajek文件转存为csv文件

import networkx as nx
import os

def read_pajek(path, encoding='utf-8-sig'):
  """Read in a pajek format graph and 
  turn it into networkx object.
  """
  return nx.readwrite.pajek.read_pajek(path, encoding=encoding)

def pajek_to_csv(G, output_path):
  edges = list(G.edges)
  with open(output_path, 'w') as f:
    for e in edges:
      f.write("%s,%s,%d\n" % (e[0], e[1], e[2]))


def work(net_path):
  # name, extname = os.path.splitext(net_path)
  output_path = net_path + '.csv'
  G = read_pajek(net_path)
  pajek_to_csv(G, output_path)


if __name__ == '__main__':
  path_zh = '/Users/junr/Documents/git/lingua/data/20191206-pdf/chinese.net'
  work(path_zh)

  path_en = '/Users/junr/Documents/git/lingua/data/20191206-pdf/english.net'
  work(path_en)

