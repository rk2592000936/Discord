import requests
import json
import discord
client = discord.Client()
bot_token = 'r46wPsN9Batu_nfoxRjL8LuEe78qyTHb'

@client.event
async def on_ready():
    print('du price bot')
    print('login as %s' % client.user.name)
    print('Client Id:%s' % client.user.id)
    await client.change_presence(status=discord.Status.idle)

@client.event
async def on_message(message):
    if message.content.startswith('!du'):
        kw = message.content.split(" ")[1]
        prices = []
        headers = {
            'tk': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDgwYTc2ZmY4ODNkOGUwYmYwOGE2ZDAiLCJpYXQiOjE1NzA3OTQ3MTZ9.58xagM7WfoItwpTkg-Q4PHnb09Vl5Z7zVnW0ErWVLRs',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        base_url = 'https://du.duoerpu.com/api/du/api/search?title='+kw+'&page=0&limit=20&sortType=0&sortMode=1&unionId='
        response1 = requests.get(base_url, headers=headers)
        response1_dic1 = json.loads(response1.text) #转换成python字典
        response1_dic2 = json.loads(response1_dic1['data']) #将data值转为字典
        product_id = response1_dic2['data']['productList'][0]['productId']# 获取商品id
        product_url = 'https://du.duoerpu.com/api/du/api/detail?productId='+str(product_id)+'&productSourceName=wx' #查询的商品页面
        response2 = requests.get(product_url,headers=headers)
        response2_dic1 = json.loads(response2.text)
        response2_dic2 = json.loads(response2_dic1['data'])
        size_list = response2_dic2['data']['sizeList'] # 获取尺码列表,以及各个码数对应的信息
        for size in size_list:
            if len(str(size['item']['price'])) > 5:
                prices.append(size['size']+'-'+str(size['item']['price']).replace('00', ''))
            else:
                prices.append(size['size']+'-'+str(size['item']['price']))
        description = response2_dic2['data']['detail']['title']
        embed = discord.Embed(title='毒价格'+str(description),description = 'test', color=0x36393F)
        embed.add_field(name='价格',value='\n'.join(prices),inline=True)
        sum = response2_dic2['data']['detail']['soldNum']
        embed.add_field(name='销售量', value=sum)
        picture = response2_dic2['data']['detail']['logoUrl']
        embed.set_thumbnail(url=picture)
        embed.set_author(name='@巴啦啦拉粑粑')
        embed.set_footer(text='@TestNotify')
        await message.channel.send(embed=embed)
client.run(bot_token)
