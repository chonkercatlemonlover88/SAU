import numpy as np
from scipy.linalg import block_diag

# Определение матриц
A = np.array([[1, 3, 6], [2, 4, 5], [5, 4, 3]])
B = np.array([[1, 2, 3], [0, 6, 4], [9, 8, 1]])
C = np.array([[1, 1, 0]])

# Вычисление матрицы управляемости
W = np.hstack((B, np.dot(A, B), np.dot(np.dot(A, A), B)))
print(f"Матрица управляемости W:\n{W}")

# Вычисление ранга матрицы управляемости
rank_W = np.linalg.matrix_rank(W)
print(f"Ранг матрицы управляемости: {rank_W}")

# Вычисление матрицы наблюдаемости
V = np.vstack((C, np.dot(C, A), np.dot(C, np.dot(A, A))))
print(f"Матрица наблюдаемости V:\n{V}")

# Вычисление ранга матрицы наблюдаемости
rank_V = np.linalg.matrix_rank(V)
print(f"Ранг матрицы наблюдаемости: {rank_V}")

# Вычисление собственных значений матрицы A
eigvals = np.linalg.eigvals(A)
print(f"Собственные значения матрицы A: {eigvals}")

# Проверка устойчивости системы
is_stable = all(np.real(eigval) < 0 for eigval in eigvals)
print(f"Система устойчива: {is_stable}")
