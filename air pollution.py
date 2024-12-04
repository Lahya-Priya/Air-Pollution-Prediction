import pandas as pd
import joblib
data=pd.read_csv('Air_Pollution_Datasets.csv')
print(data)
data_cleaned=data.drop(columns=['MID', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'])
print(data_cleaned)
columns_to_fill = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx','NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene','Xylene','AQI'] 
data_cleaned[columns_to_fill] = data_cleaned[columns_to_fill].fillna(data_cleaned[columns_to_fill].mean())
print(data_cleaned.columns)
print(data_cleaned.isnull().sum())
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
features = data_cleaned[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3','CO', 'SO2', 'O3', 'Benzene', 'Toluene','Xylene','AQI']]
target = data_cleaned['AQI_Bucket']
x_train,x_test,y_train,y_test=train_test_split(features,target,test_size=0.2,random_state=42)
'''Logistic Regression'''
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
dd=classification_report(y_pred,y_test)
print(dd)
print("Model accuracy of Logistic Regression is",accuracy_score(y_test,y_pred)*100)
'''Random Forest'''
from sklearn.ensemble import RandomForestClassifier
model1=RandomForestClassifier()
model1.fit(x_train,y_train)
test_pred1=model1.predict(x_test)
aa=classification_report(test_pred1,y_test)
print(aa)
print("Model accuracy of Random forest classifier is",accuracy_score(y_test,test_pred1)*100)
'''SVM'''
from sklearn.svm import SVC
model2=SVC()
model2.fit(x_train,y_train)
pred=model2.predict(x_test)
cc=classification_report(pred,y_test)
print(cc)
print("Model accuracy of SVM is",accuracy_score(y_test,pred)*100)
'''Navie Bayes'''
from sklearn.naive_bayes import GaussianNB # Fixed the typo in module name
model3 = GaussianNB()
model3.fit(x_train, y_train)
pred1=model3.predict(x_test)
bb=classification_report(pred1,y_test)
print(bb)
print("Model accuracy of Navie Bayes is",accuracy_score(y_test,pred1)*100)
'''Linear Regression'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)
model4=LinearRegression()
model4.fit(x_train,y_train_encoded)
pr=model4.predict(x_test)
r2=r2_score(y_test_encoded, pr)
print(f"R-squared:{r2*100}")
ee=classification_report(pr,y_test)
print(ee)
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['AQI_Bucket']=encoder.fit_transform(data['AQI_Bucket'])
data.head()
joblib.dump(model1,"my_model.h5")



