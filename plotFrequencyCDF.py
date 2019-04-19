import sys
import matplotlib.pyplot as plt
import matplotlib as mpl

def fix_hist_step_vertical_line_at_end(ax):
    axpolygons = [poly for poly in ax.get_children() if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])


with open('changeTime.txt') as f:
    data = f.readlines()
data = [float(x.rstrip())*60 for x in data]
data += [data[-1]*(500 - len(data))]

fig, ax = plt.subplots(figsize=(8, 4))

#xmin=data[-1],xmax=data[-1]*2
ax.axhline(y=1,linewidth=1, xmin=0.95,xmax=1,alpha=0.7)
ax.axhline(y=1,linewidth=1, color='orange',linestyle='--', alpha=0.7, label='100%')
ax.axvline(x=15*60,linewidth=0.7, color='black',linestyle='--', alpha=0.7, label='15 minutes')
ax.hist(data, bins = 360, range = (0, 1000),histtype='step',normed=1, cumulative=True, label='total change')
fix_hist_step_vertical_line_at_end(ax)
ax.set_xscale('log')

ax.legend(loc='right')
ax.set_xlabel('average time to change IP info (in seconds)')
ax.set_ylabel('')
#plt.show()
plt.savefig('/Users/kaishenwang/CT/dynamicIpAnalysis/average_time_to_change.png', dpi=500)
