import agent
import util
import rgb
import sys


def main():
    inputs = sys.argv

    currAgent = agent.Agent()
    # input processing
    firstInput = inputs[1]
    if len(inputs) == 3:
        startingState = rgb.State(inputs[2])
    else:
        startingState = rgb.State('rgrb|grbr|b gr|gbbr')

    startingNode = agent.Node(startingState, None)
    # random walk command processing
    if firstInput == "random":
        finalNode = currAgent.random_walk(startingNode, 8)

    # bfs command processing
    if firstInput == "bfs":
        finalNode = currAgent.bfs(startingNode)

    # dfs command processing
    if firstInput == "dfs":
        finalNode = currAgent.dfs(startingNode)

    #a* command processing
    if firstInput == "a_star":
        finalNode = currAgent.a_star(startingNode, heuristicfunc)

def heuristicfunc(state):
    # heuristic is number of conflicts/3
    # b/c max number of conflicts resolved per move is 3
    col = state.size
    row = state.size
    numConflicts = 0
    for i in range(row):
        for j in range(col):
            if i == 0:
                if j ==0:
                    if state.board[i][j] == state.board[i + 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j+1]:
                        numConflicts += 1
                elif j == col-1:
                    if state.board[i][j] == state.board[i + 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j - 1]:
                        numConflicts += 1
                else:
                    if state.board[i][j] == state.board[i + 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j - 1]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j + 1]:
                        numConflicts += 1
            elif i == row-1:
                if j ==0:
                    if state.board[i][j] == state.board[i - 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j + 1]:
                        numConflicts += 1
                elif j == col-1:
                    if state.board[i][j] == state.board[i - 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j - 1]:
                        numConflicts += 1
                else:
                    if state.board[i][j] == state.board[i - 1][j]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j - 1]:
                        numConflicts += 1
                    if state.board[i][j] == state.board[i][j + 1]:
                        numConflicts += 1
            elif j == 0:
                if state.board[i][j] == state.board[i+1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i-1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i][j+1]:
                    numConflicts += 1
            elif j == col-1:
                if state.board[i][j] == state.board[i + 1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i - 1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i][j - 1]:
                    numConflicts += 1
            else:
                if state.board[i][j] == state.board[i-1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i+1][j]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i][j-1]:
                    numConflicts += 1
                if state.board[i][j] == state.board[i][j+1]:
                    numConflicts += 1
    # get rid of dupes
    numConflicts = numConflicts/2

    # make heuristic admissible
    numConflicts = numConflicts /3

    # print(state.board)
    # print(numConflicts)

    return numConflicts


if __name__ == "__main__":
    main()
