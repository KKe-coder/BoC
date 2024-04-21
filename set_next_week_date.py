import datetime
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

def get_next_target_date(date, target_week):
    weekday = date.weekday()
    add_days = 7 - weekday + g.WeekDays.index(target_week)
    next_target_date = date + datetime.timedelta(days = add_days)
    return next_target_date
# 日付を計算する関数は、日付を越えているか否かでカウントが異なる->とりあえず、次の指定曜日の日付から7日