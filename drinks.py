import streamlit as st

# Create two columns
col1, col2 = st.columns(2)

# Column 1
with col1:
    ##################### BEVERAGE CALC PAGE #####################
    st.title("BEVERAGE PROFIT CALC")
    st.subheader("Sales tax and beverage fee calculated")
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
    price = st.number_input("Enter the price:", min_value=0.01, value=1.0, step=0.01)
    # User input for total units
    total_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)
    # Calculate cost per unit
    tax_and_bev = ((price / total_units) * 1.04712) + 0.06
    st.write(f"Cost per unit after tax and bev fee: ${tax_and_bev:.2f}")
    # Select retail price per unit
    #retail_price_options = [1, 1.25, 1.50, 2]
    #retail_price = st.selectbox("Suggested Retail Price:", retail_price_options)
    pre_retail = st.slider("Sell for 1-5", 1.0, 3.0, 1.0, 0.25)
    retail_price = float(pre_retail)
    # Optional: Display a message based on the result
    st.subheader(f"Total profit @ ${retail_price}:")
    st.subheader(f"{((retail_price - tax_and_bev) * total_units):.2f}")
    # # Define the content for the fixed footer
    footer_content = """
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: black; text-align: center; padding: 10px;">
        <p>Written by Howard Kam</p>
    </div>
    """
    # # Display the fixed footer using the st.markdown function
    st.markdown(footer_content, unsafe_allow_html=True)
    ###################################################################
st.markdown("---")

# Column 2
with col2:
    ##################### BEVERAGE CALC PAGE #####################
    st.title("FOOD PROFIT CALC")
    st.subheader("Sales tax calculated")
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
    foodprice = st.number_input("Enter the price:", min_value=0.01, value=1.0, step=0.01)
    # User input for total units
    foodtotal_units = st.number_input("Enter the total units:", min_value=1, value=1, step=1)
    # Calculate cost per unit
    tax = ((price / total_units) * 1.04712)
    st.write(f"Cost per unit after tax and bev fee: ${tax:.2f}")
    # Select retail price per unit
    #retail_price_options = [1, 1.25, 1.50, 2]
    #retail_price = st.selectbox("Suggested Retail Price:", retail_price_options)
    foodpre_retail = st.slider("Sell for 1-5", 1.0, 3.0, 1.0, 0.25)
    foodretail_price = float(foodpre_retail)
    # Optional: Display a message based on the result
    st.subheader(f"Total profit @ ${foodretail_price}:")
    st.subheader(f"{((foodretail_price - tax) * foodtotal_units):.2f}")

    ###################################################################
