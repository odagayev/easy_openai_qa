#!/bin/bash

# Execute the command and capture the STDERR
error_output=$( "$@" 2>&1 1>/dev/null )

# If the command fails (non-zero exit status)
if [ $? -ne 0 ]; then
    # Concatenate the command and error message, separated by a delimiter
    command_and_error="${*}|||${error_output}"
    # Pass the concatenated string to your Python script
    python3 /Users/odagayev/Documents/code/easy_openai_qa/cli_error_app.py "$command_and_error"
else
    # If the command succeeds, print the output
    echo "$error_output"
fi
