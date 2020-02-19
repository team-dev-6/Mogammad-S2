#Bar graph for Sprint 6.

from matplotlib import pyplot as plt 
from matplotlib import style 

style.use('ggplot')

x = ['Simba','Lays','Doritos']
y = [15,13,13]

plt.bar(x, y, align='center')

plt.title('Chips')
plt.ylabel('Price list of Chips in Rands')
plt.xlabel('Types of chips')

plt.show()