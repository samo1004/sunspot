import matplotlib.pyplot as plt
import numpy as np

rin = open('in.txt', 'r')
# print(rin.read())
# 將檔案美行前兩數字存在兩個陣列中
x = []
y = []
for line in rin:
    a = line.split()
    x.append(float(a[0]))  # 轉換成浮點數(小數)
    y.append(float(a[1]))
rin.close()

x = np.array(x)
y = np.array(y)

plt.plot(x, y)
plt.show()
