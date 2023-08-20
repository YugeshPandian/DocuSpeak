import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app import *
import openai
import os




def main():
    st.title('DocuSpeak')
    
    pdf= st.file_uploader("Upload your Document",type='pdf')
    if pdf is not None:
        pdf_bytes=pdf.read()
        temp_pdf_path = "temp.pdf"
        with open(temp_pdf_path, "wb") as temp_pdf_file:
            temp_pdf_file.write(pdf_bytes)

        loader = PyPDFLoader(temp_pdf_path)
        #loader=PyPDFLoader(pdf_bytes)
        content=loader.load_and_split()

       
       
        with st.chat_message("assistant"):
            st.write(f'Raise Question about your document "{pdf.name.title()}"')
        
        query=st.text_input("Ask Something to your Document ")
        

        if query:
         
            st.chat_message("user").markdown(query)
            embedings=OpenAIEmbeddings()
            embeding_db=FAISS.from_documents(content,embedings)

            embeding_db.save_local("embeding_db")

            chat_db=FAISS.load_local("embeding_db",embedings)
                        
            l=ChatOpenAI()
            query_completion=RetrievalQA.from_chain_type(l,retriever=chat_db.as_retriever())
            response=query_completion({"query":query})
            
            st.chat_message("assistant").markdown(response["result"])
            

        
            #docs=chat_db.similarity_search(query)
            #st.chat_message("assistant").markdown(docs)

if __name__=='__main__':
    main()
    main1()
