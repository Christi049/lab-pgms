"""The areas of the various continents of the world 
(in millions of square miles) are as follows:11.7 for Africa; 
10.4 for Asia; 1.9 for Europe; 9.4 for North America; 3.3 Oceania; 
6.9 South America; 7.9 Soviet Union. Draw a bar chart representing 
the given data."""

import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Soviet Union']
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]  

plt.figure(figsize=(10,6))
plt.bar(continents,areas,color="skyblue",edgecolor="black")

plt.title('Areas of continents')
plt.xlabel('Continents')
plt.ylabel('Areas')

plt.show()