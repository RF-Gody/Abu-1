import discord, os, random, requests
from discord.ext import commands

my_map = ["Leve sacolas reutilizáveis ao mercado.","Separar recicláveis corretamente","Fazer compostagem dos resíduos orgânicos.","Planeje refeições da semana.","Prefira produtos a granel","Escolha embalagens retornáveis ou maiores (geram menos plástico por uso).","Evite itens descartáveis como copos, talheres e guardanapos em excesso.","Congele sobras.","Organize a geladeira para consumir primeiro o que vence antes.","Aproveite partes normalmente descartadas (talos, cascas, folhas).","Substituir descartáveis por reutilizáveis.","Reutilizar antes de jogar fora, já que potes de vidro, caixas e embalagens podem virar: organizadores, vasos, armazenamento de alimentos.","Doar ou vender objetos sem uso.","Comprar produtos duráveis.","Use filtros de café reutilizáveis em vez de descartáveis.","Faça temperos e molhos caseiros para evitar potes e sachês."]

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True

# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def meme(ctx):
    nome_imagem = random.choice(os.listdir('images'))
    with open(f'images/{nome_imagem}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def eco(ctx):
    nome_imagem = random.choice(my_map)
    await ctx.send(nome_imagem)
