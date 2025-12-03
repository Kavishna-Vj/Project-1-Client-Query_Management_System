import streamlit as st

from db import setup_database
from auth import add_user, verify_user
from client import client_page
from support import support_dashboard

setup_database()

st.title("📝Client Query Management System")

if "logged_in" not in st.session_state: 
    st.session_state.logged_in = False
if "role" not in st.session_state : st.session_state.role = ""
if "username" not in st.session_state:st.session_state.username = "" 

menu=[ "Login","Sign Up","Logout"]
choice=st.sidebar.selectbox("Navigation",menu)

## Register page
if choice == "Sign Up":
     st.subheader("Create a New Account")
     new_username=st.text_input("Enter Username")
     new_password=st.text_input("Enter Password",type='password')               
     role=st.selectbox("Select Role",["Client","Support"])

     if st.button("Register"):
          if new_username and new_password:
               add_user(new_username, new_password, role)
               st.success("Account created successfully! Please login")
          else :
               st.warning("Please fill all details")

     ##Login page
       
elif choice =="Login":
      st.subheader("Login")
      username=st.text_input("Username")
      password=st.text_input("Password",type='password')
      role=st.selectbox("Select Role",["Client","Support"])
      
      if st.button("Login"):
            user_role = verify_user(username, password)
            if user_role and user_role == role:
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.username = username
                st.success(f"Welcome {username}! Logged in as {role}.")
            else:    
                st.error("Invalid username and password")

##  show logout button when logged in                 

if st.session_state.logged_in:
      if st.sidebar.button("Logout"):  
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.warning("Logged out successfully")
        st.rerun()

## Path to correct page 
if st.session_state.logged_in:
     if st.session_state.role.lower() == "client":
          client_page()
     elif st.session_state.role.lower() == "support":
          support_dashboard()    