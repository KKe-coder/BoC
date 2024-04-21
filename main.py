import os
import datetime
import pytz
import discord
import sys
from discord.ext import tasks, commands
import discord.app_commands

#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

import set_day as s
import set_next_week_date as n
import vote as v
import vote_debug as vd
import remind as r
import remind_debug as rd
import result as e
import result_debug as ed
import pick as p
import pick_debug as pd
import pick_clear as pc
import vote2pick as v2p

# DEBUG
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.none()
intents.messages = True
intents.guilds = True
intents.message_content = True
g.client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(g.client)

# デバッグ用日付設定(任意の日付を設定する)
g.debugdate = datetime.datetime(2024,2,17)
g.now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
g.today = datetime.date.today()

# デバッグモード
debugmode = False

# お知らせ用ファイル
g.pick_path = './pick_date.txt'
g.f = open(g.pick_path)

@g.client.event
async def on_ready():
    sys.stdout.write('(Starting... .... in:' + os.path.basename(__file__) +')\n\n')
    sys.stdout.flush()
    time_loop.start()
    await tree.sync(guild=discord.Object(id=KOTEI_SERVER_ID))

@tasks.loop(minutes=1)
async def time_loop():
    g.now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    g.today = datetime.date.today()

    # |debug message|
    sys.stdout.write('##DEBUG MESSAGE START##\n')
    sys.stdout.write('hour: ' + str(g.now.hour) + ', minute: ' + str(g.now.minute) + '\n')
    sys.stdout.write('today: ' + str(g.now.date()) + ', weekday: ' + str(g.now.date().weekday()) + '\n')
    sys.stdout.write('next weekday test: ' + str(n.get_next_target_date(g.today,'水')) + '\n')
    sys.stdout.write('debug mode: ' + debugmodestr)
    sys.stdout.write('\n##DEBUG MESSAGE END##\n\n')
    sys.stdout.flush()

    if g.now.date().weekday() == vote_day and g.now.hour == vote_hour and g.now.minute == vote_minute:
       await v.vote()

    if g.now.date().weekday() == remind_day and g.now.hour == remind_hour and g.now.minute == remind_minute:
       await r.remind()

    if g.now.date().weekday() == result_day and g.now.hour == result_hour and g.now.minute == result_minute:
        await e.result()

    if g.now.hour == pick_hour and g.now.minute == pick_minute:
        await p.pick()

    # #クライアント終了(デバッグ用)
    # await g.client.close()

# ここからコマンド
if debugmode != True:
    KOTEI_SERVER_ID = int(os.getenv("KOTEI_SERVER_ID"))
else:
    KOTEI_SERVER_ID = int(os.getenv("DEBUG_SERVER_ID"))

@tree.command(
    name="boc_1_vote",
    description="【手動】投票開始用"
)
@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def votemsg(ctx:discord.Interaction):
    await vd.vote_debug(ctx)

@tree.command(
    name="boc_2_rem",
    description="【手動】投票リマインド用"
)
@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def remmsg(ctx:discord.Interaction,message_id:str):
    await rd.remind_debug(ctx,message_id)

@tree.command(
    name="boc_3_res",
    description="【手動】投票結果発表用"
)

@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def resmsg(ctx:discord.Interaction,message_id:str):
    await ed.result_debug(ctx,message_id)

@tree.command(
    name="boc_4_pic",
    description="【手動】開催日当日のお知らせ"
)
@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def picmsg(ctx:discord.Interaction):
    await pd.pick_debug(ctx)

@tree.command(
    name="boc_5_pic",
    description="【手動】開催日当日のお知らせファイルリセット"
)
@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def picmsg(ctx:discord.Interaction):
    await pc.pick_clear(ctx)

@tree.command(
    name="boc_6_v2p",
    description="【手動】投票結果よりお知らせ日付を生成"
)
@discord.app_commands.guilds(KOTEI_SERVER_ID)
@discord.app_commands.default_permissions(administrator=True)
async def picmsg(ctx:discord.Interaction,message_id:str):
    await v2p.vote_to_pick(ctx,message_id)

TOKEN = os.getenv("DISCORD_TOKEN")
if debugmode != True:
    g.party_must_num = int(os.getenv("PARTY_MEMBER_MUSTNUM"))
    KOTEI_SERVER_ID = int(os.getenv("KOTEI_SERVER_ID"))
    g.KOTEI_CHANNEL_ID = int(os.getenv("KOTEI_CHANNEL_ID"))
    vote_day = s.set_day_index(str(os.getenv("VOTE_DAY_OF_THE_WEEK")))
    vote_hour = int(os.getenv("VOTE_HOUR"))
    vote_minute = int(os.getenv("VOTE_MINUTE"))
    remind_day = s.set_day_index(str(os.getenv("REMIND_DAY_OF_THE_WEEK")))
    remind_hour = int(os.getenv("REMIND_HOUR"))
    remind_minute = int(os.getenv("REMIND_MINUTE"))
    result_day = s.set_day_index(str(os.getenv("RESULT_DAY_OF_THE_WEEK")))
    result_hour = int(os.getenv("RESULT_HOUR"))
    result_minute = int(os.getenv("RESULT_MINUTE"))
    pick_hour = int(os.getenv("PICK_HOUR"))
    pick_minute = int(os.getenv("PICK_MINUTE"))
    debugmodestr = "NOT DEBUG MODE"
else:
    g.party_must_num = 2
    KOTEI_SERVER_ID = int(os.getenv("DEBUG_SERVER_ID"))
    g.KOTEI_CHANNEL_ID = int(os.getenv("DEBUG_CHANNEL_ID"))
    vote_day = g.now.date().weekday()
    vote_hour = g.now.hour
    vote_minute = g.now.minute
    remind_day = g.now.date().weekday()
    remind_hour = g.now.hour
    remind_minute = (g.now + datetime.timedelta(minutes=1)).minute
    result_day = g.now.date().weekday()
    result_hour = g.now.hour
    result_minute = (g.now + datetime.timedelta(minutes=1)).minute
    pick_hour = g.now.hour
    pick_minute = (g.now + datetime.timedelta(minutes=2)).minute
    debugmodestr = "DEBUG MODE"

g.client.run(TOKEN)
