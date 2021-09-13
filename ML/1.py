from sklearn import datasets
import matplotlib.pyplot as plt

# iris_dataset = datasets.load_iris()
# print(iris_dataset['data'][:4])

arabic_dataset = datasets.load_digits()
# print(arabic_dataset.keys())
print(arabic_dataset.images[0])
plt.imshow(arabic_dataset.images[0],cmap=plt.get_cmap('gray'))
plt.show()
