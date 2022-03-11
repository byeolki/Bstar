from email import message
import numbers
from posixpath import split
from tkinter import N
from turtle import color
from discord import Intents
from nextcord.ext import commands
import nextcord, asyncio, datetime, pytz, random, datetime, openpyxl, time
import requests
import textwrap
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View

bot = commands.Bot(command_prefix="ㅂ", Intents=Intents)
TOKEN = "OTI3MDg0MjM0MDIyMjAzNDAz.YdFEeQ.f1XOTwFYzJbTujKojvhR1wilYLw"


@bot.event
async def on_ready():
    guild_list = bot.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {} / 멤버 수: {}".format(i.id, i.name, i.member_count))
    print(f"{bot.user.name}봇은 준비가 완료 되었습니다.")
    print(f"[!] 참가 중인 서버 : {len(bot.guilds)}개의 서버에 참여 중")
    await bot.change_presence(activity=nextcord.Streaming(name='14개에 서버에서 359명과 함께하는', url='https://www.twitch.tv/your_channel_here'))

 #------------------------------------------------------------------

@bot.command()
async def 따라하기(message, text):
    await message.reply(text)

@bot.command(name="hellothisisverification")
async def on_message(message):
    message.reply("! 별키#8761")


@bot.command()
async def 검색(message, text):
    admin = Button(label="유튜브", url=f"https://www.youtube.com/results?search_query={text}", style=ButtonStyle.red)
    game = Button(label="네이버", url=f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={text}", style=ButtonStyle.green)
    gam = Button(label="구글", url=f"https://www.google.com/search?q={text}&sxsrf=APq-WBuUPgZN9d0e7AJqc1YDu4_dOMNbkw%3A1646784637370&source=hp&ei=ffAnYoPpE4vg2roP7N-IyAw&iflsig=AHkkrS4AAAAAYif-jY_f9IJKbfKFBWUfQ0L42okXB_XJ&ved=0ahUKEwjDm9Hq3rf2AhULsFYBHewvAskQ4dUDCAk&uact=5&oq=%E3%85%87&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyCgguEMcBENEDECcyCwgAEIAEELEDEIMBMgsILhCABBCxAxCDATILCAAQgAQQsQMQgwEyCwguEIAEELEDEIMBMgsILhCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBUABYAGDpF2gAcAB4AIABaYgBaZIBAzAuMZgBAKABAQ&sbot=gws-wiz", style=ButtonStyle.blurple)
    g = Button(label="다음", url=f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={text}")
    ga = Button(label="파파고", url=f"https://papago.naver.com/?sk=ko&tk=en&st={text}")
    myview = View()
    myview.add_item(admin)
    myview.add_item(game)
    myview.add_item(gam)
    myview.add_item(g)
    myview.add_item(ga)
    embed = nextcord.Embed(title=f"{text}에 검색 결과",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"필독!", value=f"```사이트별로 검색결과를 버튼형식으로 넣었습니다!```", inline=False)
    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950910400579399711/cat-looking.gif")
    await message.reply(embed=embed, view=myview)


@bot.command(name="핑")
async def pingcmd(message):
    la = bot.latency
    embed = nextcord.Embed(title=f"퐁🏓! 현재 핑을 알려드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"핑", value=f"\n```{str(round(la * 1000))}ms```", inline=False)
    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950910400789090424/cat-ping.gif")
    await message.reply(embed=embed)



@bot.command(name="도움말")
async def on_message(message):
    admin = Button(label="📊관리명령어", style=ButtonStyle.blurple)
    game = Button(label="🎮게임명령어", style=ButtonStyle.blurple)
    myview = View()
    myview.add_item(admin)
    myview.add_item(game)
    embed = nextcord.Embed(title="비스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name="비스타 관리명령어", value="```관리명령어 버튼을 누르시면 관리명령어 목록이 나옵니다!\n게임명령어 버튼을 누르시면 게임명령어 목록이 나옵니다!```", inline=False)
    embed.add_field(name="비스타 서포터 서버", value="```https://discord.gg/Gcrpy4DsX7```", inline=True)
    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    await message.reply(embed=embed, view=myview)

    async def admin_callback(interaction):
            embed = nextcord.Embed(title="비스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name="ㅂ정보", value="```ㅂ정보 명령으로 나에 정보 확인이 가능합니다!```", inline=False)
            embed.add_field(name="ㅂ핑", value="```ㅂ핑 명령으로 현재 핑을 확인하실 수 있습니다!```", inline=False)
            embed.add_field(name="ㅂ검색", value="```ㅂ검색 (검색할 단어) 명령으로 사이트별로 검색결과를 보실 수 있습니다!```", inline=False)
            embed.add_field(name="ㅂ청소", value="```ㅂ청소 (삭제할 메세지 갯수) 명령으로 특정개수에 메세지를 삭제할 수 있습니다!```", inline=False)
            embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await interaction.response.send_message(embed=embed)

    admin.callback = admin_callback

    async def game_callback(interaction):
            embed = nextcord.Embed(title="비스타의 도움말!", description="아래 링크를 통해 명령어를 훨씬 더 자세히 확인하실 수 있습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name="ㅂ수학", value="```ㅂ수학 명령으로 수학문제를 풀 수 있습니다!```", inline=False)
            embed.add_field(name="ㅂ따라하기", value="```ㅂ따라하기 (따라할 단어) 명령으로 봇이 자기말을 따라하게 할 수 있습니다!```", inline=False)
            embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            await interaction.response.send_message(embed=embed)

    game.callback = game_callback
    
    
    


@bot.command(name="정보")
async def on_message(message):
    user = message.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    embed = nextcord.Embed(title=f"{user.name}의 정보", description="ㅂ도움말을 통해 조금 더 명령어를 알아보세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    
    embed.add_field(name=f"{user.name}의 가입일", value=f"{user.name}의 가입일은 {date.year}/{date.month}/{date.day}", inline=False)
    embed.add_field(name=f"{user.name}의 자세한 정보", value=f"{user.name} / {user.id} / {user.display_name}", inline=False)
    
    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    await message.reply (embed=embed)
    
@bot.command(name="수학")
async def check(message):
    a = random.randrange(1,9)
    b = random.randrange(1,9)
    c = random.randrange(1,9)
    d = random.randrange(1,9)
    e = a*b+c-d
    f = a*a+b*b-c+d
    user = message.author
    embed = nextcord.Embed(title=f"{user.name}님 문제를 푸시겠습니까?", description="ㅂ도움말을 통해 조금 더 명령어를 알아보세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
    embed.add_field(name=f"문제목록", value=f"\n ```1을 입력하면 초등수학 \n2를 입력하면 중등수학이 나옵니다 \n3을 입력하면 문제가 취소됩니다!\nㅂ(답)으로 입력해주세요!```", inline=False)
    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
    await message.reply (embed=embed)

    try:

        def check(m):
            return m.author == message.author

        msg = await bot.wait_for("message", check=check, timeout=30)
        startTime = time.time()

        if msg.content == "ㅂ1":
            embed = nextcord.Embed(title=f"{user.name}님 문제!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"문제", value=f"\n```{a}x{b}+{c}-{d}는? \nㅂ(답)으로 입력해주세요!```", inline=False)
            embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
            await message.reply(embed=embed)
            try:
                msg2 = await bot.wait_for("message", check=check, timeout=15)
                startTime = time.time()

                if msg2.content == f"ㅂ{e}":
                    embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                    embed.add_field(name=f"결과", value=f"\n```정답입니다!😍```", inline=False)
                    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                    await message.reply(embed=embed)

                elif msg2.content != f"ㅂ{e}" and "ㅂ" in msg2.content:
                    embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                    embed.add_field(name=f"결과", value=f"\n```틀렸어요...😥```", inline=False)
                    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                    await message.reply(embed=embed)

            except asyncio.exceptions.TimeoutError:
                embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"문제결과", value=f"\n```시간이 초과되었습니다...😥```", inline=False)
                embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                await message.reply(embed=embed)

        elif msg.content == "ㅂ2":
            embed = nextcord.Embed(title=f"{user.name}님 문제!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
            embed.add_field(name=f"문제", value=f"\n```{a}²+{b}²-{c}+{d}는?\nㅂ(답)으로 입력해주세요!```", inline=False)
            embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
            embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
            await message.reply(embed=embed)
            try:
                def check(m):
                    return m.author == message.author
                
                msg2 = await bot.wait_for("message", check=check, timeout=15)
                startTime = time.time()

                if msg2.content == f"ㅂ{f}":
                    embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                    embed.add_field(name=f"결과", value=f"\n```정답입니다!😍```", inline=False)
                    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                    await message.reply(embed=embed)

                else:
                    embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                    embed.add_field(name=f"결과", value=f"\n```틀렸어요...😥```", inline=False)
                    embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                    await message.reply(embed=embed)

            except asyncio.exceptions.TimeoutError:
                embed = nextcord.Embed(title=f"{user.name}님 문제결과 드릴게요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"문제결과", value=f"\n```시간이 초과되었습니다...😥```", inline=False)
                embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                await message.reply(embed=embed)

        elif msg.content == "ㅂ3":
                embed = nextcord.Embed(title=f"{user.name}님 문제가 취소되었어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"문제취소 사유", value=f"\n```문제 취소 명령 입력```", inline=False)
                embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                await message.reply(embed=embed)

        else:
                embed = nextcord.Embed(title=f"{user.name}님 문제가 취소되었어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"문제취소 사유", value=f"\n```올바르지 않은 값 입력```", inline=False)
                embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                await message.reply(embed=embed)

    except asyncio.exceptions.TimeoutError:
                embed = nextcord.Embed(title=f"{user.name}님 문제가 취소되었어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                embed.add_field(name=f"문제취소 사유", value=f"\n```시간내에 답장을 안함```", inline=False)
                embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
                embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950364697528524800/bts-bangtan-boys.gif")
                await message.reply(embed=embed)

@bot.command(name="청소")
async def clear(ctx, amount=5):
    amount = amount+1
    if amount > 101:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 청소가 취소되었어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"청소취소 사유", value=f"\n```100이상에 값을 입력함```", inline=False)
        embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.reply(embed=embed)
    else:
        embed = nextcord.Embed(title=f"{ctx.author.name}님 청소가 완료되었어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')))
        embed.add_field(name=f"삭제된 메세지", value=f"\n```{amount-1}개에 메세지가 삭제됨```", inline=False)
        embed.set_footer(text="Bot Made by. ! 별키#8761", icon_url="https://cdn.discordapp.com/attachments/908521972961534048/939901431572471828/e400a179bf6faa13.jpg")
        embed.set_image(url="https://cdn.discordapp.com/attachments/949216095091454002/950917773347942420/vacuum-hoover.gif")
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed)



#====================================================================


bot.run(TOKEN)