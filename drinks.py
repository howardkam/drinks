import streamlit as st

# Create a Streamlit app
st.title("Price Per Unit Calculator")

# User input for price
price = st.number_input("Enter the price:", min_value=0.01, value=1.00, step=0.01)

# User input for total units
total_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)

# Calculate price per unit
price_per_unit = price / total_units

# Display the result to the user
st.write(f"Price per unit: ${price_per_unit:.2f}")

# Optional: Display a message based on the result
if price_per_unit < 0.1:
    st.warning("Bargain alert! The price per unit is very low.")
elif price_per_unit > 10:
    st.warning("This might be a bit expensive per unit.")

# You can add more features and formatting as desired.
