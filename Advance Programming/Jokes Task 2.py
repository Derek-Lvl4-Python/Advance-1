import random

def load_jokes(filename):
    try:
        with open('Jokes.txt', 'r') as file:
            jokes = file.readlines()

   
        valid_jokes = [joke.strip() for joke in jokes if '?' in joke]
        
       
        if not valid_jokes:
            print("No jokes with '?' were found in the file.")
        else:
            print(f"Loaded {len(valid_jokes)} jokes.")

        return valid_jokes

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def tell_joke(jokes):
    if not jokes:
        print("No jokes available to display.")
        return
    joke = random.choice(jokes)
    if '?' in joke:
        setup, punchline = joke.split('?', 1)
        print(f"Setup: {setup.strip()}?")
        input("Press Enter to see the punchline...")
        print(f"Punchline: {punchline.strip()}")
    else:
        print("Invalid joke format: No '?' found in joke.")

def main():
    filename = 'Jokes'
    jokes = load_jokes(filename)

    if not jokes:
        return

    while True:
        user_input = input("Alexa, tell me a Joke (or type 'quit' to exit): ").lower()

        if user_input == 'quit':
            print("Goodbye!")
            break
        elif 'tell me a joke' in user_input:
            tell_joke(jokes)
        else:
            print("Please ask 'Alexa, tell me a Joke' or type 'quit' to exit.")

if __name__ == "__main__":
    main()
