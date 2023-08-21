# DocuSpeak
DocuSpeak! It's a chatbot that allows users to interact with the content of their uploaded documents using language understanding and generation capabilities. If the document doesn't contain that search information, users can also choose to perform an internet search
Screen Cast (Demo) - https://drive.google.com/file/d/1KQICbkn8zCJuoHsSsFGQQarBtmNxd2Zl/view?pli=1
Functionality:

Document-Embedded Chatbot:

Users can upload documents, which are then split into chunks and converted into embeddings.
These embeddings are stored in a Faiss database for efficient retrieval.
When a user asks a question, the system uses K-nearest neighbors (KNN) to find the most relevant embedding(s) in the database.
The relevant chunk(s) are sent to the Chat Completion API, powered by OpenAI's GPT-3.5 model, to generate responses.


Internet Search Chatbot:

This is a separate chatbot mode where users can ask questions that are not related to the uploaded documents.
OpenAI's GPT-3.5 Turbo is used to generate responses for these questions, allowing users to interact with the chatbot as if they're searching the internet.
