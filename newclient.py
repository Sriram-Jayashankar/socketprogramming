from sklearn.datasets import fetch_openml
mnist=fetch_openml('mnist_784')
print(type(mnist))
X,y=mnist["data"],mnist["target"]