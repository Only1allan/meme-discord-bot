# Reddit Meme Discord Bot 🤖

A Discord bot that automatically fetches and posts memes from specified subreddits to your Discord server. Built with Python, this bot provides an automated way to keep your Discord server entertained with fresh memes.

## ✨ Features

* **Automatic Posting**: Posts 10 unique memes at startup and every hour
* **Subreddit Flexibility**: Can fetch memes from any specified subreddit
* **Rich Content**: Displays post titles, upvotes, and comment counts
* **Image Support**: Handles multiple image formats (JPG, JPEG, PNG, GIF)
* **Source Links**: Provides links back to original Reddit posts
* **Error Handling**: Robust error handling for various scenarios

## 📋 Prerequisites

* Python 3.8 or higher
* Discord Bot Token
* Reddit API Credentials

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Only1allan/meme-discord-bot/
   cd meme-discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### Discord Bot Setup

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the "Bot" section
4. Create a bot and copy the token
5. Enable these Gateway Intents:
   * PRESENCE INTENT
   * SERVER MEMBERS INTENT
   * MESSAGE CONTENT INTENT

### Reddit API Setup

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create a new application
3. Select "script" as the application type
4. Note your client ID and client secret

### Environment Configuration

Create a `.env` file in the project root:

```env
# Reddit API Credentials
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=python:memebot:v1.0 (by /u/YourRedditUsername)

# Discord Bot Token
DISCORD_TOKEN=your_discord_bot_token

# Channel and Subreddit Configuration
DISCORD_CHANNEL_ID=your_channel_id
SUBREDDIT_NAME=memes
```

### Bot Permissions

1. Go to OAuth2 → URL Generator in Discord Developer Portal
2. Select these scopes:
   * `bot`
   * `applications.commands`
3. Select these permissions:
   * Read Messages/View Channels
   * Send Messages
   * Embed Links
   * Attach Files
   * Read Message History
4. Use the generated URL to invite the bot to your server

## 🎮 Usage

1. **Start the bot**
   ```bash
   python memebot.py
   ```

2. **Bot Operation**
   * Posts 10 memes immediately on startup
   * Continues posting 10 memes every hour
   * Shows status messages in console

## 🛠️ Customization

Modify these parameters in the code:

* `num_memes`: Change number of memes posted per batch
* `@tasks.loop(hours=1)`: Adjust posting frequency
* `.env` settings:
  * `SUBREDDIT_NAME`: Change source subreddit
  * `DISCORD_CHANNEL_ID`: Change target channel

## 🐛 Error Handling

The bot handles various error scenarios:

* Invalid channel access
* Insufficient permissions
* Network connectivity issues
* API rate limiting
* Invalid image URLs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

* [discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper
* [PRAW](https://github.com/praw-dev/praw) - Reddit API wrapper

## 💬 Support

If you have questions or need help:
* Open an issue
* Contact the maintainers
* Check the [Discord.py Documentation](https://discordpy.readthedocs.io/)
* Review the [PRAW Documentation](https://praw.readthedocs.io/)
