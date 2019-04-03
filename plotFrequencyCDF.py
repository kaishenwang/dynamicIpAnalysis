import sys
import matplotlib.pyplot as plt
import matplotlib as mpl

def fix_hist_step_vertical_line_at_end(ax):
    axpolygons = [poly for poly in ax.get_children() if isinstance(poly, mpl.patches.Polygon)]
    for poly in axpolygons:
        poly.set_xy(poly.get_xy()[:-1])


with open('changeTime.txt') as f:
    data = f.readlines()
data = [float(x.rstrip()) for x in data]

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(data, bins = 500, range = (0, 16),histtype='step',normed=1, cumulative=True, label='total change')
fix_hist_step_vertical_line_at_end(ax)
ax.legend(loc='right')
ax.set_xlabel('average time to change IP info (in minutes)')
ax.set_ylabel('')
plt.show()
plt.savefig('/Users/kaishenwang/CT/dynamicIpAnalysis/average_time_to_change.png', dpi=500)
