# Author: mjbeyeler, 2021

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

def qq_log(p_vals, s=5, plotExpected=False, bonfThres=False, col='b', cut=None, f=[], ax=[], ax2=[], fontsize=12, figsize=(6.4,4.8)):

    extraSpace=1/4.8*figsize[0]

    # remove NaNs
    p_vals = np.asarray(p_vals)[~np.isnan(p_vals)]
    N = len(p_vals)

    # p_vals under null are uniformally distributed.
    # dividing the uniform distribution in len(p_vals) QUANTILES
    # N quantiles divide the distribution in N+1 groups
    # The N quantiles I find by spanning space btwn 0 and 1 in N+2 points, omitting both 0 and 1,
    # keeping the N quantiles.
    expected = [rank/(N+1) for rank in range(1,N+1)]

    # SCAFFOLD AND helper lines building
    if f==[]:

        if cut==None:
            
            f, ax = plt.subplots(1,1)

            if bonfThres==True:
                ax.hlines(-np.log10(0.05/len(p_vals)), min(-np.log10(expected)), max(-np.log10(expected)), 'g', '--')

            if plotExpected==True:
                ax.plot(-np.log10(expected),-np.log10(expected), 'gray', linestyle='dashed')

                # beta(rank, N + 1 - rank)
                upper_bound = [beta.ppf(0.975,rank,N+1-rank) for rank in range(1,N+1)]
                lower_bound = [beta.ppf(0.025,rank,N+1-rank) for rank in range(1,N+1)]

                plt.fill_between(-np.log10(expected), -np.log10(lower_bound), -np.log10(upper_bound), color='gray', alpha=0.5)

        else:

            # if cut would hide data points, return error
            if sum([(i < cut[1]) & (i > cut[0]) for i in -np.log10(p_vals)]):
                print("ERROR: There are points in the cut region")
                return

            # everything seems to be ok, so building the split plot:
            above_max=max(max(-np.log10(expected)), max(-np.log10(p_vals)))+extraSpace
            below_min=min(min(-np.log10(expected)), min(-np.log10(p_vals)))-extraSpace
            above_below_ratio=(above_max-cut[1])/(cut[0]-below_min)

            f, (ax, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [above_below_ratio, 1]})
            plt.subplots_adjust(hspace=0.05)

            # zoom-in / limit the view to different portions of the data
            ax.set_ylim(cut[1], above_max)  # outliers only
            ax2.set_ylim(below_min, cut[0])  # most of the data

            # diagonal lines
            d = .015  # how big to make the diagonal lines in axes coordinates
            # arguments to pass to plot, just so we don't keep repeating them
            kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)

            #Using the above-below subplot vertical ratio to correct for
            #diagonal differences
            ax.plot((-d, +d), (-d/above_below_ratio, +d/above_below_ratio), **kwargs)        # top-left diagonal
            ax.plot((1 - d, 1 + d), (-d/above_below_ratio, +d/above_below_ratio), **kwargs)  # top-right diagonal

            kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
            ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
            ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

            if bonfThres==True:
                ax.hlines(-np.log10(0.05/len(p_vals)), min(-np.log10(expected)), max(-np.log10(expected)), 'g', '--')
                ax2.hlines(-np.log10(0.05/len(p_vals)), min(-np.log10(expected)), max(-np.log10(expected)), 'g', '--')

            if plotExpected==True:
                ax.plot(-np.log10(expected),-np.log10(expected), 'gray', linestyle='dashed')
                ax2.plot(-np.log10(expected),-np.log10(expected), 'gray', linestyle='dashed')

                # beta(rank, N + 1 - rank)
                upper_bound = [beta.ppf(0.975,rank,N+1-rank) for rank in range(1,N+1)]
                lower_bound = [beta.ppf(0.025,rank,N+1-rank) for rank in range(1,N+1)]

                ax.fill_between(-np.log10(expected), -np.log10(lower_bound), -np.log10(upper_bound), color='gray', alpha=0.5)
                ax2.fill_between(-np.log10(expected), -np.log10(lower_bound), -np.log10(upper_bound), color='gray', alpha=0.5)


            # hide the spines between ax and ax2
            ax.spines['bottom'].set_visible(False)
            ax2.spines['top'].set_visible(False)
            ax.xaxis.tick_top()
            ax.tick_params(labeltop=False)  # don't put tick labels at the top
            ax2.xaxis.tick_bottom()

    # if first sequence of data already drawn, again check if points would be cut out
    elif not cut==None:
        if sum([(i < ax.get_ylim()[0]) & (i > ax2.get_ylim()[1]) for i in -np.log10(p_vals)]):
            print("Error: There are points in the cut region")
            return



    # DRAWING THE ACTUAL SCATTER
    if cut==None:
        h=ax.scatter(-np.log10(expected), -np.log10(np.sort(p_vals)), s=s, c=col, alpha=1)
        return f, ax, h, expected
    else:
        h=ax.scatter(-np.log10(expected), -np.log10(np.sort(p_vals)), s=s, c=col)
        h2=ax2.scatter(-np.log10(expected), -np.log10(np.sort(p_vals)), s=s, c=col)
        return f, ax, ax2, h, h2, expected
