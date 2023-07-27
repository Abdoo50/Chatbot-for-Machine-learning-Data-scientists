# Chatbot-for-Machine-learning-Data-scientists
This Repo defines a chatbot using Python and the Streamlit library for creating web applications. The chatbot is designed to answer questions based on a set of responses stored in a JSON file.

The first part of the chatbot is **app.py** imports the necessary libraries, loads the data from the JSON file, and defines the Chatbot class. The Chatbot class has a constructor that takes a name and initializes the responses attribute with the data from the JSON file. It also has a get_response method that takes a question as input and returns the best matching response from the JSON file.

<h2>Deployment:</h2>
The second part of the chatbot deploys the chatbot using **Streamlit**. It first creates a header and a title for the app, and then adds a text input field for the user to enter their questions. The chatbot's response is obtained using the get_response method of the Chatbot class and displayed on the webpage using the st.write method.

If the chatbot cannot find a matching response for the user's question, it returns a generic response stating that it doesn't know the answer but will learn from the user's response.
