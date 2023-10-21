import streamlit as st

# Create a Streamlit app
st.title("Price Per Unit Calculator")

# User input for price
price = st.number_input("Enter the price:", min_value=0.01, value=1.00, step=0.01)

# User input for total units
total_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)

# Calculate price per unit
price_per_unit = price / total_units
with_bev_fee = price_per_unit + 0.06

# Display the result to the user
st.write(f"Price per unit with beverage fee: ${with_bev_fee:.2f}")

# Optional: Display a message based on the result
st.write("Charge $1, your total units profit will be:")
st.write(total_units * 1) - ((with_bev_fee * total_units))
st.write("Charge $2, your total units profit will be:")
st.write(total_units * 1) - ((with_bev_fee * total_units))

# You can add more features and formatting as desired.
