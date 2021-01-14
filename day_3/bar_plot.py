import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('default') # other options are 'classic', 'ggplot', 'default'

plt.bar([2 * x + 1 for x in range(5)], [5, 2, 7, 8, 2], label='Example 1')
plt.bar([2 * x for x in range(1, 6)], [8, 6, 2, 5, 6], label='Example 2')

plt.legend()
plt.xlabel('X-Axis')
plt.ylabel('Quantity')
plt.title('My First Bar Graph')
plt.grid(False)

plt.show()
