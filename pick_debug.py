import sys
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

async def pick_debug(ctx):
    await ctx.response.defer()
    txt_channel = g.client.get_channel(g.KOTEI_CHANNEL_ID)
    with open(g.pick_path) as f:
      for s_line in f:
        if str(g.now.date()) in s_line:
          await txt_channel.send("\n@everyone\n【お知らせ】\n本日は21時よりです。\n頑張りましょう！！")
          sys.stdout.write('Notify Activated!' + '\n')
          sys.stdout.flush()
          break
    await ctx.followup.send("【完了】本日開催であればお知らせを完了しました")