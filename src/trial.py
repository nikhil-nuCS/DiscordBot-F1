import ergast_py
import matplotlib.pyplot as plt
import seaborn
e = ergast_py.Ergast()
ans = e.circuit("imola").get_circuit()
print(ans)