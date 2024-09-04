from sklearn.linear_model import LogisticRegression

X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [20,23], [14,90], [90,81]]
y = [0, 0, 1, 1, 1, 0, 0, 1]

model = LogisticRegression()
model.fit(X,y)

prediction = model.predict([[0,11]])[0]
print(prediction)