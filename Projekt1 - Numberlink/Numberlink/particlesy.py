import numpy as np
from pyswarms.single.global_best import GlobalBestPSO

def numberlink_solver(board):
    # Define the objective function
    def objective_function(position):
        # Reshape the position array into a 2D array
        links = position.reshape((len(board), len(board[0]), 2))
        # Initialize the board with all zeros
        board_links = np.zeros((len(board), len(board[0]), 2))
        # Loop through each link and check if it is valid
        for i in range(len(links)):
            for j in range(len(links[0])):
                if links[i][j][0] == -1 or links[i][j][1] == -1:
                    continue
                if board_links[i][j][0] != 0 or board_links[i][j][1] != 0:
                    return np.inf
                if i > 0 and board_links[i-1][j][1] == links[i][j][0]:
                    return np.inf
                if i < len(links)-1 and board_links[i+1][j][0] == links[i][j][0]:
                    return np.inf
                if j > 0 and board_links[i][j-1][1] == links[i][j][1]:
                    return np.inf
                if j < len(links[0])-1 and board_links[i][j+1][1] == links[i][j][1]:
                    return np.inf
                board_links[i][j] = links[i][j]
        # Calculate the total length of all the links
        total_length = 0
        for i in range(len(links)):
            for j in range(len(links[0])):
                if links[i][j][0] != -1 and links[i][j][1] != -1:
                    total_length += abs(links[i][j][0]-links[i][j][1])
        return total_length

    # Define the bounds of the search space
    bounds = (np.zeros((len(board)*len(board[0])*2))-1, np.zeros((len(board)*len(board[0])*2))+len(board)*len(board[0]))

    # Create an instance of the optimizer
    optimizer = GlobalBestPSO(n_particles=100, dimensions=len(board)*len(board[0])*2, options={"c1": 0.5, "c2": 0.3, "w": 0.9}, bounds=bounds)

    # Optimize the objective function to find the best solution
    best_position, best_cost = optimizer.optimize(objective_function, iters=10000)

    # Reshape the best position array into a 2D array
    best_links = best_position.reshape((len(board), len(board[0]), 2))

    # Print the solution
    print("Solution:")
    for i in range(len(best_links)):
        row = ""
        for j in range(len(best_links[0])):
            if best_links[i][j][0] != -1:
                row += str(int(best_links[i][j][0])) + "-"
            else:
                row += "- "
            if best_links[i][j][1] != -1:
                row += str(int(best_links[i][j][1])) + " "
            else:
                row += "- "
        print(row)

# Test the solver with the given board
board = [
    ["-","-","-","-","-"],
    ["-","1","-","-","-"],
    ["-","-","2","-","-"],
    ["-","-","1","-","-"],
    ["0","2","0","-","-"],
]
numberlink_solver(board)