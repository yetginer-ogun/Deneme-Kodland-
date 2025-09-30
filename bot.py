import discord
from discord.ext import commands
from config import token  # Botun tokenini config dosyasından içe aktarma
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send("Merhaba! Ben bir sohbet yöneticisi botuyum!")

@bot.command()
async def selam(ctx):
    await ctx.send(f"Merhaba! {ctx.author.mention}!")

@bot.command()
async def secim(ctx, a1, a2):
    sonuc  = random.choice([a1,a2])
    await ctx.send(sonuc)

@bot.command()
async def topla_eski(ctx, sayi1, sayi2):
    sonuc = int(sayi1) + int(sayi2)
    await ctx.send(sonuc)

@bot.command()
async def topla(ctx, *sayi):
    a = 0
    for x in sayi:
        if x.isdigit():
            a += int(x)
    await ctx.send(f"Verdiğiniz sayıların toplamı = {a}")



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    if member:
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Eşit veya daha yüksek rütbeli bir kullanıcıyı banlamak mümkün değildir!")
        else:
            await ctx.guild.ban(member)
            await ctx.send(f"Kullanızı {member.name} banlandı")
    else:
        await ctx.send("Bu komut banlamak istediğiniz kullanıcıyı işaret etmelidir. Örneğin: `!ban @user`")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu çalıştırmak için yeterli izniniz yok.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Kullanıcı bulunamadı!")

bot.run(token)