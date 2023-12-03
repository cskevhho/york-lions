from flask import Blueprint, render_template, request

loancalc = Blueprint("loancalc", __name__)

@loancalc.route('/loan-calculator/', methods=['GET', 'POST'])
def loan_calculator():
    if request.method == 'POST':
        vehicle_price = float(request.form['vehiclePrice'])
        down_payment = float(request.form['downPayment'])
        loan_interest_rate = float(request.form['loanInterestRate'])
        loan_duration = int(request.form['loanDuration'])

        remaining_loan_amount = vehicle_price - down_payment
        monthly_interest = (loan_interest_rate / 100) / 12
        monthlypayment = remaining_loan_amount * (monthly_interest/(1-(1+monthly_interest) ** - loan_duration))
        monthlypayment = round(monthlypayment, 2)
        return render_template('loan-calculator.html', monthly_payment=monthlypayment)

    return render_template('loan-calculator.html')
