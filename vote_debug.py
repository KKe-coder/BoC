import sys
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g
import set_next_week_date as n

async def vote_debug(ctx):
    await ctx.response.defer()
    txt_channel = g.client.get_channel(g.KOTEI_CHANNEL_ID)
    WeekDaysWithEmojis = []
    appendstr = ""
    for WeekDay, WeekDayEmoji in zip(g.WeekDays, g.WeekDayEmojis):
        WeekDaysWithEmojis.append(str(n.get_next_target_date(g.now.date(), WeekDay)) + WeekDayEmoji)
    for i, WeekDayWithEmoji in enumerate(WeekDaysWithEmojis):
        if i == len(WeekDaysWithEmojis) - 1:
            appendstr =  appendstr + WeekDayWithEmoji
        else:
            appendstr =  appendstr + WeekDayWithEmoji + '\n・'
    msg = await txt_channel.send('\n@everyone\n【投票】次の固定はいつがいいですか？投票をお願いします！\n・' + appendstr)
    for WeekDayEmoji in g.WeekDayEmojis:
        await msg.add_reaction(WeekDayEmoji)
    sys.stdout.write('Vote_DEBUG Activated!' + '\n')
    sys.stdout.flush()
    g.WeekDaysWithEmojis = WeekDaysWithEmojis
    g.appendstr = appendstr
    g.msg = msg
    await ctx.followup.send("【完了】投票の出力を完了しました")

