bill_total = 1200
people = 4

friends = ["Betelhem", "Abel", "Sara", "Hanna"]

def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

share = split_bill(bill_total, people)

for friend in friends:
    print(f"{friend} should pay ETB {share:.2f}")