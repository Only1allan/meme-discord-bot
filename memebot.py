# ===================== SYSTEM ARCHITECTURE OVERVIEW =====================
# This bot implements a client-server architecture that interfaces with two APIs:
# 1. Discord API (WebSocket + REST) - For real-time bot communication
# 2. Reddit API (REST) - For fetching meme content
#
# Data Flow:
# 1. Bot initializes and connects to Discord's Gateway via WebSocket
# 2. On successful connection, starts a periodic task
# 3. Task fetches data from Reddit API
# 4. Processes and filters the content
# 5. Sends formatted content back to Discord via REST API
# ====================================================================

import praw
import discord
from discord.ext import commands, tasks
import asyncio
import random
import aiohttp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MemeBot(commands.Bot):
    def __init__(self):
        # Set up all required intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guild_messages = True
        
        super().__init__(command_prefix='!', intents=intents)
        
        # Get configuration from environment variables
        self.subreddit_name = os.getenv('SUBREDDIT_NAME')
        self.channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
        
        # Initialize Reddit client with environment variables
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT')
        )
        
        # Start the meme posting loop when the bot is ready
        @self.event
        async def on_ready():
            print(f'Bot is ready! Logged in as {self.user.name}')
            print(f'Bot ID: {self.user.id}')
            print('Joined servers:')
            for guild in self.guilds:
                print(f'- {guild.name} (id: {guild.id})')
                print('Available channels:')
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        print(f'  - #{channel.name} (id: {channel.id})')
            
            await self.post_memes()  # Post memes immediately when bot starts
            self.post_meme.start()   # Start the hourly loop
    
    async def post_memes(self, num_memes=10):
        """Separate method to handle posting multiple memes"""
        try:
            channel = self.get_channel(self.channel_id)
            if not channel:
                print(f"Couldn't find channel with ID {self.channel_id}")
                print("Please make sure:")
                print("1. The bot is invited to the server")
                print("2. The channel ID is correct")
                print("3. The bot has permission to view and send messages in the channel")
                return
            
            # Get posts from subreddit - increased limit for better selection
            subreddit = self.reddit.subreddit(self.subreddit_name)
            memes = list(subreddit.hot(limit=100))  # Increased from 50 to 100
            
            # Filter for image posts only
            image_memes = [meme for meme in memes if 
                         any(meme.url.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif'])]
            
            if not image_memes:
                print("No image memes found")
                return
            
            print(f"Found {len(image_memes)} image memes")
            
            # Select random unique memes
            memes_to_post = min(num_memes, len(image_memes))
            selected_memes = random.sample(image_memes, memes_to_post)
            
            print(f"Posting {memes_to_post} memes...")
            
            # Post each meme
            for i, meme in enumerate(selected_memes, 1):
                try:
                    embed = discord.Embed(
                        title=meme.title,
                        url=f"https://reddit.com{meme.permalink}",
                        color=discord.Color.random()
                    )
                    embed.set_image(url=meme.url)
                    embed.set_footer(text=f"👍 {meme.score} | 💬 {meme.num_comments}")
                    
                    await channel.send(embed=embed)
                    print(f"Posted meme {i}/{memes_to_post}: {meme.title}")
                    
                    # Add a small delay between posts
                    await asyncio.sleep(1.5)
                    
                except Exception as e:
                    print(f"Error posting meme {i}: {e}")
                    continue
            
            print("Finished posting memes")
            
        except Exception as e:
            print(f"Error in post_memes: {e}")
    
    @tasks.loop(hours=1)
    async def post_meme(self):
        """Hourly task to post memes"""
        await self.post_memes()

if __name__ == "__main__":
    bot = MemeBot()
    bot.run(os.getenv('DISCORD_TOKEN'))