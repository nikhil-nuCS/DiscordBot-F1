import ergast_py
import matplotlib.pyplot as plt
import seaborn
e = ergast_py.Ergast()
ans = e.circuit("monaco").get_circuit()
print(ans)

