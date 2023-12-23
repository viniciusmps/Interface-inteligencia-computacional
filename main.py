from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
modelo = pickle.load(open('modelo.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
       
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bloodpressure = float(request.form['bloodpressure'])
        skinthickness = float(request.form['skinthickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetespedigreefunction = float(request.form['diabetespedigreefunction'])
        age = float(request.form['age'])

        # Correção aqui: usar modelo.predict, não modelo_logistico.predict
        prediction = modelo.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])

        # Mapear 1 para "Tem Diabetes" e 0 para "Não Tem Diabetes"
        result_text = "Tem Diabetes" if prediction[0] == 1 else "Não Tem Diabetes"

        return render_template('resultado.html', prediction=result_text)

if __name__ == '__main__':
    app.run(debug=True)
