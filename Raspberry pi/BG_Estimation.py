import pickle
import numpy as np
import requests
import json

from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle
import pandas
def get_HeatRadiation(T0 ,Ts): #hr   #Ts surroinding temp
    eta=0.98  #emissivty of human skin
    sigma=(10**(-8)) #Stefan Boltezmann constant
    return (4*5.67*sigma*eta*(T0**3)*(Ts-T0))

def get_HeatConvection(T0 ,Ts,L): #hc
    G=(9.8*69*(Ts-T0)*(L**3))/(0.15*(10**(-4)))
    R=G*0.7
    N=0.021*(R**4)
    K=0.5
    return ((N*K*(Ts-T0))/L)

def get_BloodFlowRate(Tx0,Tx1,Tw): #bf
    return ( (4.36*0.5*np.pi*0.02*(Tw -Tx0))/(1060*4200*(Tx1 -Tx0)) )
def Estimate_BloodGlucose(id,T0 , Ts , Tx0 , Tx1):
    x = {'id':id }
    sorted_string = json.dumps(x, indent=4, sort_keys=True)
    #requesting API
    url="http://192.168.43.198/LoginRegister/get_tall.php"
    r = requests.post(url, json=x)
    L=int(int(json.loads(r.text)[0]['tall']))
    df = pandas.read_csv("blood_modified.csv")
    df['hr']=get_HeatRadiation(df['To'] ,df['Ts'])
    df['hc']=get_HeatConvection(df['To'] ,df['Ts'],df['Tall'])
    X = df[['hr', 'hc','bf']]
    y = df['BloodG']
    x_train , x_test , y_train , y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    BG_level = regr.predict([[get_HeatRadiation(T0 ,Ts),get_HeatConvection(T0 ,Ts,L) ,get_BloodFlowRate(Tx0,Tx1,Ts)]])
    return int(BG_level[0])