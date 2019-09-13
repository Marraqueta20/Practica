#!/usr/bin/env python

# one-dimensional family of tight binding models
# parametrized by one parameter, lambda

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from __future__ import print_function
from pythtb import * # import TB model class
import numpy as np
import matplotlib.pyplot as plt
import collections as clt

# define lattice vectors
lat=[[1.0]]
# define coordinates of orbitals
orb=[[0.0],[1.0/3.0]]

# make one dimensional tight-binding model
my_model=tb_model(1,1,lat,orb)

# set model parameters
delta=2.0
t=0.5
i=1.5
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t, 0, 1, [0])
my_model.set_hop(i, 1, 0, [1])

#my_model.set_onsite([3,3])

# cutout finite model first along direction x with no PBC
tmp_model=my_model.cut_piece(25,0,glue_edgs=False)

# create k mesh over 1D Brillouin zone
(k_vec,k_dist,k_node)=my_model.k_path([[-0.5],[0.5]], 100,report=True)

(eval, evec)=my_model.solve_all(k_vec, eig_vectors = True)

# solve model on all of these k-points
(evals,evecs)=tmp_model.solve_all(eig_vectors=True)

#tmp_model.display()

ed=tmp_model.get_num_orbitals()//2


# =============================================================================
# #  GRAFICO DE LAS BANDAS PARA MODELO INFINITO
# # plot band structure for all two bands
# fig_band,   ax_band   = plt.subplots()
# for band in range(len(eval)):
#     ax_band.plot(k_dist,eval[band,:],"k-",linewidth=0.5)
# =============================================================================


# draw one of the edge states in both cases
def Fig_edge_states():
    (fig,ax)=tmp_model.visualize(0,eig_dr=evecs[ed,:],draw_hoppings=False)
    ax.set_title("Estado conductor para modelo SSH finito sin dirección periodica")
    ax.set_xlabel("x coordinate")
    ax.set_ylabel("y coordinate")
    ax.set_ylim(-10.0,10.0)
    fig.tight_layout()
    fig.savefig("edge_state.png")


#  DENSIDAD DE ESTADO
#(fig, ax) = tmp_model.visualize(0)
def State_Density():
    fig, ax = plt.subplots()
    n, bins, patches = plt.hist(evals, 100, range=(-2.5,2.5))
    ax.hist(evals,50,range=(-2.5,2.5),histtype='bar')
    ax.set_ylim(0.0,max(n)+1.0)
    ax.set_title("Densidad de estados para modelo SSH")
    ax.set_xlabel("Banda de energias")
    ax.set_ylabel("Numero de estados")
    fig.tight_layout()
    fig.savefig("SSH_finite.png")

# que tan cercano a 0
def Epsilon():
    a = []
    for i in range(len(evals)):
       k = np.absolute(evals[i])
       a = np.append(a,k)
    epsilon = min(a) - 0
    return epsilon

# Array que junta el modulo cuadrado del autovector para cada banda y orbital
# (en ese orden los índices)
def Prob_Dist():
    Weights = evecs
    for i in range(evecs.shape[0]):
        for j in range(evecs.shape[1]):
    #       for k in range(evecs.shape[2]):
            Weights[i][j] = np.inner(evecs[i][j], np.conj(evecs[i][j]))
                
    # Grafica localización de autoestados
    fig, ax = plt.subplots(2,1)
    # pick index of state in the middle of the gap
    Bandas = np.arange(tmp_model.get_num_orbitals())
    #ax[0].plot(Bandas, Weights[ed-1])
    ax[0].semilogy(Bandas, Weights[ed], 'black') 
    ax[0].set_title('Distribución de probabilidad en función de la posición')
    ax[0].set_ylabel('$log(|\psi|^{2})$')
    p = 0
    for i in range(ed - 1):
        p += 1
        ax[1].plot(Bandas, Weights[i],linewidth=0.5)
        #ax[1].semilogy(Bandas, Weights[i])
    ax[1].plot(Bandas, Weights[ed-1], 'black', label = 'Estado de borde')
    ax[1].set_ylabel('$|\psi|^{2}$')
    ax[1].set_xlabel('x')
    ax[1].legend()
    plt.show()
    fig.savefig("Prob_Dist_SSH.png")