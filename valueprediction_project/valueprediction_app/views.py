from django.shortcuts import render
from django.http import HttpResponse
from valueprediction_app.forms import HouseDataForm
import pickle
import numpy as np
import os

# Get the absolute path to the xgboost model
model_path = os.path.abspath(r'C:\Users\nicho\FullStackCOP5818\COP5818_FullStack_Project\xgboost_model.pkl')

# Load the XGBoost model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_price(request):
    if request.method == 'POST':
        form = HouseDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = [data['overall_quality'], data['gr_liv_area'], data['garage_cars'], data['garage_area'], data['total_bsmt_sf'], data['first_flr_sf'], data['full_bath'], data['tot_rms_abv_grd'], data['year_built'], data['year_remod_add']]
            X_test = np.array(features).reshape(1, -1)
            y_pred = model.predict(X_test)
            return render(request, 'result.html', {'predicted_price': y_pred[0]})
    else:
        form = HouseDataForm()
    return render(request, 'predict.html', {'form': form})