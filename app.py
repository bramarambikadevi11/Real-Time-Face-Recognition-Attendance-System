import streamlit as st
import pandas as pd
import time 
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Get current timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")  # Corrected timestamp format

# Streamlit autorefresh
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# FizzBuzz logic
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz") 
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Reading and displaying the CSV file
csv_file_path = f"Attendance/Attendance_{date}.csv"

try:
    df = pd.read_csv(csv_file_path)
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.write(f"File not found: {csv_file_path}")
except Exception as e:
    st.write(f"An error occurred while reading the file: {e}")
