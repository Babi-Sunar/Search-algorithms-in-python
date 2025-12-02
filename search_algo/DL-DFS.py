#to represent tree in python -represent nodes as value and child keys in dictionary -child nodes are represented in lists


# tree = {
#     "value" : 5,
#     "child" : [{
#         "value" : 3,
#         "child" : [{"value" : 2,"child" : []},
#                 {"value" : 4, "child" : []}]
#     },{
#         "value" : 7,
#         "child" : [{
#             "value" : 8,
#             "child" : [{
#                 "value" : 4, "child" : []
#                 }]
#             }]
#     }]
# }

tree = {
    "A" : ["B","C"],
    "B": ["D","E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E":["I", "J"],
    "F" : ["K"],
    "G" : ["L", "M"],
    "H" : [],
    "I" : [],
    "J" : [],
    "K" : [],
    "L" : [],
    "M" : []
}

visited_node = []

def DL_BFS_search(visited_node, root_node, tree, limit):
    # extended_node stores (node, depth)
    visited_node.append(root_node)
    extended_node = [(root_node, 0)]

    while extended_node:
        pop_value, depth = extended_node.pop()
        print(pop_value, end=" --> ")

        # Stop expanding when depth limit is reached
        if depth == limit:
            continue
        
        for successor in reversed(tree[pop_value]):
            if successor not in visited_node:
                visited_node.append(successor)
                extended_node.append((successor, depth + 1))

print("The DL-DFS first search result is : ")
DL_BFS_search(visited_node, 'A', tree, 2)
print("end")
