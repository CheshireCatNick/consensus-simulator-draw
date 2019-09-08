import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import normal1, normal2
import l04, l2
import partition2, partition3
import static, adaptive, dexon

colors = {
    'r': '#e74c3c',
    'o': '#e67e22',
    'y': '#f1c40f',
    'g': '#2ecc71',
    'b': '#3498db',
    'd': '#34495e',
    'p': '#8e44ad'
}
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
    ax.set_ylabel('Latency (s)')
    ax.set_xlabel('# Nodes')
    #ax.set_title(r'$Network = \mathcal{N}(250, 50), \lambda = 1000$')
    ax.set_title('DEXON Adaptive Attack')
    ind = np.arange(len(expData[0]['means']))  # the x locations for the groups
    ax.set_xticks(ind)
    ax.set_xticklabels(('16', '32', '64'))
    yMax = 0
    for data in expData:
        print(data)
        mMax = max([a + b for a, b in zip(data['means'], data['std'])])
        yMax = mMax if mMax > yMax else yMax

        positions = ind + data['pos'] * (width / 2 + seperateDist)
        if data['label'][-6:] == 'attack':
            rect = ax.bar(positions, data['means'], width, yerr=data['std'],
                label=data['label'], color=data['color'], hatch='xxxx')
        else:
            rect = ax.bar(positions, data['means'], width, yerr=data['std'],
                label=data['label'], color=data['color'])

        
        #autolabel(rects, ax)
    print(yMax)
    plt.ylim(top=yMax + 10)
    ax.legend(loc='upper left')
    fig.tight_layout()
    #plt.axhline(60000, color='k', linestyle='dashed', linewidth=1)
    #plt.text(2, 2, 'resolve', ha='right', va='center')
    plt.show()

data = normal1.data
# add+ static attack
#attackData = static.data
# add+ adaptive attack
#attackData = adaptive.data
# dexon adaptive attack
attackData = adaptive.data
dexonAttackData = dexon.data
t = 'l'
mean = t + '_mean'
std = t + '_std'
expData = [
    # add+ static attack
    # {
    #     'means': data['v-basic'][mean],
    #     'std': data['v-basic'][std],
    #     'label': 'ADD+v1',
    #     'color': colors['r']
    # },
    # {
    #     'means': attackData['v-basic'][mean],
    #     'std': attackData['v-basic'][std],
    #     'label': 'ADD+v1 under attack',
    #     'color': colors['r']
    # },
    # {
    #     'means': data['v-vrf'][mean],
    #     'std': data['v-vrf'][std],
    #     'label': 'ADD+v2',
    #     'color': colors['g']
    # },
    # {
    #     'means': attackData['v-vrf'][mean],
    #     'std': attackData['v-vrf'][std],
    #     'label': 'ADD+v2 under attack',
    #     'color': colors['g']
    # }
    # add+ adaptive attack
    # {
    #     'means': data['v-vrf'][mean],
    #     'std': data['v-vrf'][std],
    #     'label': 'ADD+v2',
    #     'color': colors['g']
    # },
    # {
    #     'means': attackData['v-vrf'][mean],
    #     'std': attackData['v-vrf'][std],
    #     'label': 'ADD+v2 under attack',
    #     'color': colors['g']
    # },
    # {
    #     'means': data['v-adaptive'][mean],
    #     'std': data['v-adaptive'][std],
    #     'label': 'ADD+v3',
    #     'color': colors['y']
    # },
    # {
    #     'means': attackData['v-adaptive'][mean],
    #     'std': attackData['v-adaptive'][std],
    #     'label': 'ADD+v3 under attack',
    #     'color': colors['y']
    # }
    # dexon adaptive attack
    {
        'means': data['dexon-hba'][mean],
        'std': data['dexon-hba'][std],
        'label': 'DEXON HBA',
        'color': colors['p']
    },
    {
        'means': dexonAttackData['dexon-hba'][mean],
        'std': dexonAttackData['dexon-hba'][std],
        'label': 'DEXON HBA under attack',
        'color': colors['p']
    },
    {
        'means': data['v-vrf'][mean],
        'std': data['v-vrf'][std],
        'label': 'ADD+v2',
        'color': colors['g']
    },
    {
        'means': attackData['v-vrf'][mean],
        'std': attackData['v-vrf'][std],
        'label': 'ADD+v2 under attack',
        'color': colors['g']
    },
]
# latency ms to s
if (t == 'l'):
    for data in expData:
        data['means'] = [i / 1000 for i in data['means']]
        data['std'] = [i / 1000 for i in data['std']]
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
