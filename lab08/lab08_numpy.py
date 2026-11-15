import numpy as np

# 1
hours = np.arange(0, 22, 3)          
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)       
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours =", hours)
print("hours.shape =", hours.shape)
print("hours.ndim  =", hours.ndim)
print("hours.size  =", hours.size)
print("hours.dtype =", hours.dtype)

print("line          =", line)
print("zeros         =", zeros)
print("unknown_table =\n", unknown_table)
print("identity      =\n", identity)

# 2

print("третий элемент             :", hours[2])
print("последний элемент          :", hours[-1])
print("элементы с индексами 2–5   :", hours[2:6])
print("каждый второй элемент      :", hours[::2])
print("массив в обратном порядке  :", hours[::-1])

# 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("форма                 :", temperatures.shape)
print("число измерений       :", temperatures.ndim)
print("число элементов       :", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка         :", temperatures[0])
print("последний столбец     :", temperatures[:, -1])
print("первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("центральный фрагмент 2×2:\n", temperatures[0:2, 1:3])
print("форма центрального фрагмента:", temperatures[0:2, 1:3].shape)

# 4

matrix = np.arange(1, 26).reshape(5, 5)

first_three_rows = matrix[:3]
print("первые три строки:\n", first_three_rows, "\nshape =", first_three_rows.shape)

last_two_rows = matrix[-2:]
print("последние две строки:\n", last_two_rows, "\nshape =", last_two_rows.shape)

first_two_cols = matrix[:, :2]
print("первые два столбца:\n", first_two_cols, "\nshape =", first_two_cols.shape)

middle = matrix[1:4, 2:5]
print("строки 1–3, столбцы 2–4:\n", middle, "\nshape =", middle.shape)

corner = matrix[-2:, -2:]
print("угловой блок 2×2 справа снизу:\n", corner, "\nshape =", corner.shape)

# 5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после замены 1:4 на 0:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)

