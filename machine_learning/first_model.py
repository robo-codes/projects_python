import pandas as pd
from sklearn.tree import DecisionTreeRegressor
house_rent_file_path = r'C:\machine_learning\houseRent\housing_train.csv'
home_data = pd.read_csv(house_rent_file_path)
features = ['sqfeet', 'beds', 'baths']
X = home_data[features]
y = home_data['price']

homies_model = DecisionTreeRegressor(random_state=1)
homies_model.fit(X,y)

preds = homies_model.predict(X)
print(homies_model.predict(X.head()))
print(y.head().tolist())
