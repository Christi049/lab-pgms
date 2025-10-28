"Measure your classmate’s height and draw the histogram"

import matplotlib.pyplot as plt

heights_input = input("Enter the heights seperated by spaces: ")

heights = list(map(float,heights_input.split()))

plt.hist(heights, edgecolor="black", bins=5)
plt.title('Distribution of classmate heights')
plt.xlabel("Height")
plt.ylabel('No of students')
plt.show()
