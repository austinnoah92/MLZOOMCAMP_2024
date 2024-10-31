#Serving the model
import pickle
from flask import Flask, request, jsonify

app = Flask('subscription')

# Load the DictVectorizer and LogisticRegression model
with open('/workspaces/MLZOOMCAMP_2024/dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

with open('/workspaces/MLZOOMCAMP_2024/model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)


#Add decorator so other functionality can be called
@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    X_client = dv.transform([client])
    probability = model.predict_proba(X_client)[0, 1]
    return jsonify({'subscription_probability': probability})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
