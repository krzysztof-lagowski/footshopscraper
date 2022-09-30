import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook,DiscordEmbed
import discord

DiscordToken = "INSERT HERE"
WebhookDiscord="INSERT HERE"

client = discord.Client()

print("Scraper running...")
@client.event
async def on_message(message):
    if message.content.startswith('!scrape'):
        a = message.content
        footshopid= a.replace("!scrape ","")
        URL= "https://releases.footshop.com/api/raffles/"+str(footshopid)
                
        liste = []
        liste2 = []
        headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')



        site_info= page.json()
      
        title = str(site_info["translations"]["en"]["title"])
              
        for s in site_info['sizeSets']['Men']['sizes']:
            liste.append("EU"+s['eur'])
            liste2.append(str(s['pieces']))
        if liste2== []:
            for s in site_info['sizeSets']['Unisex']['sizes']:
                    liste.append("EU"+s['eur'])
                    liste2.append(str(s['pieces']))
        if liste2== []:
            for s in site_info['sizeSets']['Kids']['sizes']:
                    liste.append("EU"+s['eur'])
                    liste2.append(str(s['pieces']))
        results = map(int, liste2)

        total=str(sum(results))
        if total == "0":
            total = "No stock loaded yet...."
        stock = '\n'.join(liste) #line break bei liste nache jedem komma und string ausgegeben 

        stock2 = '\n'.join(liste2) #line break bei liste nache jedem komma und string ausgegeben 

        URL= "https://releases.footshop.com/Nike-Dunk-Low-Retro-Premium-"+footshopid

        headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        picc= soup.select("img")
        picture= picc[0]["src"]  

        webhook = DiscordWebhook(url=WebhookDiscord)
              
        embed = DiscordEmbed(title=title, description="store: Footshop" , color='e10000')
                     
        embed.set_thumbnail(url=picture)
                 
        embed.set_footer(text='Krzysztof | Footshop Scraper', icon_url='https://static.aklamio.com/promotions/images/80fe76c6c87f46f645363cc7a65d8021c074c7c8/mobile/Footshop_Logo_NEU.png')
                      
        embed.set_timestamp()
     
        embed.add_embed_field(name="Sizes", value="```"'\n'+stock+"```")
        embed.add_embed_field(name="Stock", value="```"'\n'+stock2+'\n'+"Total:"+total+"```")
    
        webhook.add_embed(embed)
        response = webhook.execute()
        print("Scraped!")
          
client.run(DiscordToken)