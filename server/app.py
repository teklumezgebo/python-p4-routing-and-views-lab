#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(f'{string}')
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    numbers = ''
    for i in range(integer):
        if numbers == '':
            numbers = f'{i}'
        else:
            numbers = f'{numbers}\n{i}'
        i += 1
    return numbers + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, num2, operation):
    num1 =  int(num1)
    num2 = int(num2)
    
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)