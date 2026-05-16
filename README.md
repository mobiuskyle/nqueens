#  N-Queens Problem — Hill Climbing Algorithm

**CCS 2226 – Foundation of Artificial Intelligence**  
**Author:** mobiuskyle  

---

##  Overview

This project solves the classic **N-Queens Problem** using two approaches:

- **Task 1:** Hill Climbing
- **Task 2:** Hill Climbing with Random Restart

The goal is to place **N queens** on an **N×N chessboard** such that no two queens threaten each other — meaning no two queens share the same row, column, or diagonal.

---

##  What is Hill Climbing?

Hill Climbing is a **local search algorithm** used in Artificial Intelligence. It works by:

1. Starting with a random solution (random board)
2. Evaluating how good the solution is using a **heuristic** (number of attacking queen pairs)
3. Moving to a **better neighboring state** (moving one queen to reduce conflicts)
4. Repeating until no better move is found

The algorithm aims to reach a state with **zero conflicts** — that is the solution.

### Limitation
Hill Climbing can get **stuck at a local minimum** — a state where no single move improves the board, but it is not yet a solution. This is solved in Task 2.

---

##  What is Random Restart?

Random Restart extends Hill Climbing by:

- Detecting when the algorithm is stuck
- **Throwing away the stuck board** and starting fresh with a new random board
- Repeating until a solution is found

This dramatically increases the chances of finding a solution.

---

##  Project Structure

```
nqueens/
│
├── task1.py      # Hill Climbing solution
├── task2.py      # Hill Climbing with Random Restart
└── README.md     # This file
```

---

##  Requirements

- Python 3.x

No external libraries are needed. The code uses only Python's built-in `random` module.

---

##  How to Run

### Task 1 — Hill Climbing
```bash
python task1.py
```

### Task 2 — Hill Climbing with Random Restart
```bash
python task2.py
```

---

## Example Output

### Task 1
```
Chessboard:
. . . Q . . . .
. . . . . . Q .
. . Q . . . . .
Q . . . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . . Q
. . . . Q . . .

Number of conflicts: 0
 Solution found!
```

### Task 2
```
Solving 8-Queens with Random Restart Hill Climbing...

 Attempt 1: Stuck at local minimum. Restarting...
 Attempt 2: Stuck at local minimum. Restarting...
 Solution found after 3 attempt(s)!

Chessboard:
. . . Q . . . .
. . . . . . Q .
. . Q . . . . .
Q . . . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . . Q
. . . . Q . . .

Number of conflicts: 0
```

---

## How the Heuristic Works

The heuristic counts the number of **attacking pairs** of queens:

- Two queens on the **same row** → conflict
- Two queens on the **same diagonal** → conflict
- (Each queen is already in a unique column by design)

The algorithm tries to **minimize this number to 0**.

---

## References

- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. — Chapter 4: Search in Complex Environments
- [Hill Climbing — Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
- [N-Queens Problem — Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- CCS 2226 – Foundation of Artificial Intelligence, Practical Session Materials

---

## 📄 License

This project was created for educational purposes as part of a university practical assignment.
