import numpy as np

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
