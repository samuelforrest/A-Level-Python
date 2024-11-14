print("Hello, My name is Jarvis. I am a chatbot.")
user_input = input("What is your name? ") # This will ask the user for their name and append to variable user_name

if user_input.startswith("My Name is "):
    user_actual_name = user_input[len("My Name is "):]
else:
    user_actual_name = user_input

user_input = input("Hello, " + user_actual_name + ". How are you feeling today?")

if user_input: # This will check if user_input is not empty
  a=user_input.split("I am")
  print("Why are you feeling",a[1],"?")
else:
   print("I am sorry to hear that. I hope you feel better soon.")