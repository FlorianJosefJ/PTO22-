import numpy as np
import matplotlib.pyplot as plt
import math


genauigkeit = float(input("Bitte geben Sie die Genauigkeit in Grad ein: "))


x = np.arange(0, 360, genauigkeit)


x_rad = np.deg2rad(x)


y = np.sin(x_rad)


plt.plot(x, y)
plt.title('Sinusfunktion')
plt.xlabel('Grad')
plt.ylabel('Sinus')
plt.grid(True)


plt.xticks(np.arange(0, 360, genauigkeit))


plt.show()