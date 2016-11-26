import networkx as nx
G = nx.DiGraph()
pathFile = open('D:\\1path.txt','r')
for line in pathFile:
    lineElements = line.split()
    if len(lineElements) == 3:
    	G.add_edge(lineElements[0], lineElements[2])
pathFile.close()
pageRankResultFile = open('E:\\KU\Year4\\IR\\HwWs3-PageRank\\pageRankResult.txt','w')
pr = nx.pagerank(G, alpha = 0.85)
for key, val in pr.iteritems():
	pageRankResultFile.write("%s:pr:%f\n" % (key,val))
pageRankResultFile.close()
