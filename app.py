import streamlit as st
import openai
import os
# Set your OpenAI API key


def main1():
    openai.api_key = "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"
   
    # Streamlit app code
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
