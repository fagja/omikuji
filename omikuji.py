import random

omikuji = ["大吉", "吉", "凶", "中吉 ", "末吉"]

index = random.randint(0, len(omikuji) - 1)

result = omikuji[index]

print(f"今日の運勢は...{result}")
