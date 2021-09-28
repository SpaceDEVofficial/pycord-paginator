from typing import List, Union
import discord
from discord.abc import Messageable
from pycord_components import (
    PycordComponents,
    Button,
    ButtonStyle,
    Select,
    SelectOption,
    Interaction,
)

from .errors import MissingAttributeException,InvaildArgumentException
from discord.ext import commands
class Paginator:
    def __init__(
        self,
        client: PycordComponents,
        channel: Messageable,
        ctx: Interaction,
        contents: List[str] = None,
        embeds: List[discord.Embed] = None,
        use_select: bool = False,
        only: discord.ext.commands.Context.author = None,
        desc: dict = None
    ):
        self.context = ctx
        self.client = client
        self.channel = channel
        self.contents = contents
        self.embeds = embeds
        self.use_select = use_select
        self.index = 0
        self.only = only
        self.desc = desc

        if self.contents is not None and self.embeds is not None:
            raise MissingAttributeException("You can't use contents and embeds at once!")

        if self.contents is None and self.embeds is None:
            raise MissingAttributeException("Both contents and embeds are None!")
        if self.contents is not None or self.embeds is not None and self.desc is None:
            raise InvaildArgumentException("Contents or embeds can't be None when desc is None.")

        if self.embeds is not None and len(self.embeds) != len(self.desc):
            raise InvaildArgumentException("The number of embeds and desc do not match each other!")
        if self.contents is not None and len(self.contents) != len(self.desc):
            raise InvaildArgumentException("The number of contents and desc do not match each other!")


    def get_components(self):
        if self.embeds == None:
            if self.use_select:
                keys = []
                values = []
                for key,value in self.desc:
                    keys.append(key)
                    values.append(value)
                return [
                    self.client.add_callback(
                        Select(
                            custom_id="paginator_select",
                            options=[
                                SelectOption(
                                    label=keys[i], value=str(i), default=keys[i] == self.index,description=values[i]
                                )
                                for i in range(len(self.contents))
                            ],
                        ),
                        self.select_callback,
                    )
                ]
            else:
                return [
                    [   self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="⏮"),
                            self.button_first_callback,
                        ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="◀️"),
                            self.button_left_callback,
                        ),
                        Button(
                            label=f"Page {self.index + 1}/{len(self.contents)}",
                            disabled=True,
                        ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="▶️"),
                            self.button_right_callback,
                        ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="⏭"),
                            self.button_last_callback,
                        ),
                    ]
                ]
        else:
            if self.use_select:
                keys = []
                values = []
                for key, value in self.desc.items():
                    keys.append(key)
                    values.append(value)
                return [
                    self.client.add_callback(
                        Select(
                            custom_id="paginator_select",
                            options=[
                                SelectOption(
                                    label=keys[i], value=str(i), default=keys[i] == self.index,description=values[i]
                                )
                                for i in range(len(self.embeds))
                            ],
                        ),
                        self.select_callback,
                    )
                ]
            else:
                return [
                    [self.client.add_callback(
                        Button(style=ButtonStyle.blue, emoji="⏮"),
                        self.button_first_callback,
                    ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="◀️"),
                            self.button_left_callback,
                        ),
                        Button(
                            label=f"Page {self.index + 1}/{len(self.embeds)}",
                            disabled=True,
                        ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="▶️"),
                            self.button_right_callback,
                        ),
                        self.client.add_callback(
                            Button(style=ButtonStyle.blue, emoji="⏭"),
                            self.button_last_callback,
                        ),
                    ]
                ]



    async def start(self):
        if self.embeds == None:
            self.msg = await self.channel.send(
                content=self.contents[self.index], components=self.get_components()
            )
        else:
            self.msg = await self.channel.send(
                embed=self.embeds[self.index], components=self.get_components()
            )

    async def select_callback(self, inter: Interaction):
        self.index = int(inter.values[0])
        if self.embeds == None:
            await inter.edit_origin(
                content=self.contents[self.index], components=self.get_components()
            )
        else:
            await inter.edit_origin(
                embed=self.embeds[self.index], components=self.get_components()
            )
    async def button_first_callback(self, inter: Interaction):
        if self.index == 0:
            pass
        else:
            self.index = 0

        await self.button_callback(inter)

    async def button_left_callback(self, inter: Interaction):
        if self.index == 0:
            if self.embeds == None:
                self.index = len(self.contents) - 1
            else:
                self.index = len(self.embeds) - 1
        else:
            self.index -= 1

        await self.button_callback(inter)

    async def button_right_callback(self, inter: Interaction):
        if self.embeds == None:
            if self.index == len(self.contents) - 1:
                self.index = 0
            else:
                self.index += 1
        else:
            if self.index == len(self.embeds) - 1:
                self.index = 0
            else:
                self.index += 1

        await self.button_callback(inter)

    async def button_last_callback(self, inter: Interaction):
        if self.embeds == None:
            if self.index == len(self.contents) - 1:
                pass
            else:
                self.index = len(self.contents) - 1
        else:
            if self.index == len(self.embeds) - 1:
                pass
            else:
                self.index = len(self.embeds) - 1

        await self.button_callback(inter)

    async def button_callback(self, inter: Interaction):
        if not self.only == None:
            if inter.user.id == self.only.id and inter.message.id != self.context.message.id:
                if self.embeds == None:
                    await inter.edit_origin(
                        content=self.contents[self.index], components=self.get_components()
                    )
                else:
                    await inter.edit_origin(
                        embed=self.embeds[self.index], components=self.get_components()
                    )
        else:
            if self.embeds == None:
                await inter.edit_origin(
                    content=self.contents[self.index], components=self.get_components()
                )
            else:
                await inter.edit_origin(
                    embed=self.embeds[self.index], components=self.get_components()
                )