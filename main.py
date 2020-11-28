import matplotlib.pyplot as plt
import numpy as np

xvalues = np.linspace( -np.pi, np.pi, 500 )

yvalues = np.zeros(500)
for i in range(500) : yvalues[i] = np.sin( xvalues[i] )

plt.plot( xvalues, yvalues, "k-" )
plt.savefig( "sine.png" )
