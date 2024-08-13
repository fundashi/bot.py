import discord
from discord.ext import commands
import math

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calculadora(ctx, operacion="",num1=0,num2=0):
    if operacion =="suma":
        resultado = num1+num2
        await(f"la suma de {num1} mas {num2} es: {resultado}")
    elif operacion =="resta":
        resultado = num1-num2
        await(f"la resta de {num1} menos {num2} es: {resultado}")
    elif operacion =="multiplicacion":
        resultado = num1*num2
        await(f"la multiplicacion de {num1} por {num2} es: {resultado}")
    elif operacion =="division":
        if num2 !=0:
            resultado = num1/num2
            await(f"la division entre {num1} y {num2} es: {resultado}")
        else:
            await("la division entre 0 es imposible, ve a aprender matematicas")
    elif operacion =="potencia":
        resultado = num2 ** (1/num1)
        await(f"la raiz de{num2} en raiz {num1} es: {resultado}")
    else:
        await("operaciones no reconocidas")


bot.run("tu token secreto va aqui")
