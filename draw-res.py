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
    #ax.set_title(r'$Network = \mathcal{N}(250, 50), \lambda = 1000$')
    ax.set_title('Responsiveness')
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
    plt.ylim(top=yMax + 10000)
    ax.legend(loc='upper left')
    fig.tight_layout()
    plt.show()

n1Data = normal1.data
n2Data = normal2.data
lData = l2.data
t = 'l'
mean = t + '_mean'
std = t + '_std'
expData = [
    {
        'means': n2Data['v-basic'][mean],
        'std': n2Data['v-basic'][std],
        'label': 'ADD+v1 (' + r'$Network = \mathcal{N}(250, 50), \lambda = 1000$' + ')',
        'color': '#e74c3c'
    },
    {
        'means': n1Data['v-basic'][mean],
        'std': n1Data['v-basic'][std],
        'label': 'ADD+v1 (' + r'$Network = \mathcal{N}(1000, 300), \lambda = 1000$' + ')',
        'color': '#e67e22'
    },
    {
        'means': lData['v-basic'][mean],
        'std': lData['v-basic'][std],
        'label': 'ADD+v1 (' + r'$Network = \mathcal{N}(250, 50), \lambda = 2000$' + ')',
        'color': '#f1c40f'
    },
    {
        'means': n2Data['pbft'][mean],
        'std': n2Data['pbft'][std],
        'label': 'PBFT (' + r'$Network = \mathcal{N}(250, 50), \lambda = 1000$' + ')',
        'color': '#2ecc71'
    },
    {
        'means': n1Data['pbft'][mean],
        'std': n1Data['pbft'][std],
        'label': 'PBFT (' + r'$Network = \mathcal{N}(1000, 300), \lambda = 1000$' + ')',
        'color': '#3498db'
    },
    {
        'means': lData['pbft'][mean],
        'std': lData['pbft'][std],
        'label': 'PBFT (' + r'$Network = \mathcal{N}(250, 50), \lambda = 2000$' + ')',
        'color': '#34495e'
    },
    # {
    #     'means': data['pbft'][mean],
    #     'std': data['pbft'][std],
    #     'label': 'PBFT',
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
