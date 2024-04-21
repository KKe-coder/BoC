import sys
import datetime
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g
import set_next_week_date as n

async def result():
    txt_channel = g.client.get_channel(g.KOTEI_CHANNEL_ID)
    msg = await g.msg.channel.fetch_message(g.msg.id)
    reactions = []
    for i in range(7):
        reactions.append(msg.reactions[i].count)
    WeekDaysWithEmojis = []
    for WeekDay, WeekDayEmoji in zip(g.WeekDays, g.WeekDayEmojis):
        WeekDaysWithEmojis.append(str(n.get_next_target_date(g.now.date(), WeekDay)) + WeekDayEmoji)
    appendstr = ""
    for reaction, WeekDayWithEmoji in zip(reactions, WeekDaysWithEmojis):
        if reaction == g.party_must_num:
            appendstr =  appendstr + WeekDayWithEmoji + '\n・'
            with open(g.pick_path, mode='a') as f:
                f.write('\n' + str(WeekDayWithEmoji))
    await txt_channel.send("\n@everyone\n【投票終了】\n次の開催日は以下の通りです。\n頑張りましょう！！\n・"+ appendstr[:-2])
    sys.stdout.write('Result Activated!' + '\n')
    sys.stdout.flush()