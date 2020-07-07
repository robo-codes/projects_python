import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
covid_19_db_path = r'C:\Users\User\Desktop\work\covid19\covid_19_india.csv'
covid_19_db = pd.read_csv(covid_19_db_path)
#print(covid_19_db.head())
features = ['Deaths','Confirmed']

X = covid_19_db[features]
y = covid_19_db['Cured']
train_X, train_y, valid_X, valid_y = train_test_split(X, y, random_state = 1)
covid_19_db = RandomForestRegressor(random_state = 1)
covid_19_db.fit(train_X, train_y)
preds = covid_19_db.predict(valid_X)
print(mean_squared_error(valid_y, preds))
