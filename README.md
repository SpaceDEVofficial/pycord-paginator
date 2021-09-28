<div align="center">
    <div>
        <h1>Pycord-Paginator</h1>
        <span> <a href="https://pypi.org/project/pycord-components"><img src="https://raw.githubusercontent.com/kiki7000/discord.py-components/master/.github/logo.png" alt="discord-components logo" height="10" style="border-radius: 50%"></a>With pycord-components</span>
    </div>
    <div>
    </div>
    <div>
        <h3>paginator using pycord_components</h3>
    </div>
</div>

## Welcome!
It's a paginator for pycord-componets! Thanks to the original creator khk4912 (khk4912 /EZPaginator)!

This project is open source ⭐.

[official discord server](https://shrt.kro.kr/discord), so if you have a question, feel free to ask it on this server.

It was produced by referring to the open source of "[decave27](https://github.com/decave27/ButtonPaginator)".
## Install
```
pip install --upgrade PycordPaginator
```

## Example
```py
from PagiNation import Paginator
from discord.ext.commands import Bot
from pycord_components import PycordComponents
import discord

bot = Bot("your prefix")

@bot.event
async def on_ready():
    PycordComponents(bot)
    print(f"Logged in as {bot.user}!")

@bot.command()
async def pagination(ctx):
    embeds = [discord.Embed(title="1 page"), discord.Embed(title="2 page"), discord.Embed(title="3 page"),
                  discord.Embed(title="4 page"), discord.Embed(title="5 page")]
    desc = {
        "Basic help":"Basic help description",
        "example help1":"example help1 description",
        "example help2":"example help2 description",
        "example help3":"example help3 description",
        "example help4":"example help4 description"
    }


    e = Paginator(
        client=bot.components_manager,
        embeds=embeds,
        channel=ctx.channel,
        only=ctx.author,
        ctx=ctx,
        use_select=True,
        desc=desc)
    await e.start()

bot.run("your token")
```


## result
### use_select == True
![button](https://media.discordapp.net/attachments/889514827905630290/892211050114609182/2021_09_28_09_41_30_720.gif?width=585&height=644)


### use_select == False
![select](https://media.discordapp.net/attachments/889514827905630290/892211620506382406/2021_09_28_09_49_44_57.gif?width=585&height=644)

## option
```py
class Paginator:
    def __init__(
        self,
        client: PycordComponents,
        channel: Messageable,
        ctx: Interaction,
        contents: List[str] = None,
        embeds: List[discord.Embed] = None,
        use_select: bool = False, #if False, use buttons
        only: discord.ext.commands.Context.author = None,
        desc: dict = None
    ):
```

## License
This project is under the MIT License.

## Contribute
Anyone can contribute to this by forking the repository, making a change, and create a pull request!

But you have to follow these to PR.
+ Use the black formatter.
+ Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
+ Test.

## Thanks to
+ [khk4912](https://github.com/khk4912/EZPaginator) - Original Paginator developer
+ [Leek5](https://github.com/Leek5/pycord-components) - pycord componets lib developer
