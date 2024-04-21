#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

async def pick_clear(ctx):
    await ctx.response.defer()
    with open(g.pick_path, "r+") as f:
        f.truncate(0)
        f.seek(0)
    await ctx.followup.send("【完了】お知らせ用の日付ファイルの中身をクリアしました")