
# Voice Command Recognition System

This project implements a basic voice command recognition system using Python and PocketSphinx.

## Setup

1. Clone this repository.
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute:

```bash
python voice_command_recognizer.py
```

Speak into your microphone after you see "Listening..." and the system will recognize commands such as "hello," "exit," or "stop."

## Development

This project uses the SpeechRecognition library and PocketSphinx for processing speech into text.

Feel free to extend or modify the code for more complex command handling and additional features.
