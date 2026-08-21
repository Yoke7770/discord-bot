# Discord Bot (discord.py)

This repository contains a minimal Python Discord bot scaffold using discord.py.

Setup (local):
1. Create a virtual environment: python -m venv venv
2. Activate it: source venv/bin/activate (macOS/Linux) or venv\Scripts\activate (Windows)
3. Install dependencies: pip install -r requirements.txt
4. Create a .env file or set DISCORD_TOKEN in your environment. See .env.example
5. Run: python bot.py

Railway deploy (quick):
- On Railway: New Project → Deploy from GitHub → select this repository (Yoke7770/discord-bot)
- Railway will detect Python if requirements.txt is present.
- In Project Settings → Variables, add DISCORD_TOKEN with your bot token (mark as secret).
- Ensure the service type is a Worker and the Start Command is: python bot.py (or leave Procfile: worker: python bot.py)
- Deploy and check logs for "Logged in as" message.

Security: do NOT commit your real token. Use Railway variables or environment variables.
