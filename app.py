from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method== "POST":
        name=request.form["name"]
        age=request.form["Age"]
        workclass=request.form["WorkClass"]
        fnwglt=request.form["Fnwglt"]
        education=request.form["Education"]
        years=request.form["Education_years"]
        martial_status=request.form["Marital_status"]
        occupation=request.form["Occupation"]
        relationship=request.form["Relationship"]
        race=request.form["Race"]
        sex=request.form["Sex"]
        gain=request.form["Gain"]
        Loss=request.form["Loss"]
        hours=request.form["Hoursperweek"]
        nativecountry=request.form["Country"]
        work={'Federal-gov'   :0,'Local-gov':1,'Never-worked':2,'Private':3,'Self-emp-inc':4,'Self-emp-not-inc':5,'State-gov':6,'Without-pay':7 }
        educat={'10th':0,'11th':1,'12th':2, '1st-4th':3,'5th-6th': 4,'7th-8th':5,'9th':6,'Assoc-acdm': 7,'Assoc-voc' :8,'Bachelors': 9,'Doctorate':10,'HS-grad':11,'Masters':12,'Preschool':13,'Prof-school' :14,'Some-college':15}
        mstatus={
            'Married'       :0,
            'Never-Married' :1,
            'Other'         :2
        }
        job={
            'Adm-clerical'      :0,
            'Armed-Forces'      :1,
            'Craft-repair'      :2,
            'Exec-managerial'   :3,
            'Farming-fishing'   :4,
            'Handlers-cleaners' :5,
            'Machine-op-inspct' :6,
            'Other-service'     :7,
            'Priv-house-serv'   :8,
            'Prof-specialty'    :9,
            'Protective-serv'   :10,
            'Sales'             :11,
            'Tech-support'      :12,
            'Transport-moving'  :13
        }

        relation={
            'Husband'        :0,
            'Not-in-family'  :1,
            'Other-relative' :2,
            'Own-child'      :3,
            'Unmarried'      :4,
            'Wife'           :5
        }
        races={
            'Amer-Indian-Eskimo' :0,
            'Asian-Pac-Islander' :1,
            'Black'              :2,
            'Other'              :3,
            'White'              :4
        }
        gender={
            'Female':0,
            'Male'  :1
        }
        
        country ={
            'Cambodia': 0, 'Canada': 1, 'China': 2, 'Columbia': 3, 'Cuba': 4, 'Dominican-Republic': 5, 'Ecuador': 6, 'El-Salvador': 7, 'England': 8, 'France': 9, 'Germany': 10, 
            'Greece': 11, 'Guatemala': 12, 'Haiti': 13, 'Holand-Netherlands': 14, 'Honduras': 15, 'Hong': 16, 'Hungary': 17, 'India': 18, 'Iran': 19, 'Ireland': 20, 
            'Italy': 21, 'Jamaica': 22, 'Japan': 23, 'Laos': 24,'Mexico': 25,'Nicaragua': 26, 'Outlying-US(Guam-USVI-etc)': 27, 'Peru': 28, 'Philippines': 29, 'Poland': 30, 
            'Portugal': 31, 'Puerto-Rico': 32, 'Scotland': 33, 'South': 34, 'Taiwan': 35, 'Thailand': 36, 'Trinadad&Tobago': 37, 'United-States': 38, 'Vietnam': 39, 'Yugoslavia':40 
        }

        workclass=work[workclass]
        education=educat[education]
        martial_status=mstatus[martial_status]
        occupation=job[occupation]
        relationship=relation[relationship]
        race=races[race]
        sex=gender[sex]
        nativecountry=country[nativecountry]
        
        model = pickle.load(open("income_pred.pkl","rb"))
        array = [[age,workclass,fnwglt,education,years,martial_status,occupation,relationship,race,sex,gain,Loss,hours,nativecountry]]
        print(array)
        array = [np.array(array[0],dtype = 'float64')]
        print(array)
        result=model.predict(array)
        if result==[0]:
            income=name+" makes Income of Below $50K/year"
        else:
            income=name+" makes Income of Above $50K/year"
        return render_template('index.html',n=income)

if __name__=='__main__':    
    app.run(debug=True)