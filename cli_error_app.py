import argparse
import openai
import os
import dotenv
import platform
import sys
from termcolor import colored

# Load environment variables from .env file
dotenv.load_dotenv()

# Function to communicate with the ChatGPT API
def ask_chatgpt(api_key, error_message, input=None, environment_info=None):
    message = f"""
I ran the following command:\n{input}\n
I received the following error message:\n{error_message}\n
Here is everything I know about my environment:\n{environment_info}\n
{colored('How can I fix it?', 'black', attrs=['bold'])}
    """
    print(message)  # Debugging line
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        api_key=api_key,
        messages=[
            {"role":"system", "content":"You are a very helpful technical assistant. Please keep explanations as simple as possible."},
            {"role":"user", "content":message},
        ]
    )
    formatted_message = response['choices'][0]['message']['content']
    return formatted_message

def get_environment_info():
    environment_info = {
        "operating_system": platform.system(),
        "os_version": platform.release(),
        "python_version": sys.version,
        "environment_variables": "\n" + "\n".join([f"{k}: {v}" for k, v in os.environ.items()])
    }
    formatted_info = "\n".join([colored(f"{key}: {value}",'blue') for key, value in environment_info.items()])
    return formatted_info

# Main function
def main():
    # Define and parse CLI arguments
    parser = argparse.ArgumentParser(description="Interpret and fix terminal errors using ChatGPT")
    parser.add_argument("error_message", type=str, help="Error message from the terminal")
    args = parser.parse_args()

    command, error_message = args.error_message.split('|||')
    #strip the equal api_key= from the api_key
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Ask ChatGPT for a solution to the error
    solution = ask_chatgpt(api_key=api_key,error_message=colored(error_message, 'red'), input=colored(command, 'blue'), environment_info=get_environment_info())

    # Display the solution to the user
    print(colored("ChatGPT suggests the following solution:", 'green', attrs=['bold']))
    print(colored(solution, 'black', attrs=['bold']))

if __name__ == "__main__":
    main()