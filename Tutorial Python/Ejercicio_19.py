# Exercise 19: Following a poll a few days before an election, the following voting intention has been recorded, 
# where the names of the political parties have been camouflaged so as not to influence your personal opinion:

# parties = ['Part A', 'Part B', 'Part C', 'Part D', 'Part E', 'Part F']

# intention_vote = [21.5, 17.8, 31.8, 10.3, 5.7, 12.9]

# Create a bar chart
# Creates a pie chart.



import matplotlib.pyplot as plt

"""Bar chart"""
fig, ax = plt.subplots()
ax.bar(['Part A', 'Part B', 'Part C', 'Part D', 'Part E', 'Part F'], [21.5, 17.8, 31.8, 10.3, 5.7, 12.9])
plt.show()

"""Pie chart"""
fig, ax = plt.subplots()
ax.pie([21.5, 17.8, 31.8, 10.3, 5.7, 12.9], labels=['Part A', 'Part B', 'Part C', 'Part D', 'Part E', 'Part F'], autopct='%1.1f%%')
plt.show()




