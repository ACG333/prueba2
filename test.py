# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo cruel")

dat=np.loadtxt('data.txt', delimiter=',')
x=dat[:,0]
y=dat[:,1]


plt.plot(x,y)
plt.savefig('plot.png')
