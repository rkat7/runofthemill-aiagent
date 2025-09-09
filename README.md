#### This uses Gemini Flash API

#### This is a CLI based agent like Claude code or OpenAI's codex

## Currently has the following abilities:
    - Can fetch the files in the given directory
    - Can fetch the contents of the given file
    - Can create/overwrite (write) a new file with content provided
    - Can run a Python file with Python3

## To run this:
    - make sure you've uv installed
    - Have your own Gemini API Key
    - Start interactions in the following way
        - $ uv run main.py "{Your Prompt}" 