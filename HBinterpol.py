## Module for interpolating harmonic balance datapoints
#  get_Einv() takes 4 arguments and calculates the E-inverse matrix in the HB solve
#   - T is the time period input to the solver
#   - N and K determine the size of the E matrix and are analogous to no. of time instances
#   - omegas is the list of frequencies input to the solver
#  get_interp() interpolates out the time-history of the HB datapoints given 4 inputs
#   - T is the time period input to the solver
#   - times is the time instance translated to real time
#   - omegas is the list of frequencies input to the solver
#   - hb_lift is the corresponding coefficient at each time instance
## Recommend to look at the "isogai_flutter.ipynb" notebook included with the SU2 case files

import numpy as npi

#  Einv calculation
def get_Einv(T,N,K,omegas):
    Einv = np.zeros((N,K),dtype=complex)
    for n in range(0,N):
        for k in range(0,K):
            Einv[n,k] = complex(np.cos(omegas[k]*n*T/N),np.sin(omegas[k]*n*T/N))
    return Einv

#  Interpolation
def get_interp(T,times,omegas,hb_lift):
    Einv = get_Einv(T,len(omegas),len(omegas),omegas)
    coeffs = np.squeeze(np.asarray(np.mat(np.linalg.inv(Einv))*np.mat(hb_lift).transpose()))
    interpol = np.zeros(len(times),dtype=complex)
    for i in range(0,len(times)):
        for k in range(0,len(coeffs)):
            interpol[i] = interpol[i] + coeffs[k]*complex(np.cos(omegas[k]*times[i]),np.sin(omegas[k]*times[i]))
    return interpol
