import random # This will import the random module, which is needed to randomly pick from the 3 responses later.

def remove_punctuation_and_capitals(text): # This defines a function which allows us to remove punctuation and convert to lowercase.
  result = "" # We first need an empty string to store the cleaned text.

  for char in text: # We iterate through each character in the input text.
     if char.isalpha() or char == " ": # If the character is a letter or a space, we add it to the result string in lowercase.
        result += char.lower() 

  return result # The cleaned text will be returned with no punctuation and all lowercase.

# This defines a long list of tuples, each containing a phase to look for in user's input and a list of responses to choose from.
psychobabble = [
    ("i need ", # Phase to look for
        ["why do you need", # List of responses to randomly choose from
         "Would it really help you to get",
         "Are you sure you need"]),
    ("why dont you",
        ["Do you really think I don't",
         "Perhaps eventually I will",
         "Do you really want me to"]),
    ("why cant i",
        ["Do you think you should be able to",
         "What would you do if you could",
         "Have you really tried to"]),
    ("i cant",
        ["How do you know you can't",
         "If you tried harder, perhaps you could",
         "What would it take for you to"]),
    ("i am",
        ["Did you come to me because you are",
         "How long have you been",
         "How do you feel about being"])
]

print("Hello, My name is Jarvis Appleseed. I am a chatbot!") # Conversation starts with a generic chatbot greeting
user_input = input("What is your name? ") # This will ask the user for their name and append it to variable user_name

if user_input.startswith("My name is "): # This will check if the user input starts with "My name is"
    user_actual_name = user_input[len("My Name is "):] # We will only take the part of the input after the phrase, hence getting the user's name

else:
    user_actual_name = user_input # If there is no phrase before their name, the name is simply printed

user_input = input("Hello, " + user_actual_name + ". How are you feeling today?") # Stores the response for their feeling in user_input

if user_input: # This will check if user_input is not empty (ie. the user has entered something).
  a = user_input.split("I am") # We split their input on "I am" to get the feeling they have entered.
  print("Why are you feeling", a[1], "?") # The output hence will be only the part of their input after "I am", the raw emotion.

else:
   print("It's good to speak about your emotions!") # This is the default response if the input is empty.

while user_input != "quit": # We start a loop to keep the convo going until the user types "quit".
  user_input = input("What would you like to talk about? Or type 'quit' to end. ")
  user_input = remove_punctuation_and_capitals(user_input) # Clean the user inut by usiing the predefined function.

  print(user_input) # Print the cleaned input for debugging purposes (can be removed later).

  response_found = False # We initialise a variable to keep track of whether a response has been found for the user input.

  for phase, responses in psychobabble: # Loop though each phrase in "pysychobabble" and the corresponding responses.
     if phase in user_input: # If the phrase is found, we randomly chose a response.
        print(random.choice(responses) + " ?")
        response_found = True
        break # Exits the loop once response found and printed
  if not response_found:
     print("I am sorry, I do not understand.") # Default error message

print("Thanks for talking to me. See you soon!") # Goodbye message if the loop is quit

