import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3]

# heights of bars
height = [10, 24, 36]

# labels for bars
tick_label = ['Naive Bayes', "Feature Selection", 'Weighted Features']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()