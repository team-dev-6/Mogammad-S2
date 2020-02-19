import matplotlib.pyplot as plt

data = {'Coke': 150, 'Fanta': 120, 'Sprite': 130, 'Pepsi': 160, 'Mountain Dew': 170,}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(15, 3), sharey=True)
axs[0].bar(names, values)

axs[1].scatter(names, values)

axs[2].plot(names, values)

fig.suptitle('categorical Plotting')

plt.show()
