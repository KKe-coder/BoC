import os
#同一ディレクトリ内モジュール
  #グローバル変数管理
import global_value as g

#週のリストと絵文字を定義
g.WeekDays = ['月','火','水','木','金','土','日']
g.WeekDayEmojis = ["<:1_Mon_o:1127510785325805599>",
                "<:2_Tue_o:1127510802115596299>",
                "<:3_Wed_o:1127510816770506863>",
                "<:4_Thu_o:1127510830833995827>",
                "<:5_Fri_o:1127510841923735662>",
                "<:6_Sat_o:1127510851683877005>",
                "<:7_Sun_o:1127510861553074236>"]
g.WeekDays_Copy = g.WeekDays

#上記リストを週の開始曜日によって並び替える(開始曜日は.envにて設定)
START_DAY_OF_THE_WEEK = str(os.getenv("START_DAY_OF_THE_WEEK"))
WeekdaysEditer1 = []
WeekdaysEditer2 = []
WeekdaysEmojisEditer1 = []
WeekdaysEmojisEditer2 = []
Switchboot = ''
for (i, j) in zip(g.WeekDays, g.WeekDayEmojis):
    if i == START_DAY_OF_THE_WEEK or Switchboot == True:
        WeekdaysEditer1.append(i)
        WeekdaysEmojisEditer1.append(j)
        Switchboot = True
    else:
        WeekdaysEditer2.append(i)
        WeekdaysEmojisEditer2.append(j)
WeekdaysEditer1.extend(WeekdaysEditer2)
WeekdaysEmojisEditer1.extend(WeekdaysEmojisEditer2)
g.WeekDays = WeekdaysEditer1
g.WeekDayEmojis = WeekdaysEmojisEditer1

def set_day_index(day_of_the_week):
  g.WeekDays_Copy.index(day_of_the_week)
