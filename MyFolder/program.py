import scipy.constants as spc
import numpy as np 

c = spc.c * 100  
pi = spc.pi           
N = spc.Avogadro   

k = 5E5     
m1 = 1 / N   
m2 = 12 / N 

u = m1*m2 / (m1+m2)     
v = 1 / (2*pi*c) * np.sqrt(k/u) 

print(f"The frequency is {v:0.1f} cm^-1")
