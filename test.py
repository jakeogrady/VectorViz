from matplotlib import pyplot as plt
plt.style.use('fast')
x = [10, 3, 8, 12]
y = [12,32,4,6]
z = [0, 5, 2, 12]
w = [13,1,4,6]
x.sort()
y.sort()
w.sort()
z.sort()

plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.set_xlim(-4.5,4.5)
ax.set_ylim(-4.5,4.5)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')


plt.show()
