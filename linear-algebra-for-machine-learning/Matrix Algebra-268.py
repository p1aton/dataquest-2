## 2. Matrix Vector Multiplication ##

matrix_a = np.asarray([
    [0.7, 3, 9],
    [1.7, 2, 9],
    [0.7, 9, 2]
], dtype=np.float32)

vector_b = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

ab_product = np.dot(matrix_a, vector_b)
print(ab_product)



## 3. Matrix Multiplication ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
product_ba = np.dot(matrix_b, matrix_a)

print(product_ab)
print(product_ba)

## 4. Matrix Transpose ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a = np.transpose(matrix_a)
print(transpose_a)

print(np.transpose(transpose_a))

trans_ba = np.dot(np.transpose(matrix_b), np.transpose(matrix_a))
trans_ab = np.dot(np.transpose(matrix_a), np.transpose(matrix_b))

product_ab = np.dot(matrix_a, matrix_b)
print(np.transpose(product_ab))


## 5. Identity Matrix ##

i_2 = np.identity(2)
i_3 = np.identity(3)
matrix_33 = np.asarray([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
matrix_23 = np.asarray([
  [10, 11, 12],
  [13, 14, 15]
])
identity_33 = np.dot(i_3, matrix_33)
identity_23 = np.dot(i_2, matrix_23)


## 6. Matrix Inverse ##

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(mat):
    det = mat[0,0] * mat[1,1] - mat[0,1] * mat[1,0]
    if det == 0:
        raise ValueError("The matrix isn't invertible")
    else:
        return np.asarray([
            [mat[1,1], -mat[0,1]],
            [-mat[1,0], mat[0,0]]
        ]) / det
    
inverse_a = matrix_inverse_two(matrix_a)
i_2 = np.dot(inverse_a, matrix_a)
print(i_2)


## 7. Solving The Matrix Equation ##

mat = np.asarray([
    [30, -1],
    [50, -1]
])
b = np.asarray([
    [-1000],
    [-100]
])

solution_x = np.dot(np.linalg.inv(mat), b)
print(solution_x)



## 8. Determinant For Higher Dimensions ##

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])
det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)
