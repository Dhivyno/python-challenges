import numpy as np
import matplotlib.pyplot as plot

time = np.arange(1, 10, 0.1);

amplitude = np.log(time**time)
amplitude2 = np.power(time, 2)
amplitude3 = np.power(time, 1)
amplitude4 = np.power(time, 0)
amplitude5 = np.log(time)

plot.plot(time, amplitude)
plot.plot(time, amplitude3)
plot.plot(time, amplitude4)
plot.plot(time, amplitude5)

plot.title('Big O graphs')

plot.xlabel('Inputs')

plot.ylabel('Steps')

plot.grid(True)

plot.show()