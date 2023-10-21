import streamlit as st

# Create a Streamlit app
st.title("Price Per Unit Calculator")
# Create a rainbow-colored divider using HTML and CSS
st.markdown(
    """
    <style>
    .rainbow-divider {
        background: linear-gradient(to right, #FF0000, #FFA500, #FFFF00, #008000, #0000FF, #4B0082, #9400D3);
        height: 1px;
    }
    </style>
    <div class="rainbow-divider"></div>
    """,
    unsafe_allow_html=True
)

# User input for price
price = st.number_input("Enter the price:",min_value=1, max_value=None, value=None, step=None)

# User input for total units
total_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)


# Calculate price per unit
price_per_unit = price / total_units
tax_and_bev = (price_per_unit * 1.04712) + 0.06

# Display the result to the user
st.write(f"Price per unit with beverage fee: ${tax_and_bev:.2f}")

# Select retail price
retail_price_options = [1, 1.50, 2]
retail_price = st.selectbox("Suggested Retail Price:", retail_price_options)

# Optional: Display a message based on the result
st.subheader(f"Total profit @ ${retail_price}:")
st.subheader(f"{(total_units * retail_price) - (tax_and_bev * total_units):.2f}")


# Define the content for the fixed footer
footer_content = """
<div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: #f0f0f0; text-align: center; padding: 10px;">
    <p>This is a fixed footer in Streamlit.</p>
</div>
"""

# Display the fixed footer using the st.markdown function
st.markdown(footer_content, unsafe_allow_html=True)

# Your main content goes above this
st.write("Written by Howard Kam")

