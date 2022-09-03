import discord
import asyncio
from random import randint
from random import choice

client = discord.Client()

@client.event
async def on_ready():
  async def message(games):
    await client.wait_until_ready() #클라이언트가 준비되었을때
    while not client.is_closed(): #만약 클라이언트가 닫히지 않았을때
        for game in games:
            await client.change_presence(status = discord.Status.dnd, activity = discord.Game(game))
            await asyncio.sleep(10) #몇초마다 바꿀지 결정
  await message(['코사커봇','카이저 바보'])

@client.event
async def on_message(message):
    if message.content.startswith('!말해봐'):
        embed = discord.Embed(title="[ 말하기 ]", description="할말", color=0x00ff00)
        await message.channel.send("할말", embed=embed)

    if message.content.startswith('!인사'):
        embed = discord.Embed(title="[ 인사 ]", description=f"안녕하세요! {message.author.id}님!", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!개발자'):
        if message.author.id == 920296780204236831:
            embed = discord.Embed(title="[ 개발자 ]", description=f"앗 우리 개발자 나오셨다!", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="[ 개발자 ]", description=f"앗 당신은 권한이 없는거 같아요!", color=0x00ff00)
            await message.channel.send(embed=embed)

    if message.content.startswith('!멘션'):
        embed = discord.Embed(title="[ 멘션 ]", description=f"{message.author.mention}님을 멘션해드렸어요!", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!숫자뽑기'):
        number1 = int(message.content.split(" ")[1])
        number2 = int(message.content.split(" ")[2])
        random = randint(number1, number2)
        embed = discord.Embed(title="[ 숫자뽑기 ]", description=f"{random}", color=0x00ff00)
        embed.set_image(url=f"https://dummyimage.com/300x200/ffffff/000000.png&text={random}")
        await message.channel.send(embed=embed)

    if message.content.startswith('!룰렛'):
        roulette = ['🧱', '❤️', '🖼️', '🎁', '🔰']
        random = f"{choice(roulette)} {choice(roulette)} {choice(roulette)}"
        embed = discord.Embed(title="[ 룰렛 ]", description=f"{message.author.mention}님이 뽑은 그림은 {random}입니다!", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.channel.purge(limit=int(amount))
            embed = discord.Embed(title="[ 청소 ]", description=f"메세지 {amount}개가 관리자 {message.author.mention}님이 삭제했습니다!", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="[ 청소 ]", description=f"{message.author.mention}님은 서버의 관리자가 아닙니다!", color=0x00ff00)
            await message.channel.send(embed=embed)

client.run("봇의 토큰값")