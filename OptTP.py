#
# Python script to run Optimal Time Period algorithm for Harmonic Balance
# To run: python3 OptTP.py
#
# Input frequencies should be given as space-separated list
# Exclude the zero frequency and the negative frequencies
#

import numpy as np
import cmath

from numpy import linalg as LA

#  Function to get condition number
def get_Einv(T,N,omegas):
    Einv = np.zeros((N,N),dtype=complex)
    for n in range(0,N):
        for k in range(0,N):
            Einv[n,k] = complex(np.cos(omegas[k]*n*T/N),np.sin(omegas[k]*n*T/N))

    return LA.cond(Einv)

def main():
    #  These are the HB input frequencies
    # f_omegas = [62.831853072, 70.84]
    
    print("Enter frequencies separated by space (exclude zero and negative): ")
    print("Example: 888 999")
    f_omegas = [float(x) for x in input("> ").split()]
    
    #  Time instance, N = 2K+1
    N = 2*len(f_omegas)+1

    #  Build omega set for N = 2K+1 harmonics
    omegas = np.zeros(N)
    for i in range(1,N):
        if i > len(f_omegas):
            omegas[i] = -np.flip(f_omegas)[i-len(f_omegas)-1]
        else:
            omegas[i] = f_omegas[i-1]

    print("\nOMEGA_HB:")
    print(omegas)
    print("\n")

    #  t_n = (n-1)*T/N
    t_n = 2*np.pi*np.reciprocal(omegas,where=omegas!=0)
    T = abs(min(t_n))
    
    ## OptTP algorithm
    globalmin = 1e+6;

    for k in range(len(f_omegas)):
        T0 = 2*np.pi/f_omegas[k]
        Ti = 5*T0
        Tf = Ti
        Tstep = 0.01*T0

        imin = 1
        cmin = get_Einv(T0,N,omegas)
        print(f'Current frequency: {f_omegas[k]}')
        print(f'Current time period: {T0}')
        print(f'Condition number: {cmin}')
    
        while cmin > 1:
            print(f'Running OptTP between {T0} and {Tf}...')
            Trange = np.arange(T0,Tf+Tstep,Tstep)
            for i in range(1,len(Trange)):
                c = get_Einv(Trange[i],N,omegas)
                if c <= cmin:
                    cmin = c
                    imin = i
            if cmin > 4:
                T0 = Tf
                Tf = Tf+Ti
            else:
                break

        try:
            print(f'Optimal time period: {Trange[imin]}')
        except NameError:
            print(f'Optimal time period: {T0}')
        print(f'Condition number: {cmin}\n')
    
        if cmin < globalmin:
            globalmin = cmin

    globalfreq = 2*np.pi/globalmin
    print(f'Global minimum OptTP is {globalmin} s with corresponding frequency {globalfreq} rad/s')
    
if __name__ == "__main__":
    main()
