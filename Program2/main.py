class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):  # Defining Graph Object
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}

    def applyAOStar(self):  # Starts A Recursive AO* Algorithm
        self.aoStar(self.start, False)

    def getNeighbors(self, v):  # Gets The Neighbors Of A Given Node
        return self.graph.get(v, '')

    def getStatus(self, v):  # Returns The Status Of A Given Node
        return self.status.get(v, 0)

    def setStatus(self, v, val):  # Set The Status Of A Given Node
        self.status[v] = val

    def getHeuristicNodeValue(self, n):  # Always Returns The Heuristic Value Of A Given Node
        return self.H.get(n, 0)

    def setHeuristicNodeValue(self, n, value):  # Set The Revised Heuristic Value Of A Given Node
        self.H[n] = value

    def printSolution(self):  # Printing Solution
        print("For A Graphical Solution, Traverse The Graph From The Start Node:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinimumCostChildNodes(self, v):  # Computes The Minimum Cost Of Child Nodes Of A Given Node 'v'
        minimumCost = 0
        costToChildNodeListDict = {minimumCost: []}
        flag = True
        for nodeInfoTupleList in self.getNeighbors(v):  # Iterating Over All The Set Of Child Node(s)
            cost = 0
            nodeList = []
            for c, weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)
            if flag == True:  # Initialize Minimum Cost With The Cost Of First Set Of Child Node(s)
                minimumCost = cost
                costToChildNodeListDict[minimumCost] = nodeList  # Get The Minimum Cost Child Node(s)
                flag = False
            else:  # Checking The Minimum Cost Nodes With The Current Minimum Cost
                if minimumCost > cost:
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList  # Set The Minimum Cost Child Node(s)

        return minimumCost, costToChildNodeListDict[minimumCost]  # Return Minimum Cost And Minimum Cost Child Node(s)

    def aoStar(self, v, backTracking):  # AO* Algorithm For A Start Node And Enabling BackTracking status flag
        print("HEURISTIC VALUES  :", self.H)
        print("SOLUTION GRAPH    :", self.solutionGraph)
        print("PROCESSING NODE   :", v)
        print("-----------------------------------------------------------------------------------------")

        if self.getStatus(v) >= 0:  # If Status Node 'v' >= 0, Compute Minimum Cost Nodes Of 'v'
            minimumCost, childNodeList = self.computeMinimumCostChildNodes(v)
            self.setHeuristicNodeValue(v, minimumCost)
            self.setStatus(v, len(childNodeList))

            solved = True  # Check If The Minimum Cost Nodes Of 'v' Are Solved
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved & False

            if solved == True:  # If The Minimum Cost Nodes Of 'v' Are Solved, Set The Current Node Status As Solved(-1)
                self.setStatus(v, -1)
                self.solutionGraph[v] = childNodeList  # Update The Solution Graph With The Solved Nodes Which May Be A Part Of Solution

            if v != self.start:  # Check If The Current Node Is The Start Node For Backtracking The Current Node Value
                self.aoStar(self.parent[v], True)  # Backtracking The Current Node Value With Backtracking Status Set To True

            if not backTracking:  # Check Whether The Current Call Is Not For Backtracking
                for childNode in childNodeList:  # For Each Minimum Cost Child Node
                    self.setStatus(childNode, 0)  # Set The Status Of Child Node To 0(Needs Exploration)
                    self.aoStar(childNode, False)  # Minimum Cost Child Node Is Further Explored With Backtracking Status As False


heuristic = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
tree = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
    }

G = Graph(tree, heuristic, 'A')
G.applyAOStar()
G.printSolution()