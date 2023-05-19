import streamlit as st
import joblib
import numpy as np
from datetime import datetime

# Load the saved machine learning model
model = joblib.load(open('fraud_detection_model.pkl', 'rb'))

# Create a Streamlit web app
st.title('Credit Card Fraud Detection')
st.write('Enter the details of the credit card transaction below:')

transaction_time = st.number_input('Transaction Time',  step=0.01)

# Input form for credit card details
transaction_id = st.number_input('Transaction ID',  step=0.01)
#transaction_time = st.number_input('Date and time of transaction', min_value=0.01, step=0.01)
merchant_name = st.number_input('Merchant name',  step=0.01)
merchant_category = st.number_input('Merchant category code (MCC)',  step=0.01)
credit_limit = st.number_input('Credit limit', step=0.01)
transaction_currency = st.number_input('Currency of transaction',  step=0.01)
merchant_location_city = st.number_input('Location of merchant (city)', step=0.01)
merchant_location_state = st.number_input('Location of merchant (state)',  step=0.01)
merchant_location_country = st.number_input('Location of merchant (country)',  step=0.01)
merchant_location_zipcode =st.number_input('ZIP code of merchant',  step=0.01)
terminal_id = st.number_input('Terminal ID or device used for the transaction',  step=0.01)
card_type = st.number_input('Type of card',  step=0.01)
card_network = st.number_input('Card network' ,  step=0.01)
card_issuer = st.number_input('Card issuer',  step=0.01)
card_type_detail = st.number_input('Card type ',  step=0.01)
card_number = st.number_input('Card number ', step=0.01)
cardholder_name = st.number_input('Cardholder name ',  step=0.01)
card_expiration_date = st.number_input('Card expiration date',  step=0.01)
card_cvv = st.number_input('CVV or security code ',  step=0.01)
authorization_code = st.number_input('Authorization code', step=0.01)
transaction_status = st.number_input('Transaction status',  step=0.01)
decline_reason = st.number_input('Reason for decline ',  step=0.01)
refund_status = st.number_input('Refund or chargeback' , step=0.01)
transaction_category = st.number_input('Transaction category ', step=0.01)
interest_rate = st.number_input('Interest rate charged (if applicable)',  step=0.01)
late_payment_fees = st.number_input('Late payment fees (if applicable)', step=0.01)
minimum_payment_due = st.number_input('Minimum payment due (if applicable)',  step=0.01)
total_balance = st.number_input('Total balance (including interest and fees)',  step=0.01)
#credit_limit = st.number_input('Credit limit (if applicable)', min_value=0.01, step=0.01)
card_usage_frequency = st.number_input('Card usage frequency', step=0.01)
#average_transaction_amount = st.number_input('Average transaction amount', min_value=0.01, step=0.01)
#card_balance_utilization_ratio = st.number_input('Card balance utilization ratio (balance divided by credit limit)', min_value=0.01, step=0.01)

# Prepare the input data for prediction
#transaction_features = # Prepare the input data for prediction
transaction_features = [transaction_id, merchant_name, merchant_category, credit_limit,transaction_currency, merchant_location_city, merchant_location_state, merchant_location_country, merchant_location_zipcode, terminal_id, card_type, card_network, card_issuer, card_type_detail,
                    card_number, cardholder_name, card_expiration_date, card_cvv, authorization_code,
                    transaction_status, decline_reason, refund_status, transaction_category,
                    interest_rate, late_payment_fees, minimum_payment_due, total_balance,card_usage_frequency]

amount = st.number_input('Transaction Amount', min_value=0.01, step=0.01)
# Prepare the input data for prediction
transaction_data = np.concatenate(([transaction_time],transaction_features, [amount]), axis=None)

# Make prediction
if st.button('Detect Fraud'):
    prediction = model.predict([transaction_data])
    if prediction[0] == 1:
        st.write("<h2 style='color: red ; font-size: 20px;'>Fraud Detected..!</h2>", unsafe_allow_html=True)
    else:
        st.write("<h2 style='color: red ; font-size: 20px;'>No Fraud Detected..!</h2>", unsafe_allow_html=True)