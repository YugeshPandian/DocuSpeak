import streamlit as st
import openai
import os



def main1():
    openai.api_key = '''YOUR API KEY'''
   
    
    st.header("Explore On Internet")

    user_input = st.text_input("Search on Net")

    if st.button('Search'):
        completion = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                    {"role": "system", "content": "You are the Assistant"},
                    {"role": "user", "content": user_input}
                            ]
                            )
        res = completion.choices[0].message
        st.chat_message("assistant").markdown(res["content"])
        #st.text( res["content"])
