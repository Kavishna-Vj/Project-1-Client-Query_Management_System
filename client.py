import streamlit as st
from datetime import datetime
from db import get_connection

def client_page():
    st.header("Submit a New Query")
    email=st.text_input("Email ID")
    mobile=st.text_input("Mobile Number")
    heading=st.text_input("Query Heading")
    description=st.text_area("Query Description")
                  
    if st.button("Submit Query"):
        if email and mobile and heading and description:
            conn = get_connection()
            c = conn.cursor()
            c.execute("""INSERT INTO queries(email,mobile, heading,
                                         description, created_time,closed_time, status)
                                    VALUES(?,?,?,?,?,?,?)""",(email, mobile, heading, description,datetime.now()
                                                    .strftime("%Y-%m-%d %H:%M:%S"),"","Opened"))
            conn.commit()
            conn.close()          
            st.success("✅Query submitted successfully")
        else:
            st.warning("Please fill all field")
