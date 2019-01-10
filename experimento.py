#!/usr/bin/env python

# one-dimensional family of tight binding models
# parametrized by one parameter, lambda

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt

# define lattice vectors
lat=[[1.0]]
# define coordinates of orbitals
orb=[[0.0],[1.0/3.0]]

# make one dimensional tight-binding model
my_model=tb_model(1,1,lat,orb)

# set model parameters
delta=2.0
t=1.0
i=0.5
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t, 0, 1, [0])
my_model.set_hop(i, 1, 0, [1])

# plot band structure for each lambda
fig_band,   ax_band   = plt.subplots()

#for i_lambda in range(path_steps):
    # for each step along the path compute onsite terms for each orbital
lmbd=1
onsite_0=delta*(-1.0)*np.cos(2.0*np.pi*(1-0.0/3.0))
onsite_1=delta*(-1.0)*np.cos(2.0*np.pi*(1-1.0/3.0))
    #onsite_2=delta*(-1.0)*np.cos(2.0*np.pi*(lmbd-2.0/3.0))

    # update onsite terms by rewriting previous values
my_model.set_onsite([onsite_0,onsite_1],mode="reset")

    # create k mesh over 1D Brillouin zone
(k_vec,k_dist,k_node)=my_model.k_path([[-0.5],[0.5]], 100,report=True)
    # solve model on all of these k-points
eval=my_model.solve_all(k_vec,eig_vectors=False)

    # plot band structure for all two bands
for band in range(len(eval)):
    ax_band.plot(k_dist,eval[band,:],"k-",linewidth=0.5)


(fig, ax) = my_model.visualize(0)


# finish plot for band structure
ax_band.set_title("Band structure")
ax_band.set_xlabel("Path in k-vector")
ax_band.set_ylabel("Band energies")
ax_band.set_xlim(0.0,1.0)
fig_band.tight_layout()
fig_band.savefig("3site_band.png")


# cutout finite model along direction 0
cut_one=my_model.cut_piece(8,0,glue_edgs=False)
#
(fig,ax)=cut_one.visualize(0)
ax.set_title("SSH, ribbon")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_ribbon_2.png")

# =============================================================================
# # finish plot of onsite terms
# ax_onsite.set_title("Onsite energy for all three orbitals")
# ax_onsite.set_xlabel("Lambda parameter")
# ax_onsite.set_ylabel("Onsite terms")
# ax_onsite.set_xlim(0.0,1.0)
# fig_onsite.tight_layout()
# fig_onsite.savefig("3site_onsite.pdf")
# 
# =============================================================================
# =============================================================================
# # finish plot for Wannier center
# ax_wann.set_title("Center of Wannier function")
# ax_wann.set_xlabel("Lambda parameter")
# ax_wann.set_ylabel("Center (reduced coordinate)")
# ax_wann.set_xlim(0.0,1.0)
# fig_wann.tight_layout()
# fig_wann.savefig("3site_wann.pdf")
# 
# print('Done.\n')
# =============================================================================
