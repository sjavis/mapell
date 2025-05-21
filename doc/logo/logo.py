import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "text.latex.preamble": r"\usepackage{tgadventor}"
})

def coefs(x0, y0, x1, y1, m0, m1):
    b = 2/(m0-m1) * (y1 - y0 - m1*(x1 - x0))
    d = m0 * b
    a = x1 - x0 - b
    c = y1 - y0 - d
    return a, b, c, d

def plot_curve(x0, y0, x1, y1, m0, m1, col, lw):
    a, b, c, d = coefs(x0, y0, x1, y1, m0, m1)
    t = np.linspace(0, 1, 20)
    x = a*t**2 + b*t + x0
    y = c*t**2 + d*t + y0
    plt.plot(x, y, c=col, lw=lw)[0].set_solid_capstyle('round')
    plt.plot(-x, y, c=col, lw=lw)[0].set_solid_capstyle('round')

def plot(c, text=False):
    figsize = (4,1) if text else (1,1)
    fig = plt.figure(frameon=False, figsize=figsize)
    ax = fig.add_axes([0., 0., 1., 1.])
    ax.set_axis_off()
    ax.set_aspect('equal')

    xy0 = [0, 0]
    xy1 = [1.3, 1]
    xy2 = [2, 2]
    xy3 = [1.5, 4]
    lw = 6

    plot_curve(*xy0, *xy1, 5, -0.8, c, lw)
    plot_curve(*xy1, *xy2, -10, -0.8, c, lw)
    plot_curve(*xy2, *xy3, -3, 100, c, lw)

    plt.plot([0,xy1[0]], [xy1[0]+xy1[1],xy1[1]], c=c, lw=lw)[0].set_solid_capstyle('round')
    plt.plot([0,-xy1[0]], [xy1[0]+xy1[1],xy1[1]], c=c, lw=lw)[0].set_solid_capstyle('round')
    plt.plot([0,xy2[0]], [xy2[0]+xy2[1],xy2[1]], c=c, lw=lw)[0].set_solid_capstyle('round')
    plt.plot([0,-xy2[0]], [xy2[0]+xy2[1],xy2[1]], c=c, lw=lw)[0].set_solid_capstyle('round')
    plt.plot([0,0], [0,xy3[1]], c=c, lw=lw)[0].set_solid_capstyle('round')

    if (text):
        text = plt.text(1.8*xy2[0], xy3[1]/2, 'MAPELL', va='center', size=50, c=c)
        fig.canvas.draw()
        bbox = text.get_window_extent(renderer=fig.canvas.get_renderer())
        bbox_data = bbox.transformed(ax.transData.inverted())
        ax.set_xlim(right=bbox_data.x1)

plot('red')
plt.savefig('logo.png', transparent=True)
plt.close()

plot('red', text=True)
plt.savefig('logo_text.png', transparent=True)
plt.close()

plot('w')
plt.savefig('logo2.png', transparent=True)
plt.close()

plot('w', text=True)
plt.savefig('logo2_text.png', transparent=True)
plt.close()
