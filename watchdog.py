import asyncio
import string
import time

import discord
from discord.ext import commands, tasks
import static
from coinbase.wallet.client import Client

API_KEY = 'API_KEY'
API_SECRET = 'API_SECRET'
client = Client("API_KEY", "API_SECRET", api_version='YYYY-MM-DD')

class Watchdog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timmers = {}
        self.watchdog.start()

    @commands.command(description='check BTC price')
    async def btc(self, ctx, n=1):
        await ctx.message.delete()
        price = client.get_spot_price(currency_pair='BTC-USD')
        embed = discord.Embed(
            title=static.title_btc_price + price["amount"] + "$",
            color=static.color_BTC)
        await ctx.send(embed=embed)

    @commands.command(description='check ETH price')
    async def eth(self, ctx, n=1):
        await ctx.message.delete()
        price = client.get_spot_price(currency_pair='ETH-USD')
        embed = discord.Embed(
            title=static.title_eth_price + price["amount"] + "$",
            color=static.color_eth)
        await ctx.send(embed=embed)

    @commands.command(description='check ETH price')
    async def currencies(self, ctx, n=1):
        await ctx.message.delete()
        embed = discord.Embed(
            title=static.title_currencies,
            # description='Keep track of your points with this embed, it will be updated from time to time',
            colour=static.color_success)
        embed.set_thumbnail(url='https://media.giphy.com/media/YnkMcHgNIMW4Yfmjxr/giphy.gif')
        for currencie in static.currencies:
            print(currencie)
            price = client.get_spot_price(currency_pair=currencie + "-USD")
            embed.add_field(name=currencie, value=price["amount"] + "$")
        await ctx.send(embed=embed)

    @tasks.loop(seconds=1)
    async def watchdog(self):
        temp = {}
        n_timers = len([1 for timmers in self.timmers])
        self.watchdog.change_interval(seconds=int(n_timers / 3) + 1)
        for currencie, timmers in self.timmers.items():
            temp.update({currencie: []})
            price = client.get_spot_price(currency_pair=currencie + "-USD")
            for timmer in timmers:
                print("{} price is now at {}$ ".format(currencie, price["amount"]))
                ctx = timmer["ctx"]
                if timmer["type"] == "down" and float(price["amount"]) < timmer["value"]:
                    embed = discord.Embed(title="This is going nuts",
                                          description="{} price is now at {}$ {} ".format(currencie, price["amount"],
                                                                                          ctx.message.author.mention),
                                          colour=static.color_success)
                    embed.set_thumbnail(url=static.get_url(currencie))
                    await ctx.send(embed=embed)
                    continue
                elif timmer["type"] == "up" and float(price["amount"]) > timmer["value"]:
                    embed = discord.Embed(title="This is going nuts",
                                          description="{} price is now at {}$ {} ".format(currencie, price["amount"],
                                                                                          ctx.message.author.mention),
                                          colour=static.color_success)
                    embed.set_thumbnail(url=static.get_url(currencie))
                    await ctx.send(embed=embed)
                    continue
                temp[currencie].append(timmer)
        self.timmers = temp

    @commands.command(description='Show timmers in use')
    async def show_timmers(self, ctx):
        embed = discord.Embed(
            title="This is all the timmers",
            colour=static.color_legendary)
        await ctx.send(embed=embed)

        for currencie, timmers in self.timmers.items():
            embed = discord.Embed(
                title=currencie,
                colour=static.color_legendary)
            for i, timmer in enumerate(timmers):
                embed.add_field(name=i, value="{} {} {}".format(currencie, timmer["type"], timmer["value"]))
            embed.set_thumbnail(url=static.get_url(currencie))
            await ctx.send(embed=embed)

    @commands.command(description='Show timmers in use')
    async def del_timmer(self, ctx,name,id):
        temp = {}
        name = name.upper()
        for currencie, timmers in self.timmers.items():
            if currencie == name:
                for i, timmer in enumerate(timmers):
                    if i != int(id):
                        if not currencie in temp.keys():
                            temp.update({currencie: []})
                        temp[currencie].append(timmer)
            else:
                temp.update({currencie: timmers})
        self.timmers = temp
        await self.show_timmers(ctx)

    @commands.command(description='Insert Watchdog timer currencie,type,value',brief="currencie ,value")
    async def trigger(self, ctx, currencie, value):
        # await ctx.message.delete()
        currencie = currencie.upper()
        value = int(value.replace(",", "."))
        # add timmer to timmers
        price = client.get_spot_price(currency_pair=currencie + "-USD")
        p = float(price["amount"])
        if value > p:
            type = "up"
        elif value < p:
            type = "down"
        if not currencie in self.timmers.keys():
            self.timmers.update({currencie: []})
        self.timmers[currencie].append({"type": type, "value": float(value), "ctx": ctx})
        await ctx.send(embed=discord.Embed(
            description="New Timmer inserted when {} {} {}$ by {} ".format(currencie, type, value, ctx.message.author),
            colour=static.color_success))

    @commands.command(description='Insert Watchdog timer with percentage currencie, value',
                      brief="currencie ,percentage")
    async def triggerp(self, ctx, currencie, value):
        # await ctx.message.delete()
        currencie = currencie.upper()
        value = float(value.replace(",", "."))
        # add timmer to timmers
        price = client.get_spot_price(currency_pair=currencie + "-USD")
        p = float(price["amount"])
        if value > 0:
            type = "up"
        elif value < 0:
            type = "down"
        p = round(p + p * (value / 100), 4)
        if not currencie in self.timmers.keys():
            self.timmers.update({currencie: []})
        self.timmers[currencie].append({"type": type, "value": p, "ctx": ctx})
        await ctx.send(embed=discord.Embed(
            description="New Timmer inserted when {} {} {}$ by {} ".format(currencie, type, p, ctx.message.author),
            colour=static.color_success))


def setup(bot):
    bot.add_cog(Watchdog(bot))
