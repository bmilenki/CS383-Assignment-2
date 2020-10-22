import random
import queue
import util


class Agent:
    def __init__(self):
        pass

    def random_walk(self, node, n):
        currNode = node
        for i in range(n-1):
            currState = currNode.getState()

            j = random.randrange(len(currState.actions()))
            newState = currState.clone()
            newState.execute(currState.actions()[j])

            newNode = Node(newState, currNode)
            currNode = newNode

        randomPath = self.generatePath(currNode)

        self.printPath(randomPath)

    def bfs(self, node):
        util.pprint(node.getState())
        self._search("bfs", node)

    def dfs(self, node):
        util.pprint(node.getState())
        self._search("dfs", node)

    def a_star(self, node, heuristic):
        util.pprint(node.getState())
        self._search("a*", node, heuristic)

    def _search(self, searchType, startingNode, heuristic=""):
        steps = 1
        if searchType == "bfs":
            openList = queue.Queue()
        elif searchType == "dfs":
            openList = queue.LifoQueue()
        elif searchType == "a*":
            openList = queue.PriorityQueue()

        closed = []

        # adds first node to open
        if heuristic == "":
            openList.put(startingNode)
        else:
            openList.put((0, startingNode))

        while True:
            if openList.empty():
                print("None")
                print(steps)
                return None

            if heuristic == "":
                currNode = openList.get()
            else:
                currNode = openList.get()[1]

            currState = currNode.getState()
            currActions = currState.actions()

            for i in range(len(currActions)):
                # print("*------------ Expansion: ", steps)
                # print("Length of Closed: ", len(closed))
                newState = currState.clone()
                newState.execute(currActions[i])

                newNode = Node(newState, currNode, currNode.getDistanceFromStart())
                newNode.addDistanceFromStart()

                if self.inClosed(newNode, closed):
                    # print("already in closed list")
                    continue

                if heuristic == "":
                    if self.inOpen(newNode, openList):
                        # print("already in closed list")
                        continue
                else:
                    if self.inOpen(newNode, openList,heuristic):
                        # print("already in open list")
                        continue

                if heuristic == "":
                    openList.put(newNode)
                else:
                    heurVal = heuristic(newState) + newNode.getDistanceFromStart()
                    # print("Heur: ", heuristic(newState))
                    # print("Distance: ", newNode.getDistanceFromStart())
                    openList.put((heurVal, newNode))

                steps += 1
                searchPath = self.generatePath(newNode)
                self.printPath(searchPath)

                # print("------------*")

                if newState.is_goal():
                    print(steps)
                    return newNode

            closed.append(currNode)

    def generatePath(self, finalNode):
        path = [finalNode]
        currNode = finalNode
        while currNode.getParent() is not None:
            path.insert(0, currNode.getParent())
            currNode = currNode.getParent()

        return path

    def printPath(self, path):
        statePath = []
        for i in range(len(path)):
            # print(path[i].getState().pprint_string())
            statePath.append(path[i].getState())

        util.pprint(statePath)

    def inClosed(self, node, closedList):
        for i in range(len(closedList)):
            if node.getState() == closedList[i].getState():
                return True
        return False

    def inOpen(self, node, openList, heuristic=""):
        if heuristic == "":
            if node in openList.queue:
                return True
            return False
        else:
            heurVal = heuristic(node.getState()) + node.getDistanceFromStart()
            if (heurVal, node) in openList.queue:
                return True
            return False

class Node:
    def __init__(self, state, parent, distanceFromStart=0):
        self.state = state
        self.parent = parent
        self.distancefromstart = distanceFromStart

    def __str__(self):
        return "State {}\nParent {}\nDistance {}".format(self.state, self.parent, self.distancefromstart)

    def __eq__(self, other):
        return self.state == other.state

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent

    def getDistanceFromStart(self):
        return self.distancefromstart

    def setState(self, newState):
        self.state = newState

    def setParent(self, newParent):
        self.parent = newParent

    def addDistanceFromStart(self):
        self.distancefromstart += 1

    def __lt__(self, other):
        # needed for priority queue to work properly, this ensure first in the queue gets expanded first
        return True
