lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

#for index in range(lost_fights_count):

helmet_times = int(lost_fights_count/2)
sword_times = int(lost_fights_count/3)
shield_time = int(lost_fights_count/6)
armor_times = int(lost_fights_count/12)

result = helmet_price*helmet_times + sword_price*sword_times + shield_price*shield_time + armor_price*armor_times

print(f"Gladiator expenses: {result:.2f} aureus")
