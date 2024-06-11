import locale
import datetime

# ロケールをシステムのデフォルトに設定
locale.setlocale(locale.LC_TIME, '')

# 現在の日付を取得
today = datetime.date.today()

# 曜日
weekday_name = today.strftime("%A")

# 出力
print("こんにちは！")
print(f"今日の日付は{today}")
print(f"今日の曜日は{weekday_name}です！")
