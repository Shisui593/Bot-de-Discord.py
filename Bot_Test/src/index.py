import discord
from discord.ext import commands
import asyncio

import datetime
import config

intents = discord.Intents.all()
intents.members = True
intents.messages = True

    #Defines cual será el prefijo para el bot y este ejecute los comandos que tiene en el código.Description es solo 
    #para describir al bot no es indispensable este parámetro
bot = commands.Bot(command_prefix='!', intents=intents, description="Esto es un bot de ayuda.")

    # Comando de ping y pong. el comando de print es uno de depuracion para verificar si se esta ejecuntando correctamente.

    #Comando para anunciar que comandos nomas tiene el bot.
@bot.command()
async def comandos(ctx):
    await ctx.send("El bot tiene los siguientes comandos: `suma, hora, ping`")
    await asyncio.sleep(2)
    await ctx.send(f"(Recuerda siempre usar el prefijo '!' antes del comando.)")
    print("Informacion de comandos ejecutado.")

    #Comando de Ping
@bot.command()
async def ping(ctx):
        await ctx.send("pong 🏓")
        print("Comando 'ping' ejecutado correctamente.")

    #Comando simple de suma donde se pode 2 números enteros y se envia la suma de ambos
@bot.command()
async def suma(ctx, cifraUno=None, cifraDos=None):
    if cifraUno is None or cifraDos is None:
        await ctx.send("Por favor ingresa dos números enteros para poder sumar")
        await asyncio.sleep(2)
        await ctx.send("Ejemplo: `!suma 2 2`")
    try:
        Num1 = int(cifraUno)
        Num2 = int(cifraDos)
        resultado = Num1 + Num2
        await ctx.send(f"La suma de {Num1} y {Num2} es: {resultado}")
        print("Suma realizada.")
    except ValueError:
        await ctx.send("Por favor, asegurate de ingresar núemeros enteros válidos.")

    #Comando !info para que el bot me de la hora con color personalizado, cuando se creo el servidor, el owner del mismo, la región y 
    #el UID del servidor además de enviarlo con el icono que tenga el servidor.
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Esta es la información que puedo proveer:", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado el:", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor:", value=f"{ctx.guild.owner}")
    #embed.add_field(name="Región del servidor:", value=str(ctx.guild.region), inline=False) #El parámetro inline en el método add_field() de un embed de Discord controla si el campo se mostrará en línea o en una nueva línea en el mensaje incrustado.
    embed.add_field(name="UID del servidor:", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)
    print("Comando de infomación ejecutado.")
    
    #Comando donde el bot copia lo solicitado en consola para mandarlo en un canal específico


    #Evento que cuando el bot ya esté en línea nos lo imprima en consola, tambien se podría considerar el print de aquí
    #como un comando de depuración por que estamos corroborando que el bot está ejecutandoce.
    #EL change_presence nos ayudará a ponerle un estado al bot ya sea de "En línea, Ausente, No molestar o Personalizado" y para
    #el streaming solamente funcionara con url de Twitch.
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Shisui", url="https://www.twitch.tv/shisui_593"))
    print(f'Conectado como {bot.user.name}')

    #Token del bot que es necesario para poder comunicarce con Discord, esta guardado en un archivo de configuración
    #para mayor seguridad.  Separas la configuración sensible del código fuente principal, lo que hace que tu bot sea más seguro y fácil de mantener.
bot.run(config.token_discord)