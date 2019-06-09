import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import normal1
'''
def autolabel(rects, ax, xpos='center'):
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
'''
width = 0.1  # the width of the bars
seperateDist = 0.01
def draw(expData):
    fig, ax = plt.subplots()
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Latency (ms)')
    ax.set_xlabel('# Nodes')
    ax.set_title('Correctness')
    ind = np.arange(len(expData[0]['means']))  # the x locations for the groups
    ax.set_xticks(ind)
    ax.set_xticklabels(('16', '32', '64'))
    plt.ylim(top=1100)
    for data in expData:
        print(data)
        positions = ind + data['pos'] * (width / 2 + seperateDist)
        rects = ax.bar(positions, data['means'], width, yerr=data['std'],
                label=data['label'])
        autolabel(rects, ax)

    ax.legend()
    fig.tight_layout()
    plt.show()

data = normal1.data
exp1_means = data['pbft']['l_mean']
exp1_std = data['pbft']['l_std']
exp2_means = data['pbft_vm']['l_mean']
exp2_std = data['pbft_vm']['l_std']
exp1_label = 'PBFT on Mac'
exp2_label = 'PBFT on VM'
expData = [
    {
        'means': exp1_means,
        'std': exp1_std,
        'label': exp1_label,
        'pos': -1
    },
    {
        'means': exp2_means,
        'std': exp2_std,
        'label': exp2_label,
        'pos': 1
    }
]
draw(expData)










