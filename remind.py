import sys
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

async def remind():
    txt_channel = g.client.get_channel(g.KOTEI_CHANNEL_ID)
    msg = await g.msg.channel.fetch_message(g.msg.id)
    reactions = []
    for i in range(6):
        reactions.append(msg.reactions[i].count)
    await txt_channel.send('\n@everyone\n【リマインド】\n予定締め切り時間まであと3時間です。')
    if max(reactions) < g.party_must_num:
        await txt_channel.send("**投票してない方がいるみたいですよ！再度確認ください！**")
    sys.stdout.write('Remind Activated!' + '\n')
    sys.stdout.flush()