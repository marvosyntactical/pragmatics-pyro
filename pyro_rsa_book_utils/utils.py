import pyro
import pyro.distributions as dist

import torch

import matplotlib.pyplot as plt

def silly_plotter(d):
    # silly plotting helper from official pyro RSA examples
    support = d.enumerate_support()
    data = [d.log_prob(s).exp().item() for s in d.enumerate_support()]
    names = list(map(str, support))

    ax = plt.subplot(111)
    width = 0.3
    bins = [x-width/2 for x in range(1, len(data) + 1)]
    ax.bar(bins,data,width=width)
    ax.set_xticks(list(range(1, len(data) + 1)))
    ax.set_xticklabels(names, rotation=45, rotation_mode="anchor", ha="right")

def sillier_plotter(d: dist, threshold_bins=20, x_name=None, y_name=None):
    """
    adapted, even sillier plotter for two dimensional joint dist
    plots marginal distributions for 2 RVs
    if one of the numbers of support bins
    exceeds threshold_bins, that dist is drawn as a line graph
    otherwise as a bar plot labels
    """

    def visualise_dist(support, values, ax, names=None, title=None):
        N = len(support)
        assert len(values) == N, (N, len(values))
        if N > threshold_bins:
            ax.plot(support, values)
        else:
            width=0.3
            ax.bar(support, values, width=width)
            ax.set_xticks(list(range(1,N+1)))
            if names is not None:
                ax.set_xticklabels(
                    names,
                    rotation=45,
                    rotation_mode="anchor",
                    ha="right"
                )
        ax.title.set_text(title)

    joint = d.enumerate_support() # p(X,Y)
    X, Y = zip(*joint)
    X, Y = sorted(list(set(X))), sorted(list(set(Y)))

    # marginalize out Y
    pX = [
        sum([torch.sum(torch.cat([y * d.log_prob(joint[k]).exp() for k in range(len(joint)) if (joint[k][1]==y and joint[k][0]==x)])).item()
             for y in Y])
        for x in X
    ]
    axes_x = plt.subplot(121)

    visualise_dist(X, pX, axes_x, names=X, title=x_name)

    # marginalize out X
    pY = [
        sum([torch.sum(torch.cat([x * d.log_prob(joint[k]).exp() for k in range(len(joint)) if (joint[k][0]==x and joint[k][1]==y)])).item()
             for x in X])
        for y in Y
    ]
    axes_y = plt.subplot(122)

    visualise_dist(Y, pY, axes_y, names=Y, title=y_name)

    plt.tight_layout()
