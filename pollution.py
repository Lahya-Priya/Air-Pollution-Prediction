import joblib
import pandas as pd

# Load the model
model = joblib.load("my_model.h5")

# Input values for features
a = float(input("Enter the value of PM2.5: "))
b = float(input("Enter the value of PM10: "))
c = float(input("Enter the value of NO: "))
d = float(input("Enter the value of NO2: "))
e = float(input("Enter the value of NOx: "))
f = float(input("Enter the value of NH3: "))
g = float(input("Enter the value of CO: "))
h = float(input("Enter the value of SO2: "))
i = float(input("Enter the value of O3: "))
j = float(input("Enter the value of Benzene: "))
k = float(input("Enter the value of Toluene: "))
l = float(input("Enter the value of Xylene: "))
m = float(input("Enter the value of AQI: "))

# Create a dictionary with input values
d1 = {
    "PM2.5": a, "PM10": b, "NO": c, "NO2": d, "NOx": e,
    "NH3": f, "CO": g, "SO2": h, "O3": i, "Benzene": j,
    "Toluene": k, "Xylene": l, "AQI": m
}

# Create a DataFrame from the dictionary
d2 = pd.DataFrame([d1])

# Assuming d2 already has the correct column names, proceed to predict
p = model.predict(d2)

print(p)
'''p=[[35.57,0.92,18.22,17.15,0,0.92,27.64,133.36,0,0.02,0,544]]
print(model1.predict(p))'''
