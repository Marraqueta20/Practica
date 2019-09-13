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

t = 0.5
i = 1.5

# Specify model
lat=[[1.0]]
orb=[[0.],[1/3]]
my_model = tb_model(1,1,lat,orb,nspin=1)
my_model.set_hop(t, 0, 1, [0])
my_model.set_hop(i, 1, 0, [1])


# Define a path in k-space
(k_vec,k_dist,k_node)=my_model.k_path([[-0.5],[0.5]],100,report=True)
k_label=[r"$0$",r"$\pi$", r"$2\pi$"]

# Solve model
(evals,kvals)=my_model.solve_all(k_vec, eig_vectors = True)


# visualize infinite model
(fig,ax)=my_model.visualize(0)
ax.set_title("SSH, bulk")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
fig.tight_layout()
fig.savefig("visualice_UCell.png")

# Plot band structure
fig_band,   ax_band   = plt.subplots()
for band in range(len(evals)):
    ax_band.plot(k_dist,evals[band,:],"k-",linewidth=0.5)
ax_band.set_title("Estructura de bandas para modelo SSH")
ax_band.set_xlabel("Espacio k")
ax_band.set_ylabel("Energía")
fig_band.tight_layout()
fig_band.savefig("la_Otra_Banda.png")

