# Alice: A Custom Discord Welcome Bot 🌸

A custom, event-driven Discord bot that automatically greets new server members with randomized, anime-themed welcome embeds and tracks server departures.

## ✨ Features
* **Automated Welcome Embeds:** Listens for the `on_member_join` event to instantly greet new users in a designated welcome channel.
* **Dynamic Generation:** Randomly selects from a curated pool of greetings, immersive messages ("Booting up anime-core systems..."), and aesthetic image banners so the welcome message feels fresh every time.
* **Automated Farewells:** Tracks the `on_member_remove` event to post a goodbye message, which dynamically calculates and displays the remaining human member count in the server.
* **Admin Testing Commands:** Includes `!welcome` and `!testgoodbye` commands so server administrators can preview the embeds and test permissions without having to wait for a user to join or leave.
* ![IMG_20260325_211426](https://github.com/user-attachments/assets/57ae0630-fb93-4b90-badf-1c4b100b93c7)
* ![IMG_20260325_211413](https://github.com/user-attachments/assets/873dae35-2120-4b37-890e-383e7b2c9243)
c6654)

## 🛠️ Tech Stack
* **Language:** Python
* **Library:** `discord.py` (Object-oriented Discord API wrapper)
* **Deployment:** Replit (with environment variables for secure token management)

## 🧠 How It Was Built
This project was developed using a modern, AI-assisted workflow. I utilized AI to generate the foundational `discord.py` boilerplate and embed structures. My role as the system architect included:
* **Prompt Engineering & Logic Design:** Defining the event-driven triggers and the logic for parsing server member counts.
* **Environment Configuration:** Managing the Discord Developer Portal setups, specifically enabling Privileged Gateway Intents (Server Members Intent) for the bot to function correctly.
* **Data Curation:** Structuring the arrays of customized anime-themed dialogue and aesthetic image URLs.
* **Security:** Implementing `os.getenv()` to ensure the bot token (`DISCORD_TOKEN`) and specific channel targets (`WELCOME_CHANNEL_ID`) remain secure and out of the public source code.

## 🚀 Known Limitations & Future Plans
While this bot currently serves its purpose perfectly for my server, future iterations could include:
* **Database Integration:** Moving the hardcoded lists of messages and images into a database to allow for dynamic additions without altering the source code.
* **Slash Commands:** Migrating from the traditional `!prefix` command structure to modern Discord Application Commands (Slash Commands) for a better user experience.
* **Interactive UI:** Adding `discord.ui` buttons to the welcome message that allow users to assign themselves server roles right as they join.
