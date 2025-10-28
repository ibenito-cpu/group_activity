def save_message(message):
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print("Error saving message:", e)

def read_message():
    try:
        print("Reading saved message...")
        with open("user_message.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: No saved message found.")
    except Exception as e:
        print("Error reading message:", 
