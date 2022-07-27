import random
hand = ['グー', 'チョキ', 'パー']
print("グー チョキ パーのどれかを入力してね")
plhand = input()
str(plhand)
cpuhand = random.choice(hand)
print(plhand + cpuhand)
if plhand == cpuhand:
  print("あいこだよ！")
else:
  if plhand == "グー":
    if cpuhand == "チョキ":
      print("あなたの勝ち！")
    if cpuhand == "パー":
      print("あなたの負け！")
  elif plhand == "チョキ":
    if cpuhand == "パー":
      print("あなたの勝ち！")
    if cpuhand == "グー":
      print("あなたの負け！")
  elif plhand == "パー":
    if cpuhan == "グー":
      print("あなたの勝ち！")
    if cpuhand == "チョキ":
      print("あなたの負け！")
      
