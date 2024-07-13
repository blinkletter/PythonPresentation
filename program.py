import scipy.constants as spc   # predefined constant library
import numpy as np              # math tools

k = 5E5  # 5x10^5 dynes/cm -- the force constant of a C-H bond stretch
m1 = 12 / spc.Avogadro   # mass of an individual carbon atom
m2 = 1 / spc.Avogadro    # mass of an individual hydrogen atom

c = spc.c * 100          # convert m.s-1 to cm.s-1
pi = spc.pi              # 

u = m1*m2 / (m1+m2)      # reduced mass
v = 1 / (2*pi*c) * np.sqrt(k/u)   # Hooke's law

print(f"The frequency is {v:0.1f} cm^-1")


