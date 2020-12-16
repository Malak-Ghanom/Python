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



@app.route("/angle", methods=['POST'])
def angle_sct():
    
    # read and cast the values from the form
    number1 = float(request.form['n1'])
    number2 = float(request.form['n2'])
    radiant = math.radians(number1)

    # square the values
    sin = math.sin(radiant)
    # cos = math.cos(number1)
    # tan = math.tan(number1)
    
    result = sin
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'angle'))

@app.route("/absolute", methods=['POST'])
def absolute():
    
    # read and cast the values from the form
    number1 = int(request.form['n1'])
    number2 = int(request.form['n2'])

    # absolute the values
    result = abs(number1)
    # redirect the user to the result page
    return redirect(url_for("result", answer = result,n1=number1,n2=number2 , operation = 'absolute'))


@app.route("/")
def index():
    buttons = [
        {"title":"Add", "action":url_for('add')},
        {"title":"Subtract", "action":url_for('subtract')},
        {"title":"Multiply", "action":url_for('multiply')},
        {"title":"Divide two numbers", "action":url_for('divide')},
        {"title":"Square Root", "action":url_for('square_root')},
        {"title":"Cube", "action":url_for('cube')},
        {",title":"Angle", "action":url_for('angle_sct')},
        {"title":"Absolute", "action":url_for('absolute')}
    ]

        # {"title":"Absolute", "action":url_for('absolute')},
    return render_template("index.html", buttons = buttons)

@app.route("/result/<n1>/<n2>/<operation>/<int:answer>")
def result(n1, n2, operation, answer):
    return render_template("result.html", n1 = n1, n2= n2, operation = operation, result=answer)
