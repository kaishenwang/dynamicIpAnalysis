import sys
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    data = f.readlines()

sumChange = []
newIp = []
disappearIp = []
changeIp = []
for line in data:
    line = line.rstrip()
    numberStr = line[line.find('[')+1:-1]
    numbers = numberStr.split(',')
    sumChange.append(int(numbers[0]))
    newIp.append(int(numbers[1]))
    disappearIp.append(int(numbers[2]))
    changeIp.append(int(numbers[3]))

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(sumChange, bins = 360, range = (0, 360), histtype='step',normed=1, cumulative=True, label='total change')
ax.hist(newIp, bins = 286, range = (0, 285), histtype='step',normed=1, cumulative=True, label='new Ip ratio')
ax.hist(disappearIp, bins = 286, range = (0, 285), histtype='step',normed=1, cumulative=True, label='disappear ip ratio')
ax.hist(changeIp, bins = 286, range = (0, 285), histtype='step',normed=1, cumulative=True, label='change ip ratio')
ax.grid(True)
ax.legend(loc='right')
ax.set_title('CDF with Sliding Window')
ax.set_xlabel('number of time changed(record every 20 mins)')
ax.set_ylabel('Percentage')
plt.show()
