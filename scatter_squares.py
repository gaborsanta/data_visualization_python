import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values =  [x**2 for x in x_values]
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# custom colors by passing 0-1 to tuple. Values closer to 0
# produce dark colors.
#plt.scatter(x_values, y_values, c=(0.5, 0.5, 0.8), edgecolor='none', s=40)

# Using Colormap http://matplotlib.org/; go to Examples,
#scroll down to Color Examples, and click colormaps_reference.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()