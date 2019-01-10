#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:23:54 2019

@author: lucasgonzalez
"""
from __future__ import print_function
from pythtb import *
import matplotlib.pyplot as plt
import numpy as np

t = 1.0
i = 0.5

# specify model
lat=[[1.0]]
orb=[[0.],[1/3]]
my_model = tb_model(1,1,lat,orb,nspin=1)
my_model.set_hop(t, 0, 1, [0])
my_model.set_hop(i, 1, 0, [1])

# =============================================================================
# delta = 2
# 
# onsite_0=delta*(-1.0)*np.cos(2.0*np.pi*(1-0.0/3.0))
# onsite_1=delta*(-1.0)*np.cos(2.0*np.pi*(1-1.0/3.0))
# my_model.set_onsite([onsite_0,onsite_1],mode="reset")
# =============================================================================


#my_model.set_onsite([2,0.99],mode="reset")


# define a path in k-space
(k_vec,k_dist,k_node)=my_model.k_path([[-0.5],[0.5]],100,report=True)
k_label=[r"$0$",r"$\pi$", r"$2\pi$"]

# solve model
evals=my_model.solve_all(k_vec, eig_vectors = False)


# =============================================================================
# 
# # Veamos la celda unitaria
# (fig, ax) = my_model.visualize(0)
# ax.set_title("Graphene, bulk")
# ax.set_xlabel("x coordinate")
# ax.set_ylabel("y coordinate")
# fig.tight_layout()
# fig.savefig("visualize_UCell.png")
# 
# =============================================================================
# =============================================================================
# # cutout finite model along direction 0
# cut_one=my_model.cut_piece(8,0,glue_edgs=False)
# #
# (fig,ax)=cut_one.visualize(0)
# ax.set_title("SSH, ribbon")
# ax.set_xlabel("x coordinate")
# ax.set_ylabel("y coordinate")
# fig.tight_layout()
# fig.savefig("visualize_ribbon_2.png")
# =============================================================================


# plot band structure
fig_band,   ax_band   = plt.subplots()
for band in range(len(evals)):
    ax_band.plot(k_dist,evals[band,:],"k-",linewidth=0.5)
ax_band.set_title("SSH model band structure")
ax_band.set_xlabel("Path in k-space")
ax_band.set_ylabel("Band energy")
#ax_band.set_xticks(k_node)
#ax_band.set_xticklabels(k_label)
#for n in range(len(k_node)):
#  ax_band.axvline(x=k_node[n], linewidth=0.5, color='k')
fig_band.tight_layout()
fig_band.savefig("la_Otra_Banda.png")





