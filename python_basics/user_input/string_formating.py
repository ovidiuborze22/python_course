# string formatting
user_input = input("Enter your name: ")
message = "Hello %s!" % user_input # works with python v2 and v3 
message = f"Hello {user_input}" # works with python v3.6 and later versions
print(message)
