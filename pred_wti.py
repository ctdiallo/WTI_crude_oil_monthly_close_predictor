# Import Libraries
import streamlit as st
import keras
from PIL import Image
import numpy as np
import pickle

# # save the model
# do this in the ipynb under the classifier code
# with open("NAME OF MODEL.pkl", 'wb') as file:
#     pickle.dump(model, file)

# then do this here
#then remove loaded_
# then remove the ANN
# # load the model from the file
# with open("NAME OF model.pkl", 'rb') as file:
#     loaded_model = pickle.load(file)

# # save the model
# with open("svm.pkl", 'wb') as file:
#     pickle.dump(svm_linear, file)

    # load the model from the file
# with open("svm.pkl", 'rb') as file:
#     loaded_model = pickle.load(file)

# load the model
model = keras.models.load_model("wti_prediction.h5") ## i green this if i'm using another model

# create a function for prediction
def wti_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1, -1)
    prediction = model.predict(input_reshape)
    print(prediction)

    if(prediction[0] < 0.5 ):
        return "The price of WTI Crude Oil is likely to fall this month"
    else:
        return "The price of WTI Crude Oil is likely to rise this month"
    
# now let's setup how the page will look (page config)
def main():
    st.set_page_config(page_title = "WTI Crude Oil (CL) Monthly Close Predictor", layout = "wide")

   # add image
    image = Image.open("wti_crude.png")
    st.image(image, use_column_width = False)

    # set title content
    st.title("WTI Crude Monthly Close Predictor using Machine Learning")
    st.write("Enter your expectations to get next month Direction of WTI Crude Oil")

    # get input from user
    opec = st.number_input("OPEC Oil output (mbpd):", min_value=10.0, value=10.0, step=0.1)
    russia = st.number_input("Russia Oil output for the month (mbpd):", min_value=3.0, value=3.0, step=0.1)
    us_prod = st.number_input("US Oil output for the month (mbpd):", min_value=1.0, value=1.0, step=0.1)

    china = st.number_input("Daily China demand for Crude Oil (mbpd):", min_value=7.0, step=0.5)
    india = st.number_input("Daily India demand for Crude Oil (mbpd):", min_value=7.0, step=0.5)
    oecd_cons = st.number_input("Daily OECD demand for Crude Oil and fuels (mbpd):", min_value=10.0, step=0.5)
    us_oil_cons = st.number_input("Daily US demand for Crude Oil (mbpd):", min_value=5.0, step=0.5)
    
    days_of_supply = st.number_input("What is the duration of Inventory coverage in the United States? (days):", min_value=15.0, value=15.0, step=1.0)
    oecd_inv = st.number_input("Your estimates of OECD Countries Crude Oil stockpiles ex-USA (days):", min_value=100.0, step=10.0)
    us_inventories = st.number_input("Your estimate of Crude Oil stockpiles. Lately between 250 and 400 (in '000s):", min_value=100.0, step=10.0)
    rig_count = st.number_input("Total number of active oil drilling rigs in operation in the USA (onshore + offshore) ~ 500:", min_value=400.0, step=5.0)
    
    baltic = st.number_input("Measures freight rates for Oil and Oil products tankers across 34 routes:", min_value=100.0, step=25.0)
    copper = st.number_input("Copper, a crucial indicator for the Chinese economy:", min_value=1.00, step=0.05)
    eurusd = st.number_input("Estimate of EURUSD exchange rate:", min_value=0.80, step=0.0001)
    cot_ave = st.number_input("CFTC Commitment of Traders Net Oil futures Positions in '000s:", min_value=-700.0, value=-300.0, step=5.0)
    timespread = st.number_input("Difference between M4 and Spot WTI Crude in the Fwd curve. An estimator of contango or backwardation:", min_value=-50.0, step=0.5)
    
    gpr_index = st.number_input("Measures the occurrence of impactful geopolitical events/threats/conflicts:", min_value=20.0, step=5.0)
    us_yield_curve = st.number_input("US 10yr minus US 2yr yield at Constant maturity (%):", min_value=-5.00, step=0.25)
    us_cons_conf = st.number_input("A gauge of consumer sentiment:", min_value=20.0, step=5.0)

        ## code for prediction
    predict = ''

    # button for prediction
    if st.button('Predict'):
        predict = wti_prediction([opec, russia,us_prod, cot_ave,days_of_supply,us_inventories,oecd_inv,
                        timespread,rig_count,gpr_index,baltic, us_oil_cons,	oecd_cons,china, india,
                        eurusd,copper,us_yield_curve,us_cons_conf])

    st.success(predict)
# this ensures the code is ran as a script an not imported as a module
# find out how it works if i want to import it as a module
if __name__ == '__main__':
    main()    
