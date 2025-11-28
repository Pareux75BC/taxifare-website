import streamlit as st
import datetime
import requests

'''
# BONJOUR A TOUS
'''

st.markdown('''
**Welcome to my app frontpage**
''')

'''
## Please select the parameters of your ride
'''

passenger_count = st.slider('Select the number of passengers', 1, 10, 1)

date = st.date_input(
    "Select the date of your ride",
    datetime.date(2025, 11, 28))

time = st.time_input('Select the time of your ride', datetime.time(8, 45))

pickup_longitude = st.text_input('Select pickup longitude', -73.9506)
pickup_latitude = st.text_input('Select pickup latitude', 40.7833)
dropoff_longitude = st.text_input('Select dropoff longitude', -73.9844)
dropoff_latitude = st.text_input('Select dropoff latitude', 40.7698)

'''
## NOW, YOUR FARE WILL BE
'''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = dict(
        pickup_datetime=f'{date} {time}',
        pickup_longitude=float(pickup_longitude),
        pickup_latitude=float(pickup_latitude),
        dropoff_longitude=float(dropoff_longitude),
        dropoff_latitude=float(dropoff_latitude),
        passenger_count=int(passenger_count))

result = requests.get(url=url, params=params).json()['fare']

# Let's retrieve the prediction from the **JSON** returned by the API...

if st.button('Predict'):
    st.write('Congrats 🎉, you \'ve successfully predicted your fare')
    st.write(f'Your fare wil be ...{result:.2f}')
