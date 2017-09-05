# Projeto 1 FIS MOV

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
import math 


#Equações Diferenciais
def Equacao(s,t):
	om = s[0]
	w = s[1]
	domdt = w
	dwdt = (-ag*(math.sin(om)))/lado
	return [domdt,dwdt]

#Constantes Fixas
ag = 9.8 # Aceleração da Gravidade, em metros por segundo ao quadrado
lado = 30

t = np.arange(0,10,0.01) # Lista Tempo

SO = [45,0] #Condições Iniciais

solucao = odeint(Equacao,SO,t) # ODEINT

X = []
Y = []

for i in solucao[:,0]:
    
    x = 2*math.sin(i)
    y = 2 - 2*math.cos(i)
   # x1 = x*180/math.pi
   # y1 = *180/math.pi
    
    X.append(x)
    Y.append(y)
    
plt.plot(X,Y)
plt.title("Pêndulo")
plt.grid(True)
plt.axis((-2,2,0,4))
plt.show()

# Gráficos

plt.plot(t,solucao[:,0],'g')
plt.title("Ângulo pelo tempo")
plt.ylabel('Ângulo')
plt.xlabel("Tempo em segundos")
plt.grid(True)
plt.show()

plt.plot(t,solucao[:,1],'r')
plt.title("Velocidade Angular pelo tempo")
plt.ylabel('Velocidade Angular')
plt.xlabel("Tempo em segundos")
plt.grid(True)
plt.show()


