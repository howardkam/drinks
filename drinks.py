import streamlit as st

# Define the main page content
def main_page():
    st.title("Streamlit Multi-Page App")
    st.write("This is the main page.")
    st.write("Click the button to go to another page.")
    
    if st.button("Go to Second Page"):
        page = "second_page"

    return page

# Define the second page content
def second_page():
    st.title("Second Page")
    st.write("This is the second page.")
    st.write("Click the button to go back to the main page.")
    
    if st.button("Go Back to Main Page"):
        page = "main_page"

    return page

# Main function
def main():
    page = "main_page"

    if page == "main_page":
        page = main_page()
    elif page == "second_page":
        page = second_page()

if __name__ == '__main__':
    main()