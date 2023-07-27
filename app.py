import json

# Load the data from the JSON file
with open("data.json") as f:
  data = json.load(f)

# Create a chatbot that can answer questions
class Chatbot:

  def __init__(self, name):
    self.name = name
    self.responses = data["responses"]

  def get_response(self, question):
    # Find the best matching response for the question
    best_match = None
    for response in self.responses:
      if response["question"] == question:
        best_match = response
        break

    # If there is no matching response, return a generic response
    if best_match is None:
      return "I don't know the answer to that, but I will learn from your answer."

    # Return the best matching response
    return best_match["answer"]

# Create a chatbot instance
chatbot = Chatbot("Denny")

# Start the conversation
while True:
  # Get the user's input
  question = input("Hello, How I can Help you? \n")

  # Get the chatbot's response
  response = chatbot.get_response(question)

  # Print the chatbot's response
  print(response)