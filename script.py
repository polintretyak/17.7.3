per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))

deposit = []

for bank, percent in per_cent.items():
    deposit.append(money * percent / 100)

print("Накопленные средства за год в каждом из банков:")
for i in range(len(deposit)):
    print(f"{list(per_cent.keys())[i]}: {deposit[i]}")

max_deposit = max(deposit)
print(f"\nМаксимальная сумма накопленных средств: {max_deposit}")
