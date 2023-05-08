# -*- coding: utf-8 -*-


from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

pickle_in=open('StackModel.pkl','rb')
p_model=open('model.pkl','rb')
p_model2=open('model2.pkl','rb')
p_model3=open('model3.pkl','rb')
p_model4=open('model4.pkl','rb')
stack_model=pickle.load(pickle_in)
model=pickle.load(p_model)
model2=pickle.load(p_model2)
model3=pickle.load(p_model3)
model4=pickle.load(p_model4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [ x for x in request.form.values()]
    Gender=features[5]
    Married=features[6]
    Dependents=features[7]
    Education=features[8]
    SelfEmployed=features[9]
    PropertyArea=features[10]
    CreditHistory=features[4]
    ApplicantIncome=float(features[0])/10.0
    CoapplicantIncome=float(features[1])/10.0
    LoanAmount=float(features[3])/1000.0
    Loan_Amount_Term=int(features[2])*30
    
    
    p1=int(model.predict([[Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,CreditHistory,PropertyArea]]))
    p2=int(model2.predict([[Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,CreditHistory,PropertyArea]]))
    p3=int(model3.predict([[Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,CreditHistory,PropertyArea]]))
    p4=int(model4.predict([[Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,CreditHistory,PropertyArea]]))
    
    prediction=stack_model.predict([[p1,p2,p3,p4]])
    
    
    return render_template('index.html', prediction_text=prediction,ai=features[0],ci=features[1],la=features[3],lt=features[2],ch=int(features[4]),gd=int(features[5]),mr=int(features[6]),dp=int(features[7]),ed=int(features[8]),se=int(features[9]),pa=int(features[10]))

if __name__ == "__main__":
    app.run(debug=True)