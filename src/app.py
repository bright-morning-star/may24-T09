from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    
        form_input = dict(request.form)
        print(form_input)

        #numerical features
        tenure_months = int(form_input['tenure_months'])
        num_referrals = int(form_input['num_referrals'])
        total_long_distance_fee = float(form_input['total_long_distance_fee'])
        total_monthly_fee = float(form_input['total_monthly_fee'])
        total_charges_quarter = float(form_input['total_charges_quarter'])
        age = int(form_input['age'])
        num_dependents = int(form_input['num_dependents'])

        #categorical features
        has_internet_service = int(form_input['has_internet_service'])
        has_unlimited_data = int(form_input['has_unlimited_data'])
        has_premium_tech_support = int(form_input['has_premium_tech_support'])
        has_online_security = int(form_input['has_online_security'])
        paperless_billing = int(form_input['paperless_billing'])
        senior_citizen = int(form_input['senior_citizen'])
        married = int(form_input['married'])
        contract_type = int(form_input['contract_type'])
        payment_method = int(form_input['payment_method'])
        
        #model_inputs = [2,0,22.14,83.9,267.4,85,0,0,0,0,0,0,0,0,0,0] #For Testing Purpose

        model_inputs = [tenure_months, num_referrals, total_long_distance_fee, total_monthly_fee, 
                        total_charges_quarter, age, num_dependents,has_internet_service, 
                        has_unlimited_data, has_premium_tech_support, has_online_security, 
                        paperless_billing, senior_citizen, married, contract_type, 
                        payment_method]

        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')



# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()

    #numerical features
    tenure_months = int(request_data['tenure_months'])
    num_referrals = int(request_data['num_referrals'])
    total_long_distance_fee = float(request_data['total_long_distance_fee'])
    total_monthly_fee = float(request_data['total_monthly_fee'])
    total_charges_quarter = float(request_data['total_charges_quarter'])
    age = int(request_data['age'])
    num_dependents = int(request_data['num_dependents'])

    #categorical features
    has_internet_service = int(request_data['has_internet_service'])
    has_unlimited_data = int(request_data['has_unlimited_data'])
    has_premium_tech_support = int(request_data['has_premium_tech_support'])
    has_online_security = int(request_data['has_online_security'])
    paperless_billing = int(request_data['paperless_billing'])
    senior_citizen = int(request_data['senior_citizen'])
    married = int(request_data['married'])
    contract_type = int(request_data['contract_type'])
    payment_method = int(request_data['payment_method'])

    model_inputs = [tenure_months, num_referrals, total_long_distance_fee, total_monthly_fee, 
                    total_charges_quarter, age, num_dependents,has_internet_service, 
                    has_unlimited_data, has_premium_tech_support, has_online_security, 
                    paperless_billing, senior_citizen, married, contract_type, 
                    payment_method]
    
    prediction = Model().predict(model_inputs)
    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(debug=True)