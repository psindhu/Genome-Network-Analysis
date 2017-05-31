import snap
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn import decomposition

graph_dict = dict()
graph_nodes = []
graphs = dict()

#Network 1 Graph	
G1 = snap.PNGraph.New()
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)
G1.AddNode(4)
G1.AddEdge(1,2)
G1.AddEdge(1,3)
G1.AddEdge(2,4)
G1.AddEdge(3,4)
for EI in G1.Edges():
	print "N#1 edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
graphs[1] = [G1]
graph_nodes.append(sum(1 for _ in G1.Nodes()))

#Network 2 Graph	
G2 = snap.PNGraph.New()
G2.AddNode(1)
G2.AddNode(2)
G2.AddNode(3)
G2.AddNode(4)
G2.AddEdge(1,2)
G2.AddEdge(1,3)
G2.AddEdge(2,4)
for E2 in G2.Edges():
	print "N#2 edge (%d, %d)" % (E2.GetSrcNId(), E2.GetDstNId())
graphs[2] = [G2]
graph_nodes.append(sum(1 for _ in G2.Nodes()))


#Network 3 Graph		
G3 = snap.PNGraph.New()
G3.AddNode(1)
G3.AddNode(2)
G3.AddNode(3)
G3.AddNode(4)
G3.AddEdge(1,3)
G3.AddEdge(3,4)
for E3 in G3.Edges():
	print "N#3 edge (%d, %d)" % (E3.GetSrcNId(), E3.GetDstNId())
graphs[3] = [G3]
graph_nodes.append(sum(1 for _ in G3.Nodes()))

	
#Network 4 Graph			
G4 = snap.PNGraph.New()
G4.AddNode(1)
G4.AddNode(2)
G4.AddNode(3)
G4.AddNode(4)
G4.AddEdge(1,4)
G4.AddEdge(2,3)
for E4 in G4.Edges():
	print "N#4 edge (%d, %d)" % (E4.GetSrcNId(), E4.GetDstNId())
graphs[4] = [G4]
graph_nodes.append(sum(1 for _ in G4.Nodes()))

	
#Network 5 Graph				
G5 = snap.PNGraph.New()
G5.AddNode(1)
G5.AddNode(2)
G5.AddNode(3)
G5.AddNode(4)
G5.AddEdge(1,2)
G5.AddEdge(1,4)
G5.AddEdge(2,3)
for E5 in G5.Edges():
	print "N#5 edge (%d, %d)" % (E5.GetSrcNId(), E5.GetDstNId())
graphs[5] = [G5]
graph_nodes.append(sum(1 for _ in G5.Nodes()))
					
#Network 6 Graph
G6 = snap.PNGraph.New()
G6.AddNode(1)
G6.AddNode(2)
G6.AddNode(3)
G6.AddNode(4)
G6.AddEdge(1,4)
G6.AddEdge(2,4)
G6.AddEdge(3,4)
G6.AddEdge(2,3)
for E6 in G6.Edges():
	print "N#6 edge (%d, %d)" % (E6.GetSrcNId(), E6.GetDstNId())
graphs[6] = [G6]
graph_nodes.append(sum(1 for _ in G6.Nodes()))

#find the maximum number of nodes
val =  max(graph_nodes)
pairs = (val * (val-1))/2

#find only the unique pair of edges possible
D = snap.PNGraph.New()
for i in range (val):
	D.AddNode(i + 1)
	
for i in range (val):
	for j in range (val):
		if((i+1 <= val) and (i+1 != j+1) and (i+1 < j+1)):
			D.AddEdge(i+1,j+1)
		
#print all dummy edges
for Dummy in D.Edges():
	print "Dummy edge (%d, %d)" % (Dummy.GetSrcNId(), Dummy.GetDstNId())

#Network Comparison
for i in range(len(graphs)):
	graph_dict[i+1] = []
	x1 = 0
	for Dummy in D.Edges():
		graph = graphs[i+1][0]
		for EC1 in graph.Edges():
			if (EC1.GetSrcNId() is Dummy.GetSrcNId()) and (EC1.GetDstNId() is Dummy.GetDstNId()):
				graph_dict[i+1].append(x1)
				print "edges which are common with N#"+str(i+1)+" and Dummy# are (%d, %d)" % (EC1.GetSrcNId(), EC1.GetDstNId())
		x1 = x1 + 1
		graph_dict["N"+str(i+1)] = []

#creating dictionary showing matrix of edges in 0s and 1s	
for j in  range(len(graphs)):
	for i in range(pairs):
		y = 0
		for val in graph_dict[i+1]:
			print val
			if i == val:
				y = 1
				graph_dict["N"+str(j+1)].append(1)
				break
		if y != 1:
			graph_dict["N"+str(j+1)].append(0)
		print graph_dict["N"+str(j+1)]
		

labels = ['N1','N2','N3','N4','N5','N6']
# samples x features matrix - features are AB, AC, AD, BC, BD, CD links
X_original = np.array(graph_dict)
print X_original
pca = decomposition.PCA(n_components=2)
pca.fit(X_original)

X = pca.transform(X_original)


np.set_printoptions(suppress=True)

print('variance explained by these components:',pca.explained_variance_ratio_)

# what are the axes? what do they represent?
#looking at the first component
# note extremes represent what increases/decreases as we move along that axis

print(pca.components_[0])

print(pca.components_[1])

# a plot without labels
pl.ion()

pl.scatter(X[:, 0], X[:, 1], s=50)

for label, x, y in zip(labels, X[:, 0], X[:, 1]):
    pl.annotate(
        label, 
        xy = (x, y), xytext = (30*x,30*y),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

# a plot with labels
pl.savefig('pca_plot.png')

pl.ion()