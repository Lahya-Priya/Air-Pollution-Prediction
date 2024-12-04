from flask import Flask, render_template, request, redirect, url_for
import os
import sys
import pandas as pd # type: ignore
import joblib 

app = Flask(__name__)
if sys.stderr is None:
    sys.stderr=open(os.devnull,'w')
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
       model=joblib.load("my_model.h5")
       a=float(request.form['PM2.5'])
       b=float(request.form['PM10'])
       c=float(request.form['NO'])
       d=float(request.form['NO2'])
       e=float(request.form['NOx'])
       f1=float(request.form['NH3'])
       g=float(request.form['CO'])
       h=float(request.form['SO2'])
       i=float(request.form['O3'])
       j=float(request.form['Benzene'])
       k=float(request.form['Toluene'])
       l=float(request.form['Xylene'])
       m=int(request.form['AQI'])
       d1 = {'PM2.5': a, 'PM10': b, 'NO': c, 'NO2': d, 'NOx': e,'NH3': f1, 'CO': g, 'SO2': h, 'O3': i, 'Benzene': j,'Toluene': k, 'Xylene': l, 'AQI': m}
       # Create a DataFrame from the dictionary
       d2 = pd.DataFrame([d1])
       # Assuming d2 already has the correct column names, proceed to predict
       result = model.predict(d2)
    except ValueError:
        result = "Invalid input! Please enter numbers only."
    
    return redirect(url_for('result', result=result))

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,port=8080)

