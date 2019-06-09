import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import normal1
'''
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if (line_count > 0):
            print(map(row))
        line_count += 1
'''

data = normal1.data
exp1_means = data['pbft']['l_mean']
exp1_std = data['pbft']['l_std']
exp2_means = data['pbft_vm']['l_mean']
exp2_std = data['pbft_vm']['l_std']
exp1_label = 'PBFT on Mac'
exp2_label = 'PBFT on VM'

ind = np.arange(len(exp1_means))  # the x locations for the groups
width = 0.1  # the width of the bars
seperateDist = 0.01

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2 - seperateDist, exp1_means, width, yerr=exp1_std,
                label=exp1_label)
rects2 = ax.bar(ind + width/2 + seperateDist, exp2_means, width, yerr=exp2_std,
                label=exp2_label)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('# Nodes')
ax.set_title('Correctness')
ax.set_xticks(ind)
ax.set_xticklabels(('16', '32', '64'))
plt.ylim(top=1100)
ax.legend()

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

fig.tight_layout()

plt.show()