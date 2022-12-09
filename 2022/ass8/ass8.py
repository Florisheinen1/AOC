# Tree: [height, visible]

# Returns similar list, but now with updated which one is visible
def update_visible(trees):
    # Left to right
    min_height = -1
    for i in range(len(trees)):
        tree = trees[i]
        if tree[0] > min_height:
            tree[1] = True
            min_height = tree[0]
    
    # Right to left
    min_height = -1
    for i in range(len(trees)-1, -1, -1):
        tree = trees[i]
        if tree[0] > min_height:
            tree[1] = True
            min_height = tree[0]

def get_tree_matrix():
    matrix = []
    with open("input.txt", 'r') as file:
        for row in file.readlines():
            matrow = []
            for c in row.rstrip():
                matrow.append([int(c), False])
            matrix.append(matrow)
    return matrix

a = [[1, False], [2, False], [1, False], [3, False], [1, False], [2, False], [2, False], [1, False]]

def print_visible(matrix):
    for row in matrix:
        line = ""
        for c in row:
            line = line + ("@" if c[1] else ".")
        print(line)

def update_row_visibility(matrix):
    for i in range(len(matrix)):
        current_row = matrix[i]
        update_visible(current_row)
    
def get_column(c, matrix):
    col = []
    for row in matrix:
        col.append(row[c])
    return col

def update_column_visibility(matrix):
    for i in range(len(matrix[0])):
        current_column = get_column(i, matrix)
        update_visible(current_column)

def update_matrix_visibility(matrix):
    update_row_visibility(matrix)
    update_column_visibility(matrix)

def count_visible_trees(matrix):
    update_matrix_visibility(matrix)

    COUNT = 0
    for row in matrix:
        for tree in row:
            if tree[1]:
                COUNT += 1
    return COUNT

mat = get_tree_matrix()
print(count_visible_trees(mat))


######################################

def get_view_distance(trees):
    height = trees[0][0]
    count = 0
    for tree in trees[1:]:
        count += 1
        if tree[0] >= height:
            break
    return count

def get_score_of_row(index, row):
    left = row[:index+1]
    left.reverse()
    right = row[index:]
    left_score = get_view_distance(left)
    right_score = get_view_distance(right)
    return left_score * right_score

def get_score(x, y, matrix):
    full_row = matrix[y]
    row_score = get_score_of_row(x, full_row)

    full_column = get_column(x, matrix)
    col_score = get_score_of_row(y, full_column)
    return row_score * col_score

def get_best_tree(matrix):
    max_score = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            score = get_score(x, y, matrix)
            if score > max_score:
                max_score = score
    return max_score

print(get_best_tree(mat))