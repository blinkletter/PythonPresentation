import scipy.constants as spc
import numpy as np              # math tools

c = spc.c * 100          # speed of light: convert m.s^-1 to cm.s^-1
pi = spc.pi              # pi to many decimal places
N = spc.Avogadro         # Avogadro's number (mole^-1)

k = 5E5      # 5x10^5 dynes/cm -- the force constant of a C-H bond stretch
m1 = 1 / N   # mass of an individual carbon atom
m2 = 12 / N  # mass of an individual hydrogen atom

u = m1*m2 / (m1+m2)      # reduced mass
v = 1 / (2*pi*c) * np.sqrt(k/u)   # Hooke's law

print(f"The frequency is {v:0.1f} cm^-1")
