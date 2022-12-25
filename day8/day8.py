import copy

def read_input():
    lines = []
    with open('day8.txt', "r") as f:
        for line in f:
            row = list(line.strip())
            int_row = map(lambda x: int(x), row)
            lines.append(list(int_row))
    return lines

def solve_tl(grid):
    bool_grid = copy.deepcopy(grid)
    tallest_in_col = [-1] * len(grid[0])

    for i in range(len(grid)):
        tallest_in_row = -1
        for j in range(len(grid[0])):
            this_val = grid[i][j]
            if (this_val > tallest_in_col[j]) or (this_val > tallest_in_row):
                bool_grid[i][j] = True
            else:
                bool_grid[i][j] = False
            tallest_in_col[j] = max(tallest_in_col[j], this_val)
            tallest_in_row = max(tallest_in_row, this_val)
    return bool_grid

def solve_br(grid):
    bool_grid = copy.deepcopy(grid)
    tallest_in_col = [-1] * len(grid[0])

    for i in range(len(grid)-1, -1, -1):
        tallest_in_row = -1
        for j in range(len(grid[0])-1, -1, -1):
            this_val = grid[i][j]
            if (this_val > tallest_in_col[j]) or (this_val) > tallest_in_row:
                bool_grid[i][j] = True
            else:
                bool_grid[i][j] = False
            tallest_in_col[j] = max(tallest_in_col[j], this_val)
            tallest_in_row = max(tallest_in_row, this_val)
    return bool_grid

def sum_visible_trees(grid1, grid2):
    sum_vis = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] or grid2[i][j]:
                sum_vis +=1
    return sum_vis

def solvea(grid):
    first_pass = solve_tl(grid)
    second_pass = solve_br(grid)
    sum_vis = sum_visible_trees(first_pass, second_pass)
    return sum_vis

def score_t(grid, i, j, val):
    if (i < 0):
        return 0
    elif grid[i][j] >= val:
        return 1
    return 1 + score_t(grid, i-1, j, val)

def score_l(grid, i, j, val):
    if (j < 0):
        return 0
    elif grid[i][j] >= val:
        return 1
    return 1 + score_l(grid, i, j-1, val)

def score_b(grid, i, j, val):
    if (i > len(grid[0]) - 1):
        return 0
    elif grid[i][j] >= val:
        return 1
    return 1 + score_b(grid, i+1, j, val)

def score_r(grid, i, j, val):
    if (j > len(grid) - 1):
        return 0
    elif grid[i][j] >= val:
        return 1
    return 1 + score_r(grid, i, j+1, val)

def score(grid, i, j):
    val = grid[i][j]
    return score_t(grid,i-1,j, val) * score_l(grid,i,j-1, val) * score_b(grid,i+1,j, val) * score_r(grid,i,j+1, val)

def solveb(grid):
    highest_score = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scenic_score = score(grid, i, j)
            highest_score = max(highest_score, scenic_score)
    return highest_score

def main():
    # small_example = [[3,0,3,7,3],
    # [2,5,5,1,2],
    # [6,5,3,3,2],
    # [3,3,5,4,9],
    # [3,5,3,9,0]]
    grid = read_input()
    visible = solvea(grid)
    print(visible)
    highest_scenic_score = solveb(grid)
    print(highest_scenic_score)


if __name__ == "__main__":
    main()
