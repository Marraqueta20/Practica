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
# specify model
lat=[[0.5]]
orb=[[0.],[0.5]]
my_model = tb_model(1,1,lat,orb,nspin=1)
# =============================================================================
# my_model.set_onsite(-0.5, 0, mode="reset")
# my_model.set_onsite(0.5,1, mode="reset")
# =============================================================================
my_model.set_hop(-2, 0, 1, [0])
#my_model.set_hop(1, 1, 0, [0])
my_model.set_hop(-1, 1, 0, [1])

(fig, ax) = my_model.visualize(0)

# define a path in k-space
(k_vec,k_dist,k_node)=my_model.k_path('full',100)
k_label=[r"$0$",r"$\pi$", r"$2\pi$"]

# solve model
evals=my_model.solve_all(k_vec)

# plot band structure
fig, ax = plt.subplots()
ax.plot(k_dist,evals[0])
ax.plot(k_dist,evals[1])
ax.set_title("SSH model band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")
ax.set_xticks(k_node)
ax.set_xticklabels(k_label)
for n in range(len(k_node)):
  ax.axvline(x=k_node[n], linewidth=0.5, color='k')
fig.tight_layout()
fig.savefig("la_Otra_Banda.pdf")

# =============================================================================
# # visualize infinite model
# (fig,ax)=my_model.visualize(0)
# ax.set_title("Graphene, bulk")
# ax.set_xlabel("x coordinate")
# ax.set_ylabel("y coordinate")
# fig.tight_layout()
# fig.savefig("visualize_bulk.pdf")
# 
# # cutout finite model along direction 0
# cut_one=my_model.cut_piece(8,0,glue_edgs=False)
# #
# (fig,ax)=cut_one.visualize(0)
# ax.set_title("Graphene, ribbon")
# ax.set_xlabel("x coordinate")
# ax.set_ylabel("y coordinate")
# fig.tight_layout()
# fig.savefig("visualize_ribbon.pdf")
# 
# # cutout finite model along direction 1 as well
# 
# print('Done.\n')
# =============================================================================
