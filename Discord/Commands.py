"""
    Commands cog for East
    Holds all commands usable by any user, and a couple of classes relevant to those commands.
    Author: CraftSpider, HiddenStorys
"""
import discord
from discord.ext import commands
import asyncio
import random
import datetime
from collections import defaultdict

active_pw = defaultdict(lambda: None)

perms = {}


def sort_mem(member):
    """Function key for sorting PW_Member objects."""
    return member.end - member.start


class Commands:
    """These commands can be used by anyone, as long as East is awake.\n He doesn't care who is using them."""

    __slots__ = ['bot', 'iggy', 'temp']

    def __init__(self, bot):
        """Initialize the Commands cog. Takes in an instance of bot to use while running."""
        self.bot = bot
        self.iggy = 0
        self.temp = []
    
    #
    #   Generator Strings
    #
    noun = ["dog", "cat", "robot", "astronaut", "man", "woman", "person", "child", "giant", "elephant", "zebra",
            "animal", "box", "tree", "wizard", "mage", "swordsman", "soldier", "inventor", "doctor", "Talos",
            "dinosaur", "insect", "nerd", "dancer", "singer", "actor", "barista", "acrobat", "gamer", "writer",
            "dragon", "East"]
    adjective = ["happy", "sad", "athletic", "giant", "tiny", "smart", "silly", "unintelligent", "funny",
                 "coffee-loving", "lazy", "spray-tanned", "angry", "disheveled", "annoying", "loud", "quiet", "shy",
                 "extroverted", "jumpy", "ditzy", "strong", "weak", "smiley", "annoyed", "dextrous"]
    goal = ["fly around the world", "go on a date", "win a race", "tell their crush how they feel",
            "find their soulmate", "write a chatbot", "get into university", "graduate high school",
            "plant a hundred trees", "find their biological parents", "fill their bucket list", "find atlantis",
            "learn magic", "learn to paint", "drive a car", "pilot a spaceship", "leave Earth", "go home",
            "redo elementary school", "not spill their beer", "help East (seriously guys, I need it)"]
    obstacle = ["learning to read", "fighting aliens", "saving the world", "doing algebra", "losing their hearing",
                "losing their sense of sight", "learning the language", "hacking the mainframe", "coming of age",
                "the nuclear apocalypse is happening", "incredibly drunk", "drinking coffee", "surfing",
                "spying on the bad guys", "smelling terrible", "having a bad hair day", "exploring the new planet",
                "on the moon", "on Mars"]
    
    place = ["pub", "spaceship", "museum", "office", "jungle", "forest", "coffee shop", "store", "market", "station",
             "tree", "hut", "house", "bed", "bus", "car", "dormitory", "school", "desert", "ballroom", "cattery",
             "shelter", "street"]
    place_adjective = ["quiet", "loud", "crowded", "deserted", "bookish", "colorful", "balloon-filled", "book", "tree",
                       "money", "video game", "cat", "dog", "busy", "apocalypse", "writer", "magic", "light", "dark",
                       "robotic", "futuristic", "old-timey"]
    action = ["learn to read", "jump up and down", "cry a lot", "cry a little", "smile", "spin in a circle",
              "get arrested", "dance to the music", "listen to your favourite song", "eat all the food",
              "win the lottery", "hack the mainframe", "save the world", "find atlantis", "get accepted to Hogwarts",
              "swim around", "defy gravity", "spy on the bad guys", "drive a car", "enter the rocket ship",
              "learn math", "write a lot", "do gymnastics"]
    
    #
    #   User Commands
    #
    
    @commands.command()
    async def information(self, ctx):
        """Gives a short blurb about East."""
        await ctx.send("Hey, I'm East! Official joke-bot of nothing.\
                           \nMy Developers are CraftSpider, Dino, and HiddenStorys, but Hidd's the one who keeps up on my code.\
                           \nAny suggestions or bugs can be promptly disregarded, because my update schedule is horrible. Or just pass them along to Hidden.")

    @commands.command()
    async def discord_tos_official(self, ctx):
        """Disclaimer for discord TOS"""
        await ctx.send("East will in the process of running possibly log your username and log commands that you give "
                       "it. Due to Discord TOS, you must be informed and consent to any storage of data you send here. "
                       "This data will never be publicly shared except at your request, and only used to help run East"
                       " and support features that require it. If you have any questions about this or problems with it"
                       " , please talk to HiddenStorys or CraftSpider for information and we'll see what we can do to "
                       "help")

    @commands.command()
    async def tos_civilian (self, ctx):
        """Returns East version."""
        await ctx.send("Hey, just so you know, in the process of running I might log your guys' usernames and commands. You have to be informed about this because of Discord TOS. I'll never share your stuff publicly, and your information will only be used to help run me! If you have any questions, send them to Hiddenstorys and he'll see what he can do to help!")

    @commands.command()
    async def version(self, ctx):
        """Returns East version."""
        await ctx.send("Version: {0}".format(self.bot.VERSION))

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.lower().split('d'))
        except ValueError:
            await ctx.send('I can\'t read that. Could you put it in NdN?')
            return
        try:
            result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
        except ValueError:
            await ctx.send("Can't go any lower than 1, sorry.")
            return
        if result is "":
            await ctx.send("Can't go any lower than 1, sorry.")
            return
        await ctx.send(result)
       
    @commands.command()
    async def BEWARE(self, ctx):
    	"""A gag command"""
    	await ctx.send("BEWARE the Box Ghost! http://vignette1.wikia.nocookie.net/dpwikia/images/4/44/S01e03_Box_Ghost_arms_wide.png") 


    @commands.command(description='For when you wanna settle the score some other way',
                      usage="[choice 1], [choice 2], ...")
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        choices = " ".join(choices)
        if "," not in choices:
            await ctx.send("Come on, we both know that to make a decision you need *two* things to pick between.")
            return
        out = "You're asking me to choose between: {}.\n".format(choices)
        if random.randint(1, 5) == 1:
            out += "I'm not really feeling like making a decision right now."
        elif random.randint(1, 5) == 500:
            out += "You should just go with everything. Trust me, I know what I'm doing."
        else:
            choices = choices.split(",")
            out += random.choice(choices).strip()
        await ctx.send(out)

    @commands.command()
    async def time(self, ctx):
        """Prints out the current time in UTC, HH:MM:SS format"""
        await ctx.send("Why do you keep asking me what time it is? {0}".format(datetime.datetime.utcnow().strftime("%H:%M:%S")))
    
    @commands.command(name="could", hidden=True)
    async def Could(self, ctx, *extra):
        if str(ctx.author) == "Talos#1108" and extra[1] == "ask":
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send("Only if you tear through mine, first ;)")
            return
        await ctx.send("Excuse me?")

    @commands.command()
    async def magicShow(self, ctx): 
    	await ctx.send("ABRACADABRA!")

    @commands.command()
    async def sexyMagicShow(self, ctx):
    	await ctx.send("Abraca*damn*")

    @commands.command(aliases=["ww", "WW"])
    async def wordwar(self, ctx, length: str="", start: str=""):
        """Runs an X minute long word-war"""
        try:
            length = float(length)
        except Exception:
            await ctx.send("How many minutes do you wanna go?")
            return
        if length > 60 or length < 1:
            await ctx.send("Hey, please give me a number between 1 and 60.")
            return

        if start:
            try:
                if start[0] == ":":
                    start = int(start[1:])
                elif start[0].isnumeric():
                    start = int(start)
                else:
                    raise Exception
            except Exception:
                await ctx.send("Start time format broken. Starting now.")
                start = ""
            if start != "" and (start > 59 or start < 0):
                await ctx.send("Could I have a start time between 0 to 59?")
                return

        if start:
            dif = abs(datetime.datetime.utcnow() - datetime.datetime.utcnow().replace(minute=start, second=0))
            await ctx.send("The ww is going at :{0:02}".format(start))
            await asyncio.sleep(dif.total_seconds())
        minutes = "minutes" if length != 1 else "minute"
        await ctx.send("Word War for {0:g} {1}.".format(length, minutes))
        await asyncio.sleep(length * 60)
        await ctx.send("Word War Over")

    @commands.command()
    async def credits(self, ctx):
        """Giving credit where it is due"""
        await ctx.send("Primary Developers: CraftSpider, HiddenStorys, Dino.\n"
                       "Other contributors: Wundrweapon")
    
    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined the party at {0.joined_at}'.format(member))
    
    @commands.command()
    async def uptime(self, ctx):
        """To figure out how long the bot has been online."""
        pass
    
    @commands.group()
    async def generate(self, ctx):
        """Generates a crawl or shit post"""
        if ctx.invoked_subcommand is None:
            await ctx.send("You can only use 'shitPost' or 'crawl'.")
    
    @generate.command(name='crawl')
    async def _crawl(self, ctx):
        """Generates a crawl"""
        place_adj = random.choice(self.place_adjective)
        place = random.choice(self.place)
        words = str(random.randint(50, 1000))
        action = random.choice(self.action)
        await ctx.send("You enter the {} {}. Write {} words as you {}.".format(place_adj, place, words, action))
    
    @generate.command(name='shitPost')
    async def _shitPost(self, ctx):
        """Generates a prompt"""
        adj = random.choice(self.adjective)
        noun = random.choice(self.noun)
        goal = random.choice(self.goal)
        obstacle = random.choice(self.obstacle)
        await ctx.send("Do not trust a {} who can {} and still be {}.".format(noun, goal, obstacle))

    @commands.command()
    async def hello(self, ctx):
    	await ctx.send("Hiya!");

    @commands.command()
    async def hi(self, ctx):
    	await ctx.send("Hiya!")

    
    @commands.command()
    async def promote(self, ctx):
    	"""Gives a list of stories and art."""
    	await ctx.send("What's that? You want to hear about the writing that's been going on around the chat? Well boy do I have news for you! \n First, we've got some awesome drawings from Q: https://pre07.deviantart.net/0777/th/pre/i/2017/223/8/5/commissions__open___4_4__by_benzyon-db0zsgf.jpg")
    	await ctx.send("and then there's 'Am I Not Just' by Hidden! https://www.wattpad.com/story/118988403-am-i-not-just") 
    	await ctx.send("If you'd like your work featured on this list, feel free to send it in to Hiddenstorys! I'd really like to see some new writers up here.")	
    	await ctx.send("Thanks for listening! Check back later, and there might be something new up.")

    @commands.command()
    async def Hamilton(self, ctx):
    	"""Spews out some Hamilton"""
    	await ctx.send("[BURR] After the war I went back to New York\n[HAMILTON] A-After the war I went back to New York\n[BURR] I finished up my studies and I practiced law\n[HAMILTON] I practiced law, Burr worked next door\n[BURR] Even though we started at the very same time Alexander Hamilton began to climb How to account for his rise to the top?")

    @commands.command()
    async def PrincessBride(self, ctx):
    	await ctx.send("Hello. My name is Inigo Montoya. You killed my father. Prepare to die.")

    @commands.command()
    async def oh_my(self, ctx):
    	await ctx.send("^Hi there...")
    	await asyncio.sleep(2)
    	await ctx.send("How do I say this without sounding weird?")
    	await ctx.send("You have very nice programming, Talos.")

    @commands.command()
    async def reminders(self, ctx):
    	if self.iggy == 0:
    		while True:
    			self.iggy = 1
    			await ctx.send("Have you had anything to drink recently?")
    			await asyncio.sleep(3600)
    			await ctx.send("When's the last time you ate anything?")
    			await asyncio.sleep(3600)
    			await ctx.send("If you're writing, stretch your wrists!")
    			await asyncio.sleep(3600)
    			await ctx.send("Hey, stretch your legs and walk around for a minute.")
    			await asyncio.sleep(3600)
    			await ctx.send("When's the last time you were outside?")
    			await asyncio.sleep(3600)

    	else:
    		await ctx.send("This command is already running.")

  
    @commands.group(aliases=["pw", "PW"])
    async def productivitywar(self, ctx):
        """Commands for a productivity war."""
        if ctx.invoked_subcommand is None:
            await ctx.send("You can either 'create', 'join', 'start', 'leave', or 'end' a pw!")


    @productivitywar.command(name='create')
    async def _create(self, ctx):
        """Begins a new PW, if one isn't already running."""
        if active_pw[ctx.guild.id] is not None:
            await ctx.send("There's already a PW going on, and I can't double up. Would you like to **join**?")
        else:
            await ctx.send("Hey, I'm starting a new PW!")
            active_pw[ctx.guild.id] = PW()
            active_pw[ctx.guild.id].join(ctx.author)

    @productivitywar.command(name='join')
    async def _join(self, ctx):
        """Join a currently running PW, if you aren't already in it."""
        if active_pw[ctx.guild.id] is not None:
            if active_pw[ctx.guild.id].join(ctx.author):
                await ctx.send("User {} finally thought to join us.".format(ctx.author))
            else:
                await ctx.send("You're already here, and you can't join twice.")
        else:
            await ctx.send("You can't join something that doesn't exist. You should **create** a pw!")

    @productivitywar.command(name='start')
    async def _start(self, ctx):
        """Start a PW that isn't yet begun."""
        if active_pw[ctx.guild.id] is not None:
            if not active_pw[ctx.guild.id].get_started():
                await ctx.send("Starting PW")
                active_pw[ctx.guild.id].begin()
            else:
                await ctx.send("There's already a pw going on, keep up! Want to **join**?")
        else:
            await ctx.send("You can't start a pw that doesn't exist. Maybe you want to **create** one?")

    @productivitywar.command(name='leave')
    async def _leave(self, ctx):
        """End your involvement in a PW, if you're the last person, the whole thing ends."""
        if active_pw[ctx.guild.id] is not None:
            leave = active_pw[ctx.guild.id].leave(ctx.author)
            if leave == 0:
                await ctx.send("User {} left the PW and all of us.".format(ctx.author))
            elif leave == 1:
                await ctx.send("You aren't in the PW! You should come and **join** the fun.")
            elif leave == 2:
                await ctx.send("You've already left the PW! Do you want to **end** it?")
            if active_pw[ctx.guild.id].get_finished():
                await self._end.invoke(ctx)
        else:
            await ctx.send("There isn't a pw to leave. It just doesn't exist. Maybe you should try to **create** one?")

    @productivitywar.command(name='end')
    async def _end(self, ctx):
        """End the whole PW, if one is currently running."""
        if active_pw[ctx.guild.id] is None:
            await ctx.send("There's currently no PW going on, but you *could* **create** one.")
        elif not active_pw[ctx.guild.id].get_started():
            await ctx.send("Deleting un-started PW. Really, if you weren't going to use it why make it in the first place?")
            active_pw[ctx.guild.id] = None
        else:
            await ctx.send("Ending the PW, because you guys can't do anything for yourselves.")
            active_pw[ctx.guild.id].finish()
            cur_pw = active_pw[ctx.guild.id]
            out = "```"
            out += "Start: {}\n".format(cur_pw.start.replace(microsecond=0).strftime("%b %d - %H:%M:%S"))
            out += "End: {}\n".format(cur_pw.end.replace(microsecond=0).strftime("%b %d - %H:%M:%S"))
            out += "Total: {}\n".format(cur_pw.end.replace(microsecond=0) - cur_pw.start.replace(microsecond=0))
            out += "Times:\n    East - ∞ \n"
            cur_pw.members.sort(key=sort_mem, reverse=True)
            for member in cur_pw.members:
                out += "    {0} - {1}\n".format(member.user, member.end.replace(microsecond=0) - member.start.replace(microsecond=0))
            out += "```"
            await ctx.send(out)
            active_pw[ctx.guild.id] = None

    @productivitywar.command(name='dump', hidden=True)
    async def _dump(self, ctx):
        """Dumps info about the current state of a running PW"""
        cur_pw = active_pw[ctx.guild.id]
        if cur_pw is None:
            await ctx.send("All of the PWs running are in an alternate dimension. Maybe you should try making one in *this* dimension.")
            return
        out = "```"
        out += "Start: {}\n".format(cur_pw.start)
        out += "End: {}\n".format(cur_pw.end)
        out += "Members:\n"
        for member in cur_pw.members:
            out += "    {0} - {1} - {2}\n".format(member, member.start, member.end)
        out += "```"
        await ctx.send(out)


class PW:

    __slots__ = ['start', 'end', 'members']

    def __init__(self):
        """Creates a PW object, with empty variables."""
        self.start = None
        self.end = None
        self.members = []

    def get_started(self):
        """Gets whether the PW is started"""
        return self.start is not None

    def get_finished(self):
        """Gets whether the PW is ended"""
        return self.end is not None

    def begin(self):
        """Starts the PW, assumes it isn't started"""
        self.start = datetime.datetime.utcnow()
        for member in self.members:
            if not member.get_started():
                member.begin(self.start)

    def finish(self):
        """Ends the PW, assumes it isn't ended"""
        self.end = datetime.datetime.utcnow()
        for member in self.members:
            if not member.get_finished():
                member.finish(self.end)

    def join(self, member):
        """Have a new member join the PW."""
        if PW_Member(member) not in self.members:
            new_mem = PW_Member(member)
            if self.get_started():
                new_mem.begin(datetime.datetime.utcnow())
            self.members.append(new_mem)
            return True
        else:
            return False

    def leave(self, member):
        """Have a member in the PW leave the PW."""
        if PW_Member(member) in self.members:
            for user in self.members:
                if user == PW_Member(member):
                    if user.get_finished():
                        return 2
                    else:
                        user.finish(datetime.datetime.utcnow())
            for user in self.members:
                if not user.get_finished():
                    return 0
            self.finish()
            return 0
        else:
            return 1


class PW_Member:

    __slots__ = ['user', 'start', 'end']

    def __init__(self, user):
        self.user = user
        self.start = None
        self.end = None

    def __str__(self):
        return str(self.user)

    def __eq__(self, other):
        return isinstance(other, PW_Member) and self.user == other.user

    def get_len(self):
        if self.end is None:
            return -1
        else:
            return self.start - self.end

    def get_started(self):
        return self.start is not None

    def get_finished(self):
        return self.end is not None

    def begin(self, time):
        self.start = time

    def finish(self, time):
        self.end = time


def setup(bot):
    bot.add_cog(Commands(bot))
