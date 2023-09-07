# class BellmanFord{
#     function BellmanFord(list nodes, list edges, node source)
#     distance := list
#     predecessor := list
#     // Step 1: initialize
#     for each node n in nodes do
#         distance[n] := inf // Initialize the distance to all nodes to infinity
#         predecessor[n] := null // And having a null predecessor
#     distance[source] := 0 // The distance from the source to itself is zero
#     // Step 2: relax edges repeatedly
#     repeat |nodes|-1 times:
#         for each edge (u, v) with weight w in edges do
#             if distance[u] + w < distance[v] then
#                 distance[v] := distance[u] + w
#                 predecessor[v] := u
#     // Step 3: check for negative-weight cycles
#     for each edge (u, v) with weight w in edges do
#         if distance[u] + w < distance[v] then
#             error "Graph contains a negative-weight cycle"
#     return distance, predecessor

# }

