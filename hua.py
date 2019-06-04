import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname()
import numpy as np
num =10
plt.rcParams['figure.figsize'] = (num, num/1.8)
r = 10.0
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
for number in range(1,41):
    plt.plot(x, y,color='black',linewidth=10)
    plt.text(0, -1.3, '%d'%number, ha='center', va= 'center',fontsize=180,family='Times New Roman')
    # plt.text(0, -1.5, '%d'%49, ha='center', va= 'center',fontsize=180,family='Times New Roman')
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('./number/%d.png'%number,dpi=500)
    plt.close()
    # break