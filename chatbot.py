import random # This will import the random module, which is needed to randomly pick from the 3 responses later.

def remove_punctuation_and_capitals(text): # This defines a function which allows us to remove punctuation and convert to lowercase.
  result = "" # We first need an empty string to store the cleaned text.

  for char in text: # We iterate through each character in the input text.
     if char.isalpha() or char == " ": # If the character is a letter or a space, we add it to the result string in lowercase.
        result += char.lower() 

  return result # The cleaned text will be returned with no punctuation and all lowercase.

psychobabble = [
    ("i need ",
        ["why do you need",
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

print("Hello, My name is Jarvis. I am a chatbot.")
user_input = input("What is your name? ") # This will ask the user for their name and append to variable user_name

if user_input.startswith("My name is "):
    user_actual_name = user_input[len("My Name is "):]
else:
    user_actual_name = user_input

user_input = input("Hello, " + user_actual_name + ". How are you feeling today?")

if user_input: # This will check if user_input is not empty
  a = user_input.split("I am")
  print("Why are you feeling", a[1], "?")
else:
   print("I am sorry to hear that. I hope you feel better soon.")

while user_input != "quit":
  user_input = input("What would you like to talk about? Or type 'quit' to end. ")
  user_input = remove_punctuation_and_capitals(user_input)
  print(user_input)
  response_found = False
  for phase, responses in psychobabble:
     if phase in user_input:
        print(random.choice(responses) + " ?")
        response_found = True
        break
  if not response_found:
     print("I am sorry, I do not understand.")
print("Thanks")

