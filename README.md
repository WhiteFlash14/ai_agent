# Code Agent

A minimal implementation of Claude Code, powered by Google's free Gemini API. This project demonstrates a coding agent that can interact with the filesystem, read/write files, and execute Python code, all through natural language prompts. The `calculator` directory provides a simple calculator app for testing the agent's capabilities.

## Features

- **Natural Language Coding Agent**: Ask questions or make requests in plain English; the agent will plan and execute function calls to fulfill your request.
- **Google Gemini API**: Uses the Gemini API for language understanding and function-calling.
- **Function Calling**: The agent can:
  - List files and directories
  - Read file contents
  - Write or overwrite files
  - Execute Python scripts
- **Sandboxed Execution**: All file operations are restricted to the `./calculator` directory for safety.

## Directory Structure

```
code_agent/
│
├── main.py                # Entry point for the coding agent
├── call_function.py       # Function call routing and available functions
├── functions/             # Implements file and code operations
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python.py
├── calculator/            # Test sandbox for the agent
│   ├── main.py            # Calculator CLI
│   ├── pkg/
│   │   ├── calculator.py  # Calculator logic (infix expression evaluator)
│   │   └── render.py      # Pretty-printing calculator results
│   └── tests.py           # Calculator tests
├── requirements.txt       # Python dependencies
└── ...
```

## Getting Started

1. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Set up your Gemini API key**:
   - Create a `.env` file in the root directory:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key
     ```

3. **Run the agent**:
   ```
   python main.py "How do I build a calculator app?"
   ```

   - Use `--verbose` for detailed output:
     ```
     python main.py "Show me the files in the calculator directory" --verbose
     ```

## The Calculator Test App

The `calculator` directory contains a simple command-line calculator for testing the agent's file and code manipulation abilities.

- **Run the calculator directly**:
  ```
  cd calculator
  python main.py "3 + 5 * 2"
  ```

- **Calculator logic**: Supports basic arithmetic with correct operator precedence.
- **Rendering**: Results are displayed in a pretty ASCII box.

## Available Functions

The agent can call the following functions (see `functions/`):

- **get_files_info**: List files in a directory, with size and type.
- **get_file_content**: Read up to 10,000 characters from a file.
- **write_file**: Write content to a file (creates parent directories if needed).
- **run_python_file**: Execute a Python script and return its output.

All file operations are sandboxed to the `./calculator` directory.

## Dependencies

- `google-genai==1.12.1`
- `python-dotenv==1.1.0`

## License

This project is for educational and demonstration purposes only. 