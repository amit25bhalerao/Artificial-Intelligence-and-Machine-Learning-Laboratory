# Dictionary To Define Graph
tree = {'S': [['B', 4], ['C', 3]],                  # Start Node
        'B': [['F', 5]],                            # Intermediate Node
        'C': [['D', 7], ['E', 10]],                 # Intermediate Node
        'D': [['E', 2]],                            # Intermediate Node
        'E': [['G', 5]],                            # Intermediate Node
        'F': [['G', 16]]}                           # Goal Node

# Dictionary To Store Heuristic Values
heuristic = {'S': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

# Dictionary To Calculate And Restore Cost For Different Nodes While Traversing Optimal Path
# Initial Cost Set To Zero
cost = {'S': 0}


# Defining Function For AStarSearch Algorithm
def AStarSearch():

    # global Keyword Allows You To Modify The Variable Outside Of The Current Scope
    global tree, heuristic
    closed = []                         # Closed Nodes
    opened = [['S', 14]]                # Open Nodes

    # Finding The Visited Nodes
    # Looping Until We Find The Goal Node
    while True:

        # f(n) = g(n) + h(n)
        # Selecting The Numerical Parameter Of 'opened'
        fn = [i[1] for i in opened]

        # Selecting The Index Of The Minimum Value In 'fn'
        chosen_index = fn.index(min(fn))

        # Selecting The Character Associated With The Index Of The Minimum Value In 'fn'
        node = opened[chosen_index][0]

        # Adding The Node Present In 'opened' To 'closed
        closed.append(opened[chosen_index])

        # Deleting The Node Having Minimum Value In 'fn' From 'opened'
        del opened[chosen_index]

        # Break The Loop If The Goal Node Is Found
        # -1 Indicates The End Of Array
        if closed[-1][0] == 'G':
            break

        # Looping Through The Graph For Current Node
        for item in tree[node]:
            # Checking If The Current Node Is Present As A Visited Node. If So, Then We Skip The Same During Iteration
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            # We Update The Cost Dictionary By Appending The Unvisited Node To It
            cost.update({item[0]: cost[node] + item[1]})
            # Calculating f(n) Value For The Current Node
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            # Creating 'temp' To Store f(n) Of Current Node
            temp = [item[0], fn_node]
            # Store f(n) Of Current Node In 'opened'
            opened.append(temp)

    # Find Optimal Sequence
    # Correct Optimal Tracing Node, Initializing As Node G
    trace_node = 'G'

    # Initial Optimal Node Sequence
    optimal_sequence = ['G']

    # Tracing From Goal Node To Start Node
    for i in range(len(closed) - 2, -1, -1):
        # Check Current Node
        check_node = closed[i][0]
        # Check If The 'trace_node' Is The Child Of Our Testing 'check _node' Or Not
        if trace_node in [children[0] for children in tree[check_node]]:
            # Storing Cost Associated With Node
            children_costs = [temp[1] for temp in tree[check_node]]
            # Storing Character Associated With Node
            children_nodes = [temp[0] for temp in tree[check_node]]
            # Check Whether f(n) = g(n) + h(n) If So, Append Current Node To Optimal Sequence And Change The Correct
            # Optimal Tracing Node To Current Node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node

    # Reverse The Optimal Sequence
    optimal_sequence.reverse()

    # Return 'closed' And 'optimal_sequence'
    return closed, optimal_sequence


if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('Visited Nodes: ' + str(visited_nodes))
    print('Optimal Nodes Sequence: ' + str(optimal_nodes))