# Telegram Quiz Bot

This Python Telegram bot sends 5 safety quiz questions every day at a specified time, aimed at electricians.

## Features

- Automated quizzes sent to employees at specific times.
- Customizable quiz message sending time.
- Easy setup and usage.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ufs8889/Python_Telegram_Quiz_Bot.git
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
    ```bash
    .\env\Scripts\Activate.ps1
    ```

## Usage

1. Navigate to the bot directory:
    ```bash
    cd Python_Telegram_Quiz_Bot\python_telegram_bot_quiz
    ```

2. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Edit bot credentials in `bot_send.py`:
    - Set your Telegram Bot token:
        ```python
        TOKEN = 'YOUR_TOKEN'
        ```
    - Set your channel or group ID:
        ```python
        CHAT_ID = 'YOUR_CHAT_ID'
        ```

4. Configure the time to send quiz messages in `bot_send.py`:
    ```python
    schedule.every().day.at("10:00").do(send_quiz, updater.bot)
    ```

5. Run the bot:
    ```bash
    python bot_send.py
    ```

## Contributing

Contributions are welcome! Feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
