from math import log
from flask import Flask,render_template,request,jsonify

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operations():
    if (request.method == 'POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if ops=="add":
            r=num1+num2
            res= "The sum of "+str(num1)+" and "+str(num2)+ " is "+str(r)
            return render_template('results.html',result=res)
        
        elif ops=="subtract":
            r=num1-num2
            res= "The difference of "+str(num1)+" and "+str(num2)+ " is "+str(r)
            return render_template('results.html',result=res)
        
        elif ops=="multiply":
            r=num1*num2
            res= "The product of "+str(num1)+" and "+str(num2)+ " is "+str(r)
            return render_template('results.html',result=res)
        
        elif ops=="divide":
            r=num1/num2
            res= "The quotient of "+str(num1)+" and "+str(num2)+ " is "+str(r)
            return render_template('results.html',result=res)
        
        elif ops=="log":
            r=log(num1,num2)
            res= "The log of "+str(num1)+" to base "+str(num2)+ " is "+str(r)
            return render_template('results.html',result=res)

if __name__ == '__main__':
    app.run(host="0.0.0.0")