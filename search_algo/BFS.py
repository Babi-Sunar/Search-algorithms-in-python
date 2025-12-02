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
    5 : [3,7],
    3: [2,4],
    7: [8],
    2 : [],
    4 :[8],
    8 : []
}
visited_node =[]
expanded_node = []

# function
def BFS_search(visited_node,root_node,tree):
    visited_node.append(root_node)
    expanded_node.append(root_node)

    while(expanded_node):
        pop_value = expanded_node.pop(0)
        print(pop_value, end= " --> ")
        for successor in tree[pop_value]:
            if(successor not in visited_node): #not in
                visited_node.append(successor) 
                expanded_node.append(successor)

print("The breadth first search result is : ")
BFS_search(visited_node, 5, tree)