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
# for different network
width = 0.25  # the width of the bars
seperateDist = 0.15
# for different lambda
#width = 0.2  # the width of the bars
#seperateDist = 0.15
def draw(expData):
    fig, ax = plt.subplots()
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Latency (s)')
    #ax.set_xlabel('# Nodes')
    #ax.set_title(r'$Network = \mathcal{N}(250, 50), \lambda = 1000$')
    # for different network
    ax.set_title('Responsiveness with Different Network')

    # for different lambda
    #ax.set_title('Different Network Configuration ' + r'$\lambda$')
    ind = np.arange(len(expData[0]['means']))  # the x locations for the groups

    ax.set_xticks(ind)
    ax.tick_params(axis='x', which='major', labelsize=9)
    ax.set_xticklabels(('ADD+v1', 'ADD+v2', 'ADD+v3', 'Algorand', 'Async BA', 'DEXON HBA', 'PBFT'))
    yMax = 0
    for data in expData:
        print(data)
        mMax = max([a + b for a, b in zip(data['means'], data['std'])])
        yMax = mMax if mMax > yMax else yMax
        # 0.14 is for different network
        positions = ind + data['pos'] * (width / 2 + seperateDist) + 0.14
        rect = ax.bar(positions, data['means'], width, yerr=data['std'],
                label=data['label'], color=data['color'])
        
        #autolabel(rects, ax)
    print(yMax)
    plt.axvline(3.5, color='k', linestyle='dashed', linewidth=1)

    plt.ylim(top=yMax + 1)
    ax.legend(loc='upper left')
    fig.tight_layout()
    plt.show()

n1Data = normal1.data
n2Data = normal2.data
l2Data = l2.data
l04Data = l04.data
t = 'l'
mean = t + '_mean'
std = t + '_std'
# for different network
d1 = {
    'mean': [
        n2Data['v-basic'][mean][0], 
        n2Data['v-vrf'][mean][0], 
        n2Data['v-adaptive'][mean][0], 
        n2Data['algorand'][mean][0],
        n2Data['aba'][mean][0],
        n2Data['dexon-hba'][mean][0],
        n2Data['pbft'][mean][0]
    ],
    'std': [
        n2Data['v-basic'][std][0], 
        n2Data['v-vrf'][std][0], 
        n2Data['v-adaptive'][std][0], 
        n2Data['algorand'][std][0],
        n2Data['aba'][std][0],
        n2Data['dexon-hba'][std][0],
        n2Data['pbft'][std][0]]
}
d2 = {
    'mean': [
        n1Data['v-basic'][mean][0], 
        n1Data['v-vrf'][mean][0], 
        n1Data['v-adaptive'][mean][0], 
        n1Data['algorand'][mean][0],
        n1Data['aba'][mean][0],
        n1Data['dexon-hba'][mean][0],
        n1Data['pbft'][mean][0]
    ],
    'std': [
        n1Data['v-basic'][std][0], 
        n1Data['v-vrf'][std][0], 
        n1Data['v-adaptive'][std][0], 
        n1Data['algorand'][std][0],
        n1Data['aba'][std][0],
        n1Data['dexon-hba'][std][0],
        n1Data['pbft'][std][0]]
}
# for different lambda
d3 = {
    'mean': [
        l04Data['v-basic'][mean][0], 
        l04Data['v-vrf'][mean][0], 
        l04Data['v-adaptive'][mean][0], 
        l04Data['algorand'][mean][0],
        l04Data['aba'][mean][0],
        l04Data['dexon-hba'][mean][0],
        l04Data['pbft'][mean][0],
    ],
    'std': [
        l04Data['v-basic'][std][0], 
        l04Data['v-vrf'][std][0], 
        l04Data['v-adaptive'][std][0], 
        l04Data['algorand'][std][0],
        l04Data['aba'][std][0],
        l04Data['dexon-hba'][std][0],
        l04Data['pbft'][std][0],
    ]
}
d4 = {
    'mean': [
        n1Data['v-basic'][mean][0], 
        n1Data['v-vrf'][mean][0], 
        n1Data['v-adaptive'][mean][0], 
        n1Data['algorand'][mean][0],
        n1Data['aba'][mean][0],
        n1Data['dexon-hba'][mean][0],
        n1Data['pbft'][mean][0],
    ],
    'std': [
        n1Data['v-basic'][std][0], 
        n1Data['v-vrf'][std][0], 
        n1Data['v-adaptive'][std][0], 
        n1Data['algorand'][std][0],
        n1Data['aba'][std][0],
        n1Data['dexon-hba'][std][0],
        n1Data['pbft'][std][0],
    ]

}
d5 = {
    'mean': [
        l2Data['v-basic'][mean][0], 
        l2Data['v-vrf'][mean][0], 
        l2Data['v-adaptive'][mean][0], 
        l2Data['algorand'][mean][0],
        l2Data['aba'][mean][0],
        l2Data['dexon-hba'][mean][0],
        l2Data['pbft'][mean][0],
    ],
    'std': [
        l2Data['v-basic'][std][0], 
        l2Data['v-vrf'][std][0], 
        l2Data['v-adaptive'][std][0], 
        l2Data['algorand'][std][0],
        l2Data['aba'][std][0],
        l2Data['dexon-hba'][std][0],
        l2Data['pbft'][std][0],
    ]

}

expData = [
    # for different network
    {
        'means': d1['mean'],
        'std': d1['std'],
        'label': r'$\mathcal{N}(1000, 300)$',
        'color': colors['r']
    },
    {
        'means': d2['mean'],
        'std': d2['std'],
        'label': r'$\mathcal{N}(250, 50)$',
        'color': colors['g']
    },
    # for different lambda
    # {
    #     'means': d3['mean'],
    #     'std': d3['std'],
    #     'label': r'$\lambda = 400$',
    #     'color': colors['g']
    # },
    # {
    #     'means': d4['mean'],
    #     'std': d4['std'],
    #     'label': r'$\lambda = 1000$',
    #     'color': colors['y']
    # },
    #     {
    #     'means': d5['mean'],
    #     'std': d5['std'],
    #     'label': r'$\lambda = 2000$',
    #     'color': colors['r']
    # }
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
poss = [-1, 0, 1]
for data, pos in zip(expData, poss):
    data['pos'] = pos
draw(expData)
