#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:48:11 2019

@author: lucasgonzalez
"""

from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt

def set_model(t, delta, theta):
    lat=[[1.0]]
    orb=[[0.],[1/3],[2/3]]
    #orb=[[0.],[1/2]]
    model = tb_model(1,1,lat,orb)
    model.set_hop(t, 0, 1, [0])
    model.set_hop(t, 1, 2, [0])
    model.set_hop(t, 2, 0, [1])
    #model.set_hop(t,1,0,[1])
    onsite_0=delta*np.cos(2.0*np.pi*(theta))
    onsite_1=delta*np.cos(2.0*np.pi*(1.0/3.0+theta))
    onsite_2=delta*np.cos(2.0*np.pi*(2.0/3.0+theta))
    model.set_onsite([onsite_0, onsite_1, onsite_2])
    #model.set_onsite([onsite_0, onsite_1])
    return(model)

# Parametros
t = 1.5
delta = 2.0

# Evolucionamos la fase theta por un camino
path_steps=500
all_theta=np.linspace(0.0,1.0,path_steps,endpoint=True)

# Tamaño de la cadena
num_cells=10
#num_orb=2*num_cells
num_orb=3*num_cells

# inicializamos los arrays que guardaran los autovalores y x expectations
ch_eval=np.zeros([num_orb,path_steps],dtype=float)
ch_xexp=np.zeros([num_orb,path_steps],dtype=float)

for i_theta in range(path_steps):
    theta=all_theta[i_theta]

    # Se construye el modelo y resolvemos
    my_model=set_model(t,delta,theta)
    ch_model=my_model.cut_piece(num_cells,0, glue_edgs=False)
    (eval,evec)=ch_model.solve_all(eig_vectors=True)

    # Guardamos los autovalores
    ch_eval[:,i_theta]=eval
    ch_xexp[:,i_theta]=ch_model.position_expectation(evec,0)

#plot autovalores vs. theta

(fig, ax) = plt.subplots()

# loop sobre las "bandas"
for n in range(num_orb):
    # diminish the size of the ones on the borderline
    xcut=2.   # discard points below this
    xfull=4.  # use sybols of full size above this
    size=(ch_xexp[n,:]-xcut)/(xfull-xcut)
    for i in range(path_steps):
        size[i]=min(size[i],1.)
        size[i]=max(size[i],0.1)
    ax.scatter(all_theta[:],ch_eval[n,:], edgecolors='none', s=size*6., c='k')

ax.set_title("Autovalores para modelo de 3 sitios finito")
ax.set_xlabel(r"Fase $\theta$")
ax.set_ylabel("Energia")
ax.set_xlim(0.,1.)
fig.tight_layout()
fig.savefig("3site_endstates.png")
plt.show()
    