#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:10:23 2019

@author: lucasgonzalez
"""
from pythtb import *
import matplotlib.pyplot as plt
import numpy as np
# specify model
lat=[[1.]]
orb=[[0.0]]
my_model=tb_model(1,1,lat,orb,nspin=1)
my_model.set_hop(-0.5, 0, 0, [1])


# define a path in k-space
(k_vec,k_dist,k_node)=my_model.k_path('full',100)
k_label=[r"$0$",r"$\pi$", r"$2\pi$"]

# solve model
evals=my_model.solve_all(k_vec)

# plot band structure
fig, ax = plt.subplots()
ax.plot(k_dist,evals[0])
ax.set_title("1D chain band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")
ax.set_xticks(k_node)
ax.set_xticklabels(k_label)
#ax.set_xlim(-0.2,1.2)
for n in range(len(k_node)):
  ax.axvline(x=k_node[n], linewidth=0.5, color='k')
fig.tight_layout()
fig.savefig("simple_band.pdf")

# visualize infinite model
(fig,ax)=my_model.visualize(0)
ax.set_title("Graphene, bulk")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_bulk.pdf")

# cutout finite model along direction 0
cut_one=my_model.cut_piece(8,0,glue_edgs=False)
#
(fig,ax)=cut_one.visualize(0)
ax.set_title("Graphene, ribbon")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualize_ribbon.pdf")

# cutout finite model along direction 1 as well

print('Done.\n')
