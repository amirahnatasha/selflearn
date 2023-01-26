import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()

model = KMeans(n_clusters = 10, random_state = 50)

model.fit(digits.data)

# print(digits.DESCR)
# print(digits.data)
# print(digits.target)

# Figure size (width, height)
 
fig = plt.figure(figsize=(6, 6))
 
# # Adjust the subplots 
 
# fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
 
# # For each of the 64 images
 
# for i in range(64):
 
#     # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
 
#     ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
 
#     # Display an image at the i-th position
 
#     ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
 
#     # Label the image with the target value
 
#     ax.text(0, 7, str(digits.target[i]))
 
# plt.show()

fig = plt.figure(figsize=(8,3))

fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):

  ax = fig.add_subplot(2, 5, 1 + i)

  ax.imshow(model.cluster_centers_[i].reshape((8,8)), cmap=plt.cm.binary)


# plt.gray()
# plt.matshow(digits.images[100])
plt.show()

new_samples = np.array([
[0.00,0.00,0.00,0.38,0.68,0.00,0.00,0.00,0.00,0.00,3.43,7.55,7.62,6.48,2.36,0.00,0.00,2.52,7.55,5.34,3.20,6.63,7.48,0.00,0.00,5.34,5.95,0.23,0.46,5.19,7.55,0.00,0.00,0.31,0.23,2.36,6.94,7.62,3.96,0.00,0.00,0.00,4.42,7.63,7.62,5.80,5.11,2.06,0.00,0.00,5.95,6.86,6.86,6.86,6.33,2.06,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.60,4.96,6.10,5.57,1.14,0.00,0.00,0.00,7.02,6.94,5.11,7.17,6.48,0.15,0.00,0.00,7.63,3.89,0.00,2.44,7.62,2.36,0.00,0.00,6.71,5.57,0.00,0.38,7.62,3.81,0.00,0.00,3.51,7.62,5.80,6.79,7.62,2.90,0.00,0.00,0.00,3.58,6.63,6.79,2.67,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.13,6.79,6.10,6.10,5.57,1.07,0.00,0.00,2.90,7.62,5.34,4.73,5.26,1.07,0.00,0.00,1.22,7.62,6.48,5.95,1.68,0.00,0.00,0.00,0.08,4.88,5.34,6.79,6.25,0.00,0.00,0.00,0.00,0.00,0.84,5.04,7.62,0.00,0.00,0.00,0.08,5.57,7.63,7.62,6.33,0.00,0.00,0.00,0.08,4.88,3.58,1.68,0.15,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.22,4.27,4.57,4.04,0.76,0.00,0.00,0.84,7.40,7.32,6.18,7.55,6.56,0.46,0.00,1.53,7.62,2.67,0.00,2.37,7.62,3.82,0.00,0.23,7.17,5.49,0.00,0.08,7.09,4.57,0.00,0.00,3.51,7.63,5.41,5.87,7.62,3.51,0.00,0.00,0.23,4.12,6.10,6.10,3.58,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')