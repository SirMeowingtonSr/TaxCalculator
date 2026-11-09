# Tax Brackets: $0-$12,500 = 12%; $12,501-$42,000 = 17%; Above $42,000 = 22%
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    income_text = request.form.get("income", "")
    income = float(income_text)
    if income <= 12500:
        tax_total = income * 0.12
    elif income <= 42000:
        tax_total = (12500 * 0.12) + ((income - 12500) * 0.17)
    else:
        tax_total = (12500 * 0.12) + (29500 * 0.17) + ((income - 42000) * 0.22)

    if tax_total < 0:
        return "Error: Please go back and enter a positive number", 400
    
    return render_template('calculate.html', tax = tax_total, income = float(income_text))

if __name__ == "__main__":
    app.run(debug=True)