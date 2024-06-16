import joblib


class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)


combination_factors = {

    "has_internet_service": "Yes" , 
    "has_unlimited_data": "Yes" , 
    "has_premium_tech_support": "Yes", 
    "has_online_security" : "Yes", 
     "paperless_billing": "No", 
     "senior_citizen": "Yes", 
     "married": "Yes", 
     "contract_type": 1, 
     "payment_method": 1
}
model_inputs = list(combination_factors.values())

print(model_inputs)                  
print(Model().predict(model_inputs)) 