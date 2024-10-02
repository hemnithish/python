from flask import Flask, render_template, request

app = Flask(__name__)

# Home route to display the calculator form
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Route to handle the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get data from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return render_template('calculator.html', result="Error: Division by zero!")
            result = num1 / num2
        else:
            result = "Invalid Operation"
        
        return render_template('calculator.html', result=result)
    
    except ValueError:
        return render_template('calculator.html', result="Error: Invalid input. Please enter numbers.")

if __name__ == '__main__':
    app.run(debug=True)
