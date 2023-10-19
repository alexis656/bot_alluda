import discord
from discord.ext import commands
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot que te informara sobre el tema del cuidado del medio ambiente y como esta afectando la contaminacion al mundo {bot.user}!')

@bot.command()
async def informame(ctx):
    await ctx.send(f'El cuidado del medio ambiente es un tema importante en la actualidad. La humanidad ha causado muchos problemas ambientales, como la deforestación, la explotación irracional de los recursos naturales, el consumo insostenible, la contaminación y otros impactos que han debilitado la atmósfera y la biodiversidad{bot.user}!')

@bot.command()
async def como_ayudo(ctx):
    await ctx.send(f'como podemos ayudar al cambio:Para ayudar a reducir la contaminación, se pueden hacer los siguientes cambios en la vida diaria:',
                   '1.Disminuir al máximo el uso del automóvil y la motocicleta; preferir caminar, usar bicicleta o el transporte público',
                   '.2.Elegir productos con menor contenido de compuestos orgánicos volátiles y reducir las fugas de gas LP.',
                   '3.Emplear el agua y la energía de manera racional y eficiente.',
                   '4.No tirar basura en las calles, evitar quemar basura, hojas y otros objetos, así como hacer fogatas en bosques o en plena ciudad.',
                   '5.Reutilizar el agua que juntaste de la regadera y de lavar las verduras para regar las plantas o el jardín.',
                   '6.Recoger, separar y eliminar los residuos de forma segura para proteger la tierra y el agua, fomentar la reducción de sustancias nocivas para el medio ambiente y fomentar el reciclaje por parte de los ciudadanos y las empresas. {bot.user}!')

@bot.command()
async def tips(ctx):
    tips = [
        "Recuerda separar tus residuos en orgánicos e inorgánicos para facilitar su reciclaje.",
        "Evita utilizar plásticos de un solo uso, opta por alternativas reutilizables.",
        "Antes de desechar, ¡piensa si puedes reutilizar!",
        "Compostar tus residuos orgánicos es una excelente manera de reciclar y ayudar al medio ambiente.",
        # ... [Añadir más tips según tu preferencia]
    ]
    await ctx.send(random.choice(tips))



meme_reciclar = ["meme1","meme2","meme3", "meme4","meme5"]

@bot.command()
async def memeresi(ctx):
    img_name = random.choice(meme_reciclar)  # Elige un nombre de archivo al azar
    with open(f'imagen/{img_name}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTE1NTIwMTc5ODI0MDQ4NTUyNg.G7Rfmx.FGitkzFdAhkAFZfpjua36gn87vsnWLReaVKCTg")
