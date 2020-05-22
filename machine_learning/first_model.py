import pandas as pd
from sklearn.ensemble import RandomForestRegressor
#from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
house_rent_file_path = r'C:\machine_learning\houseRent\housing_train.csv'
home_data = pd.read_csv(house_rent_file_path)
features = ['sqfeet', 'beds', 'baths']
X = home_data[features]
y = home_data['price']
train_X, valid_X, train_y, valid_y = train_test_split(X, y, random_state=1)
homies_model = RandomForestRegressor(n_estimators=100, random_state=1)
homies_model.fit(train_X,train_y)

preds = homies_model.predict(valid_X)
print(mean_absolute_error(preds, valid_y))
