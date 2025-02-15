import discord
import os
import random
import requests
from discord.ext import commands
from settings import settings



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    await ctx.send(f'EScribe $info, para decirte algunas de mis funciones')

@bot.command()
async def info(ctx):
    await ctx.send(f'Te contaré algunos detalles para que sepas que onda')
    await ctx.send(f'heh, add, roll, mem, mem1, mem2, mem3, duck, dog, zorro, poke + (nombredelpokemon), API')
    await ctx.send(f'Diviertete, y aprende con cada uno de ellos')
    await ctx.send(f'Recueda poner siempre el prefijo $')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def guess(ctx, number: int):
    """Guess a random number from 1 to 6."""
    # explained in a previous example, this gives you
    # a random number from 1-6
    value = random.randint(1, 6)
    # with your new helper function, you can add a
    # green check mark if the guess was correct,
    # or a red cross mark if it wasn't
    await ctx.tick(number == value)

@bot.command()
async def mem(ctx):
    with open('Images/meme1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def mem1(ctx):
    memes = os.listdir('Images')
    with open(f'Images/{random.choice(memes)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    momos = os.listdir('Animales')
    with open(f'Animales/{random.choice(momos)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    momazos = os.listdir('Carros')
    with open(f'Carros/{random.choice(momazos)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


def get_zorro_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('zorro')
async def zorro(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_zorro_image_url()
    await ctx.send(image_url)


def get_pika_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('pika')
async def pika(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_pika_image_url()
    await ctx.send(image_url)


@bot.command()
async def API(ctx):
    await ctx.send(f"""Hola, soy un bot ayuda {bot.user}!""")# esta linea saluda
    await ctx.send(f'Hablaré acerca de las APIs')
    await ctx.send(f'Son de gran utilidad, cuando se trata de pedir datos a páginas web')
    await ctx.send(f'E implementar esos datos en aplicaciones nuestras, o dinámicas')
    # Enviar una pregunta al usuario
    await ctx.send("Quieres saber más acerca de este tema? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("Quiere descir Application Programming Interface.")
            await ctx.send("Esto nos ayudará a conectarnos a aplicaciones externas, y pedir datos.")
            await ctx.send("La forma en que nos comunicamos con otras aplicaciones, y hacemos solicitudes.")   
        else:
            await ctx.send("Está bien, si lo necesitas en alguna ocasión, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo, con sí, si, o no")
    await ctx.send("Si quieres expandir aún más tu saber, responde continua")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['continua']:
            await ctx.send("Hacemos solicitudes a través de estas, para que un servidor nos responda con los datos que solicitamos.")
            await ctx.send("Es como pedirle a un mesero (API), algo del menú (datos), para que passe el pedido a la cocina (servidor), y no responda trayendo nuestra comida (datos).") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas el dato, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Ahora te gustaría ver un ejemplo de esto!! responde con un claro")
    response2 = await bot.wait_for('message', check=check)
    if response2:
        if response2.content in ['claro']:
            await ctx.send("Nosotros pedimos en formato <requests>, y nos los regresa en formato <json>.")
            await ctx.send("Tambien están los status code, como le fue a nuestra solicitud, 404 es que no se encontró, 500 es que el servidor no lo procesó, etc.")
            await ctx.send("Un ejemplo es la siguiente página: ")

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")



bot.run(settings['TOKEN'])
 