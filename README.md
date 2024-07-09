Sure! Here’s a README for the Bump Butler program:

---

# Bump Butler

Bump Butler is a proof-of-concept program developed to test if it was possible to automate server bumping on Disboard in Discord.

## Disclaimer

Using Bump Butler or similar tools will violate Discord's ToS and can result in account suspension or a permanent ban. By using Bump Butler, you acknowledge that you are violating Discord's ToS and accept all associated risks. The developers of Bump Butler do not endorse or encourage any activity that breaches Discord's ToS and are not responsible for any consequences arising from the use of this software.

## Requirements

- Python 3.11+

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/BumpButler.git
    cd BumpButler
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Rename `.envExample` to `.env` and edit the values to match your settings:
    ```sh
    mv .envExample .env
    ```

4. Open the `.env` file and set your values:
    ```
    token = "your token"
    ownerID = your_user_id
    startMessage = "your message to start the bot"
    ```

## Usage

1. Run the program:
```sh
python main.py
```

2. Go to the server where the user's token you added is also present.
3. Send the start message from the account you set as the owner (ownerID) in the `.env` file.

If set up correctly, the bot will respond with "ok" and bump every 2 hours.

The program will only start with the message specified by the `ownerID` and `startMessage` in the `.env` file.

## Important Notes

- Bump Butler only works with a user token, not a bot token. Bots cannot use slash commands, which is why this is not allowed by Discord's ToS.
- Using this program can lead to your Discord account being suspended or permanently banned.

## Credits

- Developed by Hamziee
- Thanks to [Selfcord.py](https://github.com/OmegaDevStudio/Selfcord) for making it super easy