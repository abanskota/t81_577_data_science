import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, request
import flask

with open('./model/model.pkl', 'rb') as model_pkl:
    rf = pickle.load(model_pkl)

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
    
        CRIM = request.args.form('CRIM')
        ZN = request.args.form('ZN')
        INDUS = request.args.form('INDUS')
        CHAS = request.args.form('CHAS')
        NOX = request.args.form('NOX')
        RM = request.args.form('RM')
        AGE = request.args.form('AGE')
        DIS = request.args.form('DIS')
        RAD = request.args.form('RAD')
        TAX = request.args.form('TAX')
        PTRATIO = request.args.form('PTRATIO')
        B = request.args.form('B')
        LSTAT = request.args.form('LSTAT')

        unseen = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
        result = rf.predict(unseen)

        return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)


if __name__ == '__main__':
    app.run()