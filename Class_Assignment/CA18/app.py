# calcweb
import math
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)               # create a new flask application

# define basic routes

@app.route("/add", methods=["POST"])
def add():
    print("The page was requested with the method POST.")

    # read the values from the form
    n1 = int(request.form['n1'])   # read the value from the first number input
    n2 = int(request.form['n2'])  # read the value from the second number input
    return redirect(url_for("result", n1 = n1, n2 = n2, operation = 'add', answer = n1 + n2))

@app.route("/subtract", methods=['POST'])
def subtract():
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # subtract the values
    result = number1 - number2

    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2, operation = 'subtract'))
        

@app.route("/multiply", methods=['POST'])
def multiply():

    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])
    # multiply the values
    result = number1 * number2
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2, operation = 'multiply'))

@app.route("/divide", methods=['POST'])
def divide():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    if number2 == 0:
        return render_template("errors/division-by-zero.html")
    
    # divide the values
    result = number1 / number2
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2, operation = 'divide'))

@app.route("/squareroot", methods=['POST'])
def square_root():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    if number1 < 0:
        return render_template("errors/math.html")

    # square the values
    result = math.sqrt(number1)
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'square_root'))

@app.route("/cube", methods=['POST'])
def cube():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # square the values
    result = number1 ** 3
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'cube'))


@app.route("/x^y", methods=['POST'])
def x_pow_y():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # square the values
    result = number1 ** number2
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'x^y'))


@app.route("/sin", methods=['POST'])
def sin():    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = float(request.form['n2'])
    
    sin=math.sin(math.radians(number1))
    # redirect the user to the result page
    return render_template("result.html", n1 = number1, n2= number2, operation = 'sin', result=sin)

@app.route("/cos", methods=['POST'])
def cos():    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = float(request.form['n2'])

    cos=math.cos(math.radians(number1))
    # redirect the user to the result page
    return render_template("result.html", n1 = number1, n2= number2, operation = 'cos', result=cos)

@app.route("/tan", methods=['POST'])
def tan():    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = float(request.form['n2'])

    tan=math.tan(math.radians(number1)) 
    # redirect the user to the result page
    return render_template("result.html", n1 = number1, n2= number2, operation = 'tan', result=tan)



@app.route("/absolute", methods=['POST'])
def absolute():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # absolute the values
    result = abs(number1)
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'absolute'))


@app.route("/exp", methods=['POST'])
def exp():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # absolute the values
    result =math.exp(number1)
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'exp'))


@app.route("/log", methods=['POST'])
def log():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # absolute the values
    result =math.log10(number1)
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'log'))

@app.route("/ln", methods=['POST'])
def ln():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # absolute the values
    e = 2.718281
    result= math.log(e, 10)
    
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'ln'))



@app.route("/")
def index():
    buttons = [
        {"title":"+", "action":url_for('add')},
        {"title":"-", "action":url_for('subtract')},
        {"title":"*", "action":url_for('multiply')},
        {"title":"/", "action":url_for('divide')},
        {"title":"√x", "action":url_for('square_root')},
        {"title":"(x)^3", "action":url_for('cube')},
        {"title":"|x|", "action":url_for('absolute')},
        {"title":"x^y", "action":url_for('x_pow_y')},
        {"title":"e^x", "action":url_for('exp')},
        {"title":"sin(x)", "action":url_for('sin')},
        {"title":"cos(x)", "action":url_for('cos')},
        {"title":"tan(x)", "action":url_for('tan')},
        {"title":"log(x)", "action":url_for('log')},
        {"title":"Ln(x)", "action":url_for('ln')},
        {"title":"π", "action":url_for('sin')}        
    ]

        # {"title":"Absolute", "action":url_for('absolute')},
    return render_template("index.html", buttons = buttons)

@app.route("/result/<n1>/<n2>/<operation>/<float(signed=True):answer>")
def result(n1, n2, operation, answer):
    return render_template("result.html", n1 = n1, n2= n2, operation = operation, result=answer)
