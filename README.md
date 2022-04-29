# Kanapy

Kana is a multi-purpose personal Discord bot written in Python.

### Tech

- [discord.py](https://github.com/Rapptz/discord.py) - An API wrapper for Discord written in Python!

### Installation & Setup

Kanapy requires [Python](https://www.python.org/) 3.8+ to run, to know your version run this following command `python --version`

1. **Set up venv** [ Optional ]
   `python -m venv venv`

2. **Install dependencies**
   `pip install -U -r requirements.txt`

3. **Create a `.env` file with the following template**:

```
- TOKEN=" " # Your Discord Bot Token
- USER_MONGO=" " # Your MongoDB connection URI
- PSQL_URI=" " # Your PSQL connection URI

# this is for the Search cog, unload it if you don't have a key.
- YOUTUBE_KEY=" " # Your YouTube Data API key
```

### Running your Instance

You could use a Process Manager like [PM2](https://pm2.keymetrics.io/), [Docker](https://www.docker.com/) or even [systemd](https://systemd.io/)
there are examples of each in the examples folder