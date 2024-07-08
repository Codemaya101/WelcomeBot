import discord
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True  # Enable the member intents

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    guild = member.guild
    total_members = guild.member_count
    channel_id = # Replace with your actual welcome channel ID
    role_category_id =  # Replace with your actual role category ID

    # Logging the IDs to verify
    logging.info(f'Welcome channel ID: {channel_id}')
    logging.info(f'Role category ID: {role_category_id}')

    # Fetch the channel and role category objects
    channel = client.get_channel(channel_id)
    role_category = discord.utils.get(member.guild.categories, id=role_category_id)

    if channel:
        logging.info(f'Fetched channel: {channel.name}')
    else:
        logging.error(f'Failed to fetch channel with ID: {channel_id}')

    if role_category:
        logging.info(f'Fetched role category: {role_category.name}')
    else:
        logging.error(f'Failed to fetch role category with ID: {role_category_id}')

    if channel and role_category:
        server_welcome_message = (
            f'✨ **Welcome to our awesome server, {member.mention}!** ✨\n\n'
            f'We\'re thrilled to have you here! 🎉\n\n'
            f'You are the {total_members}th member of our server!\n\n'
            f'🔹 **Don\'t forget to**:\n'
            f'1. **Pick a role** - Head over to the **{role_category.name}** category to choose your roles.\n\n'
            f'Enjoy your stay and feel free to ask if you have any queries in the server! 😊'
        )

        dm_welcome_message = (
            f'👋 **Hi {member.name}, welcome to our server!** 👋\n\n'
            f'We are excited to have you here. 😊\n\n'
            f'Take your time to explore the channels and get to know everyone.\n'
            f'If you have any questions, don\'t be shy and ask away in the server.\n\n'
            f'Have a great time!'
        )

        try:
            await channel.send(server_welcome_message)
            logging.info(f'Sent welcome message to {channel.name}')
        except discord.HTTPException as e:
            logging.error(f"Failed to send server welcome message: {e}")

        try:
            await member.send(dm_welcome_message)
            logging.info(f'Sent DM to {member.name}')
        except discord.Forbidden:
            logging.warning(f"Could not send welcome DM to {member.name}")
    else:
        logging.error(f"Failed to fetch channel or role category.")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
client.run('#paste your bot token here')





