from bs4 import BeautifulSoup
from nextcord.ext import commands
import nextcord, asyncio, datetime, pytz, random, datetime, time, aiosqlite, urllib.request, urllib.parse,requests
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View
from bs4 import BeautifulSoup as bs
    
intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="ㅂ", intents=intents)
TOKEN = "토큰"

#=================================================================

@bot.event
async def on_ready():
    i = datetime.datetime.now()
    print(f"{bot.user.name}봇은 준비가 완료 되었습니다.")
    print(f"[!] 참가 중인 서버 : {len(bot.guilds)}개의 서버에 참여 중")
    print(f"[!] 이용자 수 : {len(bot.users)}와 함께하는 중")
    await bot.change_presence(activity=nextcord.Streaming(name=f'ㅂ도움말|{len(bot.users)}명과 함께', url='https://www.twitch.tv/your_channel_here'))
    print(i)
    

    ch = bot.get_channel(951785065220812820)
    embed = nextcord.Embed(title=f"봇이 켜졌어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"켜진시간", value=f"\n{i}", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400789090424/cat-ping.gif")
    msg = await ch.send(embed=embed)
    await asyncio.sleep(60)
    await msg.delete()  


@bot.event
async def on_guild_join(guild):
    await bot.change_presence(activity=nextcord.Streaming(name=f'ㅂ도움말|{len(bot.users)}명과 함께', url='https://www.twitch.tv/your_channel_here'))

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(activity=nextcord.Streaming(name=f'ㅂ도움말|{len(bot.users)}명과 함께', url='https://www.twitch.tv/your_channel_here'))

@bot.event
async def on_member_join(member):
    await bot.change_presence(activity=nextcord.Streaming(name=f'ㅂ도움말|{len(bot.users)}명과 함께', url='https://www.twitch.tv/your_channel_here'))

@bot.event
async def on_member_remove(member):
    await bot.change_presence(activity=nextcord.Streaming(name=f'ㅂ도움말|{len(bot.users)}명과 함께', url='https://www.twitch.tv/your_channel_here'))

#=================================================================



#=================================================================



#=================================================================

@bot.command()
async def 언밴(ctx):
    if ctx.author.guild_permissions.administrator:
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                pass
        embed = nextcord.Embed(title=f"{ctx.author.name}님 성공적으로 언밴을 완료 했습니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 언밴이 취소되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"언밴취소 사유", value=f"\n관리자가 아님", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.reply(embed=embed)

#=================================================================

@bot.command()
async def 킥(ctx, member:nextcord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.kick()
        embed = nextcord.Embed(title=f"{ctx.author.name}님 성공적으로 킥을 완료 했습니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"대상 정보", value=f"{member}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 킥이 취소되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"킥취소 사유", value=f"\n관리자가 아님", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.reply(embed=embed)

#=================================================================

@bot.command()
async def 밴(ctx, member:nextcord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.ban()
        embed = nextcord.Embed(title=f"{ctx.author.name}님 성공적으로 밴을 완료 했습니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"대상 정보", value=f"{member}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 밴이 취소되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"밴취소 사유", value=f"\n관리자가 아님", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.reply(embed=embed)

#=================================================================



#=================================================================



#=================================================================



#=================================================================

@bot.command(name="주사위")
async def on_message(message):
    i = random.randrange(1,7)
    l = random.randrange(1,7)
    embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲굴리는중...", inline=True)
    embed.add_field(name=f"리스타의 주사위", value=f"대기중", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
    msg = await message.reply(embed=embed)

    await asyncio.sleep(2)

    embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲{i}!!", inline=True)
    embed.add_field(name=f"리스타의 주사위", value=f"🎲굴리는중...", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
    msg2 = await msg.edit(embed=embed)

    await asyncio.sleep(2)

    embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲{i}!!", inline=True)
    embed.add_field(name=f"리스타의 주사위", value=f"🎲{l}!!", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
    msg3 = await msg2.edit(embed=embed)

    if i < l:
        embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲{i}!!", inline=True)
        embed.add_field(name=f"리스타의 주사위", value=f"🎲{l}!!", inline=True)
        embed.add_field(name=f"승자", value=f"🎲{i} < 🎲{l} 이므로 승은 리스타!", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await msg3.edit(embed=embed)

    elif l < i:
        embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲{i}!!", inline=True)
        embed.add_field(name=f"리스타의 주사위", value=f"🎲{l}!!", inline=True)
        embed.add_field(name=f"승자", value=f"🎲{l} < 🎲{i} 이므로 승은 {message.author.name}!", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await msg3.edit(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{message.author.name}님 주사위를 굴릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"{message.author.name}님의 주사위", value=f"🎲{i}!!", inline=True)
        embed.add_field(name=f"리스타의 주사위", value=f"🎲{l}!!", inline=True)
        embed.add_field(name=f"승자", value=f"🎲{l} = 🎲{i} 이므로 무승부...!", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
        await msg3.edit(embed=embed)


#=================================================================



#=================================================================



#=================================================================

@bot.command(name="핑")
async def pingcmd(message):
    la = bot.latency
    embed = nextcord.Embed(title=f"퐁🏓! 현재 핑을 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"핑", value=f"\n{str(round(la * 1000))}ms", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950910400789090424/cat-ping.gif")
    await message.reply(embed=embed)

#=================================================================

@bot.command(name="도움말")
async def on_message(message):
    admin = Button(label="📊관리명령어", style=ButtonStyle.blurple)
    game = Button(label="🎮게임명령어", style=ButtonStyle.blurple)
    gam = Button(label="🕳️잡명령어", style=ButtonStyle.blurple)
    myview = View()
    myview.add_item(admin)
    myview.add_item(game)
    myview.add_item(gam)
    embed = nextcord.Embed(title="리스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name="리스타 관리명령어", value="관리명령어 버튼을 누르시면 관리명령어 목록이 나옵니다!\n게임명령어 버튼을 누르시면 게임명령어 목록이 나옵니다!", inline=True)
    embed.add_field(name="리스타 서포터 서버", value="https://discord.gg/Gcrpy4DsX7", inline=True)
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_thumbnail(url=r"https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    msg = await message.reply(embed=embed, view=myview)

    async def admin_callback(interaction):
            embed = nextcord.Embed(title="리스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name="ㅂ핑", value="ㅂ핑 명령으로 현재 핑을 확인하실 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ청소", value="ㅂ청소 (삭제할 메세지 갯수) 명령으로 특정개수에 메세지를 삭제할 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ채널생성", value="ㅂ채널생성 (채널이름) 명령으로 음성채널과 채팅채널을 생성하실 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ채팅삭제", value="ㅂ채널삭제 (채널ID) 명령으로 채팅채널을 삭제하실 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ음성삭제", value="ㅂ음성삭제 (채널ID) 명령으로 채팅채널을 삭제하실 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ슬로우", value="ㅂ슬로우 (슬로우(초)) 명령으로 메세지를 보낸 채널에 슬로우를 걸 수 있어요!", inline=True)
            embed.add_field(name="ㅂ채널편집", value="ㅂ찬반투표 (채널ID) (바꿀 채널명) 명령을 입력하면 채널을 편집할 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ킥", value="ㅂ킥 (대상을 멘션) 명령으로 해당 대상을 킥을 할 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ밴", value="ㅂ밴 (대상을 멘션) 명령으로 밴을 할 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ언밴", value="ㅂ언밴 명령으로 모든 밴을 풀 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ잠금", value="ㅂ잠금 명령으로 해당 채널에 메세지 보내기 권한을 없앨 수 있습니다!", inline=True)
            embed.add_field(name="ㅂ잠금해제", value="ㅂ잠금해제 명령으로 해당 채널에 메세지 보내기 권한을 풀 수 있습니다!", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_thumbnail(url=r"https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await msg.edit(embed=embed)

    admin.callback = admin_callback

    async def gam_callback(interaction):
        embed = nextcord.Embed(title="리스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name="ㅂ큐알코드", value="ㅂ큐알코드 (링크 또는 말) 명령으로 큐알코드를 생성하실 수 있습니다!", inline=True)
        embed.add_field(name="ㅂbmi", value="ㅂbmi (키) (몸무게) 명령으로 자신의 bmi지수를 확인 할 수 있습니다!", inline=True)
        embed.add_field(name="ㅂ타이머", value="ㅂ타이머 (수) (단위) 타이머를 측정 할 수 있습니다!\n수와 단위 사이 띄어쓰기 하셔야 합니다!", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await msg.edit(embed=embed)

    gam.callback = gam_callback

    async def game_callback(interaction):
            embed = nextcord.Embed(title="리스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name="ㅂ주사위", value="ㅂ주사위 명령으로 봇과 주사위대결을 할 수 있습니다!!", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_thumbnail(url=r"https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await msg.edit(embed=embed)

    game.callback = game_callback
    
#=================================================================



#=================================================================



#=================================================================

@bot.command(name="청소")
async def clear(ctx, amount=5):
    amount = amount+1
    if ctx.author.guild_permissions.administrator:
        if amount > 101:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 청소가 취소되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"청소취소 사유", value=f"\n100이상에 값을 입력함", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
            await ctx.reply(embed=embed)
        else:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 청소가 완료되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"삭제된 메세지", value=f"\n{amount-1}개에 메세지가 삭제됨", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=embed)
    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 청소가 취소되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"청소취소 사유", value=f"\n관리자가 아님", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.nextcordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.reply(embed=embed)

#===================================================================

@bot.command(name="채널생성")
async def on_message(message, text):
    voicech = Button(label="🔊음성채널 생성", style=ButtonStyle.blurple)
    textch = Button(label="⌨️채팅채널 생성", style=ButtonStyle.green)
    myview = View()
    now = datetime.datetime.now()
    guild = message.guild
    myview.add_item(voicech)
    myview.add_item(textch)
    if message.author.guild_permissions.administrator:
        embed = nextcord.Embed(title=f"{message.author.name}님 생성할 채널을 선택해주세요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"선택방법", value=f"\n생성하고 싶은 채널버튼을 누른다", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        msg = await message.reply(embed=embed, view=myview)

        if message.author.guild_permissions.administrator:
            async def voicech_callback(interaction):
                embed = nextcord.Embed(title=f"{message.author.name}님 음성채널이 생성되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"채널 정보", value=f"\n생성 날짜 : {now}\n채널이름 : {text}", inline=True)
                embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                await message.reply(embed=embed)
                await guild.create_voice_channel(f"{text}")
                await msg.delete()

        else:
            embed = nextcord.Embed(title=f"{message.author.name}님 생성을 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await message.reply(embed=embed)

        voicech.callback = voicech_callback

        if message.author.guild_permissions.administrator:
            async def textch_callback(interaction):
                embed = nextcord.Embed(title=f"{message.author.name}님 채팅채널이 생성되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"채널 정보", value=f"\n생성 날짜 : {now}\n채널이름 : {text}", inline=True)
                embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                await message.reply(embed=embed)
                await guild.create_text_channel(f"{text}")
                await msg.delete()

        else:
            embed = nextcord.Embed(title=f"{message.author.name}님 생성을 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await message.reply(embed=embed)

        textch.callback = textch_callback

    else:
        embed = nextcord.Embed(title=f"{message.author.name}님 생성을 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await message.reply(embed=embed)

#====================================================================

@bot.command()
async def 채팅삭제(ctx, channel: nextcord.TextChannel):
    cancle = Button(label="취소", style=ButtonStyle.red)
    textch = Button(label="⌨️진짜 삭제 하시겠습니까?", style=ButtonStyle.green)
    myview = View()
    now = datetime.datetime.now()
    myview.add_item(textch)
    myview.add_item(cancle)
    if ctx.author.guild_permissions.administrator:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 진짜 삭제 하실 건가요?!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"선택방법", value=f"\n채널을 삭제 하시려면 버튼을 눌러주세요", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        msg = await ctx.reply(embed=embed, view=myview)

        if ctx.author.guild_permissions.administrator:
            async def textch_callback(interaction):
                embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"삭제된 채널 정보", value=f"\n삭제 날짜 : {now}\n 채널이름 : {channel}", inline=True)
                embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                await ctx.reply(embed=embed)
                await channel.delete()
                await msg.delete()

        else:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

        textch.callback = textch_callback

        async def cancle_callback(interaction):
                await msg.delete()
        
        cancle.callback = cancle_callback

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)


@bot.command()
async def 음성삭제(ctx, channel: nextcord.VoiceChannel):
    textch = Button(label="⌨️진짜 삭제 하시겠습니까?", style=ButtonStyle.green)
    cancle = Button(label="취소", style=ButtonStyle.red)
    myview = View()
    now = datetime.datetime.now()
    myview.add_item(textch)
    myview.add_item(cancle)
    if ctx.author.guild_permissions.administrator:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 진짜 삭제 하실 건가요?!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"선택방법", value=f"\n채널을 삭제 하시려면 버튼을 눌러주세요", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        msg = await ctx.reply(embed=embed, view=myview)

        if ctx.author.guild_permissions.administrator:
            async def textch_callback(interaction):
                embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제되었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"삭제된 채널 정보", value=f"\n삭제 날짜 : {now}\n 채널이름 : {channel}", inline=True)
                embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                await ctx.reply(embed=embed)
                await channel.delete()
                await msg.delete()

        else:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

        textch.callback = textch_callback

        async def cancle_callback(interaction):
                await msg.delete()
        
        cancle.callback = cancle_callback

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 삭제 할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

#====================================================================

@bot.command()
async def 슬로우(ctx, seconds: int):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 슬로우 모드를 걸었어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"슬로우 시간", value=f"\n{seconds}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 슬로우를 걸 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

#====================================================================



#====================================================================



#====================================================================

@bot.command()
async def 채널편집(ctx, channel: int, text):
    if ctx.author.guild_permissions.administrator:
        ch = bot.get_channel(channel)
        await ch.edit(name=text)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 편집했어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"채널정보", value=f"\nID : {channel}\n새로운 채널명 : {text}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 편집할 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)


#====================================================================

@bot.command()
async def 타이머(ctx, second: int, text):
    if text in "분":
        i = datetime.datetime.now()
        b = second*60
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머를 시작합니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}분 타이머\n시작시간 {i}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)
        await asyncio.sleep(b)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머가 끝났어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}분 타이머", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    if text in "초":
        i = datetime.datetime.now()
        b = second
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머를 시작합니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}초 타이머\n시작시간 {i}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)
        await asyncio.sleep(b)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머가 끝났어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}초 타이머", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    if text in "시간":
        i = datetime.datetime.now()
        b = second*3600
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머를 시작합니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}초 타이머\n시작시간 {i}", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)
        await asyncio.sleep(b)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 타이머가 끝났어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"타이머 정보", value=f"\n{second}초 타이머", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

#====================================================================



#====================================================================

@bot.command()
async def 잠금(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 잠궜습니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 닫을 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

#====================================================================

@bot.command()
async def 잠금해제(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 풀었습니다!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 채널을 열 수 없어요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"사유", value=f"\n관리자가 아니라서", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

#====================================================================

@bot.command()
async def 큐알코드(ctx, *, qrmsg):
    embed = nextcord.Embed(title="QR코드", description="QR코드를 만들고 있습니다...",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    loadingmsg = await ctx.reply(embed=embed)
    qrserver = f"https://api.qrserver.com/v1/create-qr-code/?data={qrmsg}"
    embed = nextcord.Embed(title="QR코드", description="요청하신 QR코드입니다!", color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.set_image(url=f"{qrserver}")
    embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    await loadingmsg.edit(embed=embed)

#====================================================================

@bot.command()
async def bmi(ctx, h: int, w: int):
    h1 = h/100
    h2 = h1*h1
    b = w/h2
    if b <=  18.5:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 bmi지수를 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"BMI", value=f"\nBMI : {b}\n단계 : 저체중", inline=True)
        embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        await ctx.reply(embed=embed)

    elif 22.9 < b <= 24.9:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 bmi지수를 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"BMI", value=f"\nBMI : {b}\n단계 : 정상", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

    elif 24.9 < b <= 29.9:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 bmi지수를 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"BMI", value=f"\nBMI : {b}\n단계 : 초기비만", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

    elif 29.9 < b <=  34.9:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 bmi지수를 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"BMI", value=f"\nBMI : {b}\n단계 : 2단계 비만", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

    elif 34.9 < b:
            embed = nextcord.Embed(title=f"{ctx.author.name}님 bmi지수를 알려드릴게요!",color=0x2f3136,timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"BMI", value=f"\nBMI : {b}\n단계 : 고도비만!", inline=True)
            embed.set_footer(text="Bot Made by. ! 𝓫𝔂𝓮𝓸𝓵𝓴𝓲#8761", icon_url="https://cdn.nextcordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await ctx.reply(embed=embed)

#====================================================================



#====================================================================

bot.run(TOKEN)
