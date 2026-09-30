def solve_n_queens(n):
    cols = set()
    pos_diag = set()
    neg_diag = set()
    
    solutions = []
    board = [["."] * n for _ in range(n)]
    
    def dfs(row):
        if row == n:
            copy = ["".join(r) for r in board]
            solutions.append(copy)
            return
        
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
            
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            
            dfs(row + 1)
            
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    dfs(0)
    return solutions

N = 4
all_solutions = solve_n_queens(N)

print(f"Found {len(all_solutions)} solutions for N = {N}:\n")
for idx, sol in enumerate(all_solutions, 1):
    print(f"Solution #{idx}:")
    for row in sol:
        print(" ".join(row))
    print()