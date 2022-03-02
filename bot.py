import discord
from voting import Voting
from register import Register

TOKEN = 'OTQxNDg5NDEwNzc0NTUyNjU5.YgWsVw.lj3O9-bcYfHqNSAjVR0vy2fs1AY'

client = discord.Client()


new_welcome_id = 939577544901025852
new_officer_id = 935592737963651192
new_sc = 935592739624587344
old_welcome_id = 942822050601500701
old_officer_id = 942822050576343051
PV = "<:PV:947823514973503499>"
PRESENT = "<:PRESENT:947823484648714270>"
FOR = "<:FOR:947822518041972767>"
AGAINST = "<:AGAINST:947823413823668285>"
ABSTAIN = "<:ABSTAIN:947823455498280990>"


vote = Voting()
register = Register()
register.setup_dict()
green = 0x64E900



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='the votes'))
    channel = client.get_channel(new_welcome_id)
    welcome = discord.Embed(title=f"Welcome to the server! My name is DESMUN Bot.", description=f"To get started head over to the registration channel.", colour=green)
    welcome.add_field(name="For a full list of commands:", value="Type !help")
#    await channel.send(content=None, embed=welcome)
#    await channel.send("!help_register_me")
#    await channel.send("!placards")




@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    member = message.author
    guild = message.guild
    channel = str(message.channel.name)
    comm = str(message.channel.category).lower()
    print(f'{username}: {user_message} ({channel})')

    if user_message.lower() == '!help_register_me' and comm == "lobby":
        help_reg = discord.Embed(title=f"How do i register at DESMUN?",
                                 description=f"Type !register ***Your committee***, ***Your country***, ***Your name***", colour=green)
        help_reg.add_field(name="Tips", value="- Leave the brackets out when typing\n- Use commas and spaces between committee, country and name")
        help_reg.set_footer(text="Type !help_register_me for this message to appear again. For any other queries on registration contact tech support.")
        await message.channel.send(content=None, embed=help_reg)
        if message.author == client.user:
            await message.delete(delay=5)
    elif user_message.lower() == '!placards':
        placards = discord.Embed(title="Delegate placards",
                                 description=f"React to your country to raise your placard and let your chair know you want to speak.",
                                 colour=green)
        chan_list = register.placard_channels()
        print(chan_list)
        for chan in chan_list:
            channel = client.get_channel(int(chan))
            message_1 = await channel.send(content=None, embed=placards)
            if int(chan) != new_sc:
                message_2 = await channel.send(content="** **")
                for country in register.countries_1:
                    await message_1.add_reaction(country)
                for country in register.countries_2:
                    await message_2.add_reaction(country)
            else:
                for country in register.countries_sc:
                    await message_1.add_reaction(country)
        if message.author == client.user:
            await message.delete(delay=5)
    elif message.channel.name == 'registration' and user_message.lower().count('!register'):
        reg_list = register.create_reg(message.content)
        if not register.check_reg(reg_list):
            response = f"<@{member.id}>\nHmm you might have made a mistake typing.\nLook below to learn more."
            await message.channel.send(response)
            await message.channel.send("!help_register_me")
            return
        if register.check_user(str(member)):
            roles = register.find_roles(reg_list)
            new_nick = register.setup_nick(reg_list)
            reg = discord.Embed(title=f"Registered!", description=f"{member} is a now part of {reg_list[0]} at DESMUN.", colour=green)
            for i in roles:
                role = guild.get_role(i)
                await member.add_roles(role)
            await member.send(content=None, embed=reg)
            await member.edit(nick=new_nick)
            return
        else:
            rereg_error = discord.Embed(title=f"Error occurred.", description=f"You have already been registered.", colour=green)
            await member.send(content=None, embed=rereg_error)
    else:
        officer_role = guild.get_role(new_officer_id)
        for role in member.roles:
            if officer_role == role:
                if user_message.lower() == '!help':
                    help = discord.Embed(title="DESMUN Bot Commands", description="Here is everything I can do:", colour=green)
                    help.add_field(name="!help", value="to view this list of commands again")
                    help.add_field(name="!register", value="registers you into your committee")
                    help.add_field(name="!help_register_me", value="shows information on how to register properly")
                    help.add_field(name="!vote", value="starts voting procedures")
                    help.add_field(name="!endvote", value="ends voting procedures")
                    help.add_field(name="!rollcall", value="starts roll call")
                    help.add_field(name="!endroll", value="ends roll call")
                    help.add_field(name="!clear", value="clear vote and rollcall data")
                    help.set_footer(text="All voting related commands can only be used by student officers. For any queries on the bot contact tech support.")
                    await message.channel.send(content=None, embed=help)

                elif user_message.lower() == "!rollcall":
                    rollcall = discord.Embed(title="Are you voting?", description=f"React {PRESENT} for present and {PV} for present and voting.", colour=green)
                    rollcall.set_footer(text="Your first vote is the one that counts in the results.")
                    emojis = [PRESENT, PV]
                    message = await message.channel.send(content=None, embed=rollcall)
                    for emoji in emojis:
                        await message.add_reaction(emoji)

                elif user_message.lower() == "!vote":
                    voting = discord.Embed(title="Voting procedure has started.", description=f"React {FOR} to vote for , {AGAINST} to vote against, {ABSTAIN} to abstain.", colour=green)
                    voting.set_footer(text="Your first vote is the one that counts in the results.")
                    emojis = [FOR, AGAINST, ABSTAIN]
                    message = await message.channel.send(content=None, embed=voting)
                    for emoji in emojis:
                        await message.add_reaction(emoji)

                elif user_message.lower() == "!endvote":
                    v = vote.end_vote("fa", comm)
                    endvote = discord.Embed(title="Voting procedure has ended.", description=f"{v}", colour=green)
                    message = await message.channel.send(content=None, embed=endvote)

                elif user_message.lower() == "!endroll":
                    v = vote.end_vote("pv", comm)
                    endroll = discord.Embed(title="Rollcall procedure has ended.", description=f"{v}", colour=green)
                    message = await message.channel.send(content=None, embed=endroll)

                elif user_message.lower() == "!clear":
                    vote.clear(comm)
                    clear = discord.Embed(title="All vote and rollcall data has been cleared.", colour=green)
                    message = await message.channel.send(content=None, embed=clear)


@client.event
async def on_reaction_add(reaction, user):
    if type(reaction.emoji) is str:
        return
    comm = str(reaction.message.channel.category).lower()
    emoji = reaction.emoji.name
    if user != client.user:
        if emoji == "FOR" and vote.check_voter(user):
            vote.vote("f", comm)
            return
        elif emoji == "AGAINST" and vote.check_voter(user):
            vote.vote("ag", comm)
            return
        elif emoji == "AGAINST" and vote.check_voter(user):
            vote.vote("ag", comm)
            return
        elif emoji == "ABSTAIN" and vote.check_voter(user):
            vote.vote("ab", comm)
            return
        elif emoji == "PRESENT" and vote.check_voter(user):
            vote.vote("p", comm)
            return
        elif emoji == "PV" and vote.check_voter(user):
            vote.vote("pv", comm)
            return
client.run(TOKEN)
