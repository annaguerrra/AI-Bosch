from sklearn.linear_model import ElasticNet

x = [ [4, 8], [3, 6], [10, 2]]
y = [20, 16, 26]

model = ElasticNet()
model.fit( x, y)

print(model.predict([20,10]))