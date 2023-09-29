#!/bin/bash

# URL variable
URL='https://chat.openai.com/?model=gpt-4'

# Check if a question was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <question_for_chatgpt4>"
    exit 1
fi

QUESTION="$1"

xdg-open "$URL"
sleep 10
xdotool type "$QUESTION"
xdotool key Return
