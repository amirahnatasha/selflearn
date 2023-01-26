import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [
  [0,0],
  [0,1],
  [1,0],
  [1,1]
]

labels = [0, 1, 1, 1]

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)

point_grid = list(product(x_values, y_values))
# plt.scatter([point[0] for point in data], [point[1] for point in labels], c =labels)

# plt.show()

classifier = Perceptron(max_iter = 40)

classifier.fit(data, labels)

print(classifier.score(data, labels))

print(classifier.decision_function([[0,0], [1,1], [0.5,0.5]]))

distances = classifier.decision_function(point_grid)

abs_distance = [abs(pt) for pt in distances]

distances_matrix = np.reshape(abs_distance, (100, 100))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap)
plt.show()

