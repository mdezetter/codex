yuan = int(input("What do you have left in yuan? "))
yen = int(input("What do you have left in yen? "))
won = int(input("What do you have left in won? "))

usd_yuan = yuan * 0.14
usd_yen = yen * 0.0067
usd_won = won * 0.00070

total = usd_yuan + usd_yen + usd_won

print()
print(round(total),3)