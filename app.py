from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def Home():
    return render_template("HPP.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()] 
    final=[np.array(int_features)]  
    prediction = model.predict(final)
    print(int_features)
    print(prediction[0])

    return render_template("HPP.html", prediction_text = prediction, attack_text=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)



