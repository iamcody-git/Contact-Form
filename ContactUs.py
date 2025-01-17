
import streamlit as st
from sendEmail import send_email


st.markdown(
    """
    <style>
    
    .stForm {
        background-color: #000080; /* Navy blue */
        padding: 20px;
        border-radius: 10px;
    }

   
    .stTextInput input, .stTextArea textarea {
        background-color: #f0f0f0; /* Light gray background */
        color: #000000; /* Black text */
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    
    .stButton button {
        background-color: #000080; /* Navy blue */
        color: white; /* White text */
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }

   
    .stButton button:hover {
        background-color: #0000CD; /* Lighter navy blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for form fields
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if 'first_name' not in st.session_state:
    st.session_state.first_name = ""
if 'last_name' not in st.session_state:
    st.session_state.last_name = ""
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
if 'user_message' not in st.session_state:
    st.session_state.user_message = ""

st.header('Contact Us')

with st.form(key='contact_form'):
    
    col1, col2 = st.columns(2)
    

    with col1:
        first_name = st.text_input('First Name *', value=st.session_state.first_name)
    
  
    with col2:
        last_name = st.text_input('Last Name *', value=st.session_state.last_name)
    
 
    user_email = st.text_input('Email *', value=st.session_state.user_email)
    

    user_message = st.text_area('Message *', value=st.session_state.user_message)
    
   
    submit_button = st.form_submit_button(label='Submit')
    
    # Validation and Email Sending
    if submit_button:
        if not first_name or not last_name or not user_email or not user_message:
            st.error("Please fill out all required fields marked with *.")
        else:
            # Send email using the function from email_sender.py
            success, message = send_email(first_name, last_name, user_email, user_message)
            if success:
                st.success("Thank you for contacting us! We'll get back to you soon.")
                # Clear the form fields by resetting session state
                st.session_state.first_name = ""
                st.session_state.last_name = ""
                st.session_state.user_email = ""
                st.session_state.user_message = ""
                st.session_state.form_submitted = True
            else:
                st.error(message)

# Reset form_submitted state after clearing the form
if st.session_state.form_submitted:
    st.session_state.form_submitted = False