from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle sauvegardé
model_filename = 'best_logistic_model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    # Extraire les données reçues dans la requête
    data = request.json
    input_features = np.array(data['features']).reshape(1, -1)
    
    # Calculer la probabilité
    probability = model.predict_proba(input_features)[:, 1][0]
    
    # Déterminer la classe en fonction du seuil de 0.5
    prediction = int(probability >= 0.5)
    
    # Retourner la réponse JSON
    return jsonify({
        'probability': probability,
        'prediction': 'Accepted' if prediction == 1 else 'Rejected'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
