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
visited_node =[]
expanded_node = []

# function
def BFS_search(visited_node,root_node,tree):
    visited_node.append(root_node)
    expanded_node.append(root_node)
    while(expanded_node):
        pop_value = expanded_node.pop()
        print(pop_value, end= " --> ")
        for successor in reversed(tree[pop_value]):
            if(successor not in visited_node): #not in
                visited_node.append(successor )
                expanded_node.append(successor)
print("The breadth first search result is : ")
BFS_search(visited_node,'A', tree)
print("end")