age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
money_for_birthday = 10
stolen = 0
toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_saved += money_for_birthday
        money_for_birthday += 10
        stolen += 1
    else:
        toys += 1

money_saved += toys * toy_price - stolen

if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {abs(money_saved-washing_machine_price):.2f}")
