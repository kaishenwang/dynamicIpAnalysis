import sys
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    data = f.readlines()
data = [float(x.rstrip()) for x in data]

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(data, bins = 500, histtype='step',normed=1, cumulative=True, label='total change')
ax.grid(True)
ax.legend(loc='right')
ax.set_title('CDF')
ax.set_xlabel('average time to change ip')
ax.set_ylabel('')
plt.show()
