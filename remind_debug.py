import os
import sys
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

async def remind_debug(ctx,message_id):
    await ctx.response.defer()
    txt_channel = g.client.get_channel(g.KOTEI_CHANNEL_ID)
    msg = await txt_channel.fetch_message(int(message_id))
    reactions = []
    for i in range(6):
        reactions.append(msg.reactions[i].count)
    await txt_channel.send('\n@everyone\n【リマインド】\n予定締め切り時間まであと3時間です。')
    if max(reactions) < g.party_must_num:
        await txt_channel.send("**投票してない方がいるみたいですよ！再度確認ください！**")
    sys.stdout.write('Remind_DEBUG Activated!' + '\n')
    sys.stdout.flush()
    await ctx.followup.send("【完了】リマインドを完了しました")