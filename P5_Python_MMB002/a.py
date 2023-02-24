# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# print ([mylist[i:i+4] for i in range(0, len(mylist), 4)])
# # Prints [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
# Matrice initiale 2D
matrix_2d = [[1, 2, 3, 4], 
             [5, 6, 7, 8], 
             [9, 10, 11, 12], 
             [13, 14, 15, 16], 
             [17, 18, 19, 20], 
             [21, 22, 23, 24]]

# Paginer la matrice 2D en une matrice 3D de pages de 5 lignes chacune
page_size = 5
num_rows, num_cols = len(matrix_2d), len(matrix_2d[0])
num_pages = (num_rows + page_size - 1) // page_size

matrix_3d = []
for page in range(num_pages):
    start_idx = page * page_size
    end_idx = min(start_idx + page_size, num_rows)
    matrix_3d.append(matrix_2d[start_idx:end_idx])

print(matrix_3d)
