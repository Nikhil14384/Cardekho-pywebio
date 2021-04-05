from flask import Flask, render_template, request,send_from_directory
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
#import jsonify
#import requests
import pickle
import numpy as np
import sklearn
#from sklearn.preprocessing import StandardScaler
from pywebio.input import *
from pywebio.output import *
import datetime
# =============================================================================
# app = Flask(__name__)
# model = pickle.load(open('cardekho_pred.pkl', 'rb'))
# @app.route('/',methods=['GET'])
# def Home():
#     return render_template('index.html')
# 
# 
# standard_to = StandardScaler()
# @app.route("/predict", methods=['POST'])
# def predict():
#     Fuel_Type_Diesel=0
#     if request.method == 'POST':
#         Year = int(request.form['Year'])
#         Present_Price=float(request.form['Present_Price'])
#         Kms_Driven=int(request.form['Kms_Driven'])
#         Kms_Driven2=np.log(Kms_Driven)
#         Owner=int(request.form['Owner'])
#         Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
#         if(Fuel_Type_Petrol=='Petrol'):
#                 Fuel_Type_Petrol=1
#                 Fuel_Type_Diesel=0
#         else:
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=1
#         Year=2020-Year
#         Seller_Type_Individual=request.form['Seller_Type_Individual']
#         if(Seller_Type_Individual=='Individual'):
#             Seller_Type_Individual=1
#         else:
#             Seller_Type_Individual=0	
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
#         prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
#         output=round(prediction[0],2)
#         if output<0:
#             return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
#         else:
#             return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
#     else:
#         return render_template('index.html')
# =============================================================================
model = pickle.load(open('cardekho_pred.pkl', 'rb'))
app1 = Flask(__name__)
#standard_to = StandardScaler()
def hitman():
    Year=int(input("Enter the car year of purchse",type='number'))
    Year=datetime.date.today().year-Year
    current_price=input("Enter the current ex-showroom price of car",type='float')
    km_driven=input("Enter the KM that vehicle driven so far",type='number')
    km_driven2=np.log(km_driven)
    owner=input("Enter the number of owners changed",type='number')
    fuel_type= select('Select the fuel type',['petrol','diesel','CNG'])
    if(fuel_type=='petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    seller_type=select("select the seller type",['Dealer','Individual'])
    if(seller_type=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0

    transmission_type=select("Select the engine type",['Mannual car','Automatic car'])   
    if(transmission_type=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
    prediction=model.predict([[current_price,km_driven2,owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output <= 0:
        put_text("Oops...! you cannot sell your car")
    else:
        put_text('The resale value of your car is : %.1f lakhs ' %(output))
    app1.add_url_rule('/hitman', 'webio_view', webio_view(hitman),
            methods=['GET', 'POST', 'OPTIONS'])
    
    

if __name__=="__main__":
    #app.run(debug=True)
    app1.run(debug=True)



