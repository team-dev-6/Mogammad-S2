import pandas as pd 
from matplotlib import pyplot as plt 

#plt.style.use('prices')

prices = [4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]

plt.hist(prices, bins=3, edgecolor='black')


plt.title('Prices of Veggies')

plt.xlabel('Brocolli                Spinach                     Cabbage')
plt.ylabel('Price')
plt.show()
