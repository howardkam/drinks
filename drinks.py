import streamlit as st

# Create a Streamlit app
st.title("Price Per Unit Calculator")

# User input for price
price = st.number_input("Enter the price:", min_value=0.01, value=1.00, step=0.01)

# User input for total units
total_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)

# Calculate price per unit
price_per_unit = price / total_units
tax_and_bev = (price_per_unit * 1.04712) + 0.06

# Display the result to the user
st.write(f"Price per unit with beverage fee: ${tax_and_bev:.2f}")

# Select retail price
retail_price_options = [1, 1.5, 2]
retail_price = st.selectbox("Suggested Retail Price:", retail_price_options)

# Optional: Display a message based on the result
st.write(f"Total profit @ ${retail_price} dolars:")
st.write(f"{(total_units * retail_price) - (tax_and_bev * total_units):.2f}")




