import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import normal1, normal2
import l04, l2
import partition, partition2
import static, adaptive, dexon
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
width = 0.06  # the width of the bars
seperateDist = 0.04
def draw(expData):
    fig, ax = plt.subplots()
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Latency (ms)')
    ax.set_xlabel('# Nodes')
    ax.set_title('Adaptive Attack')
    ind = np.arange(len(expData[0]['means']))  # the x locations for the groups
    ax.set_xticks(ind)
    ax.set_xticklabels(('16', '32', '64'))
    yMax = 0
    for data in expData:
        print(data)
        mMax = max([a + b for a, b in zip(data['means'], data['std'])])
        yMax = mMax if mMax > yMax else yMax

        positions = ind + data['pos'] * (width / 2 + seperateDist)
        rect = ax.bar(positions, data['means'], width, yerr=data['std'],
                label=data['label'], color=data['color'])
        
        #autolabel(rects, ax)
    print(yMax)
    plt.ylim(top=yMax + 1100)
    ax.legend()
    fig.tight_layout()
    plt.show()

normalData = normal1.data
attackData = dexon.data
expData = [
    {
        'means': normalData['dexon-hba']['l_mean'],
        'std': normalData['dexon-hba']['l_std'],
        'label': 'DEXON HBA',
        'color': '#e74c3c'
    },
    {
        'means': attackData['dexon-hba']['l_mean'],
        'std': attackData['dexon-hba']['l_std'],
        'label': 'DEXON HBA under attack',
        'color': '#e67e22'
    },
    # {
    #     'means': normalData['v-adaptive']['l_mean'],
    #     'std': normalData['v-adaptive']['l_std'],
    #     'label': 'ADD+3',
    #     'color': '#f1c40f'
    # },
    # {
    #     'means': attackData['v-adaptive']['l_mean'],
    #     'std': attackData['v-adaptive']['l_std'],
    #     'label': 'ADD+3 under attack',
    #     'color': '#2ecc71'
    # },
    # {
    #     'means': data['v-basic']['l_mean'],
    #     'std': data['v-basic']['l_std'],
    #     'label': 'ADD+ v1',
    #     'pos': 1,
    #     'color': '#3498db'
    # },
    # {
    #     'means': data['v-basic']['l_mean'],
    #     'std': data['v-basic']['l_std'],
    #     'label': 'ADD+ v1',
    #     'pos': 2,
    #     'color': '#34495e'
    # },
    # {
    #     'means': data['v-basic']['l_mean'],
    #     'std': data['v-basic']['l_std'],
    #     'label': 'ADD+ v1',
    #     'pos': 3,
    #     'color': '#8e44ad'
    # }
]
# calculate pos
l = len(expData)
poss = range(0, l)
if (l % 2 == 0):
    poss = [pos - l / 2 for pos in poss]
    for i in range(0, l):
        if (poss[i] >= 0):
            poss[i] += 1
else:
    poss = [pos - l / 2 for pos in poss]

print(poss)
for data, pos in zip(expData, poss):
    data['pos'] = pos
draw(expData)
