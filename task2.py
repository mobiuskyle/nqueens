import random
def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]
def conflicts(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                count += 1
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count
def best_neighbor(board):
    n = len(board)
    current_conflicts = conflicts(board)
    best_board = board[:]
    best_score = current_conflicts

    for col in range(n):
        for row in range(n):
            if row == board[col]:
                continue
            neighbor = board[:]
            neighbor[col] = row
            score = conflicts(neighbor)
            if score < best_score:
                best_score = score
                best_board = neighbor[:]

    return best_board, best_score

def hill_climbing(n):
    board = random_board(n)

    while True:
        current_score = conflicts(board)
        if current_score == 0:
            return board, True

        neighbor, neighbor_score = best_neighbor(board)

        if neighbor_score >= current_score:
            return board, False

        board = neighbor
def print_board(board):
    n = len(board)
    print("\nChessboard:")
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[col] == row else ". "
        print(line)
def hill_climbing_random_restart(n, max_restarts=1000):
    for attempt in range(1, max_restarts + 1):
        board, success = hill_climbing(n)

        if success:
            print(f"Solution found after {attempt} attempt(s)!")
            return board

        else:
            print(f"Attempt {attempt}: Stuck at local minimum. Restarting...")

    print("Could not find a solution within the restart limit.")
    return None     
n = 8
print(f"Solving {n}-Queens with Random Restart Hill Climbing...\n")

solution = hill_climbing_random_restart(n)

if solution:
    print_board(solution)
    print("\nNumber of conflicts:", conflicts(solution))
