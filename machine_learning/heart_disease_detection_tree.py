import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
heart_disease_dataset_path = r'C:\Users\User\Desktop\work\heart_disease\heart.csv'
heart_data = pd.read_csv(heart_disease_dataset_path)
features = ['age','sex','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
X = heart_data[features]
y = heart_data['target']
print("original value :\n",heart_data['target'].head().tolist())
#train_X, valid_X, train_y, valid_y = train_test_split(X, y, random_state=1)
heart_data = DecisionTreeRegressor(random_state=1)
heart_data.fit(X, y)
preds = heart_data.predict(X)
print("predicted values :",heart_data.predict(X.head()))
print("accuracy :",accuracy_score(preds, y))
print("mean_absolute_error :",mean_absolute_error(preds, y))
