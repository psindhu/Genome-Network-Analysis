import snap

edgefilename = "edges1.txt"  # A file containing the graph, where each row contains an edge
                                     # and each edge is represented with the source and dest node ids,
                                     # and the edge attributes, separated by a tab.

nodefilename = "nodes1.txt"  # A file containing the nodes of a graph. Each row contains a node id,
                                     # and (optionally) node attributes.


context = snap.TTableContext()  # When loading strings from different files, it is important to use the same context
                                # so that SNAP knows that the same string has been seen before in another table.

edgeschema = snap.Schema()
edgeschema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))

nodeschema = snap.Schema()
nodeschema.Add(snap.TStrTAttrPr("nodeID", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("nodeattr1", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("nodeattr2", snap.atStr))

edge_table = snap.TTable.LoadSS(edgeschema, edgefilename, context, "\t", snap.TBool(False))
node_table = snap.TTable.LoadSS(nodeschema, nodefilename, context, "\t", snap.TBool(False))

# In this example, we add both edge attributes to the network, but only one node attribute.
edgeattrv = snap.TStrV()
edgeattrv.Add("edgeattr1")
edgeattrv.Add("edgeattr2")

nodeattrv = snap.TStrV()
nodeattrv.Add("nodeattr1")

# net will be an object of type snap.PNEANet
net1 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", edgeattrv, node_table, "nodeID", nodeattrv, snap.aaFirst)
for NI in net1.Nodes():
	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
for EI in net1.Edges():
	print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
	
	
	

edgefilename = "edges2.txt"  # A file containing the graph, where each row contains an edge
                                     # and each edge is represented with the source and dest node ids,
                                     # and the edge attributes, separated by a tab.

nodefilename = "nodes2.txt"  # A file containing the nodes of a graph. Each row contains a node id,
                                     # and (optionally) node attributes.


context = snap.TTableContext()  # When loading strings from different files, it is important to use the same context
                                # so that SNAP knows that the same string has been seen before in another table.

edgeschema = snap.Schema()
edgeschema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))

nodeschema = snap.Schema()
nodeschema.Add(snap.TStrTAttrPr("nodeID", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("nodeattr1", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("nodeattr2", snap.atStr))

edge_table = snap.TTable.LoadSS(edgeschema, edgefilename, context, "\t", snap.TBool(False))
node_table = snap.TTable.LoadSS(nodeschema, nodefilename, context, "\t", snap.TBool(False))

# In this example, we add both edge attributes to the network, but only one node attribute.
edgeattrv = snap.TStrV()
edgeattrv.Add("edgeattr1")
edgeattrv.Add("edgeattr2")

nodeattrv = snap.TStrV()
nodeattrv.Add("nodeattr1")

# net will be an object of type snap.PNEANet
net2 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", edgeattrv, node_table, "nodeID", nodeattrv, snap.aaFirst)
for N2 in net2.Nodes():
	print "node: %d, out-degree %d, in-degree %d" % ( N2.GetId(), N2.GetOutDeg(), N2.GetInDeg())
for E2 in net2.Edges():
	print "edge (%d, %d)" % (E2.GetSrcNId(), E2.GetDstNId())




