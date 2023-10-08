import pickle
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Example Input
# 1450: 5, 896, 1, 730, 882, 896, 1, 5, 1961, 1961
# 2889:	7, 2000, 3, 650, 996, 996, 2, 9, 1993, 1994

# Load the Linear Regression model from the file
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create window
window = tk.Tk()

# Title of the window
window.title("Real Value Assessment")

# Create input fields
tk.Label(window, text="Overall Quality (1-10)").grid(row=0)
overall_qual_entry = tk.Entry(window)
overall_qual_entry.grid(row=0, column=1)

tk.Label(window, text="Above Ground Square Footage").grid(row=1)
gr_liv_area_entry = tk.Entry(window)
gr_liv_area_entry.grid(row=1, column=1)

tk.Label(window, text="Garage Car Capacity").grid(row=2)
garage_cars_entry = tk.Entry(window)
garage_cars_entry.grid(row=2, column=1)

tk.Label(window, text="Garage Square Footage").grid(row=3)
garage_area_entry = tk.Entry(window)
garage_area_entry.grid(row=3, column=1)

tk.Label(window, text="Basement Square Footage").grid(row=4)
total_bsmt_sf_entry = tk.Entry(window)
total_bsmt_sf_entry.grid(row=4, column=1)

tk.Label(window, text="First Floor Square Footage").grid(row=5)
first_flr_sf_entry = tk.Entry(window)
first_flr_sf_entry.grid(row=5, column=1)

tk.Label(window, text="Number of Full Baths").grid(row=6)
full_bath_entry = tk.Entry(window)
full_bath_entry.grid(row=6, column=1)

tk.Label(window, text="Number of Above Ground Rooms").grid(row=7)
tot_rms_abv_grd_entry = tk.Entry(window)
tot_rms_abv_grd_entry.grid(row=7, column=1)

tk.Label(window, text="Year Built").grid(row=8)
year_built_entry = tk.Entry(window)
year_built_entry.grid(row=8, column=1)

tk.Label(window, text="Year Remodeled").grid(row=9)
year_remod_add_entry = tk.Entry(window)
year_remod_add_entry.grid(row=9, column=1)

# Create prediction function 
def predict_price():
    # Get values from inputs
    features = []
    features.append(int(overall_qual_entry.get()))
    features.append(int(gr_liv_area_entry.get()))
    features.append(int(garage_cars_entry.get()))
    features.append(int(garage_area_entry.get()))
    features.append(int(total_bsmt_sf_entry.get()))
    features.append(int(first_flr_sf_entry.get()))
    features.append(int(full_bath_entry.get()))
    features.append(int(tot_rms_abv_grd_entry.get()))
    features.append(int(year_built_entry.get()))
    features.append(int(year_remod_add_entry.get()))
    
    # Predict price using XGBoost model and inputs
    X_test = np.array(features).reshape(1, -1)
    y_pred = model.predict(X_test)
    
    # Display predicted Price
    messagebox.showinfo("Prediction Result", "The predicted house price is ${:,.2f}".format(y_pred[0]))
    window.destroy()  # Close window

# Add button to initialize prediction
predict_button = tk.Button(window, text="Predict", command=predict_price)
predict_button.grid(row=10, columnspan=2)

# Run the tkinter event loop
window.mainloop()