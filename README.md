# Voice Assistant

This is a simple voice assistant named Axel that can perform various tasks based on voice commands.

## Features

- Greet the user
- Tell the current time
- Tell the current date
- Open Google
- Open YouTube
- Tell a joke
- Search on Google
- Play a Spotify playlist
- Close the browser
- Get weather information for a specified city
- Open Google News
- Perform calculations
- Play music from a specified directory
- Shutdown the computer
- Restart the computer
- Open the calculator
- Exit the assistant

## How to Use

1. **Install the required libraries**:
    ```sh
    pip install speechrecognition pyttsx3 pyjokes requests
    ```

2. **Run the script**:
    ```sh
    python index.py
    ```

3. **Give voice commands**:
    - Say "Axel" to wake up the assistant.
    - Use commands like "time", "date", "open google", "open youtube", "tell me a joke", "search for [query]", "play spotify music", "close browser", "weather in [city]", "news", "calculate [expression]", "play music", "shutdown", "restart", "open calculator", "exit".

## How to Clone

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/voice-assistant.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd voice-assistant
    ```

3. **Follow the usage instructions**.

## Note

- Replace the placeholder API key in the `get_weather` function with a valid API key from OpenWeatherMap.
- Update the `music_dir` variable in the `play music` command with the path to your music folder.
