# CLI Error Assistant

CLI Error Assistant is a command-line utility that helps you automatically diagnose and fix errors encountered in the terminal. By leveraging the OpenAI ChatGPT API, the utility provides suggestions for fixing common errors in a user-friendly manner.

Pass all of the relevant information about the error. Pass the following to ChatGPT for a fast answer:
- The command you put in
- The error message
- The environment information (OS, Python version, environment variables, etc.)

See the example below:

![](https://github.com/odagayev/easy_openai_qa/blob/master/example_of_cli.gif)

## Features

- Given an option to provide error and environment information directly OpenAI for QA via bash
- Parses error messages and environment information
- Communicates with OpenAI ChatGPT API to get error resolution suggestions
- Displays solutions in a user-friendly and color-coded format

## Prerequisites

- Python 3.6 or later
- OpenAI Python library (v0.27.0 or later)
- `termcolor` library
- An OpenAI API key

## Installation

1. Clone this repository:

```
git clone https://github.com/odagayev/easy_openai_qa
```

2. Install the required Python libraries:

```
pip install openai termcolor python-dotenv
```

3. Create a `.env` file in the project's root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

4. Set up the `error_wrapper.sh` script to make it accessible from the terminal:

```
sudo ln -s /path/to/your/openai_qa_error.sh /usr/local/bin/openai_qa_error
```

## Usage

To use the CLI Error Assistant, simply prefix any command in the terminal with `error_wrapper`. For example:

```
openai_qa_error ls non_existent_directory
```
or 
```
openai_qa_error python3 test.py
```


If an error occurs, the CLI Error Assistant will capture the error message and provide a solution using the ChatGPT API.

## License

This project is licensed under the MIT License - see the [LICENSE](license.md) file for details. 
