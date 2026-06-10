print("Bill Split Calculator")

bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
number_of_people = int(input("Enter number of people: "))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount

print(f"\nTotal (including tip): ${total_amount:.2f}")

amount_per_person = total_amount / number_of_people

print(f"Each person pays: ${amount_per_person:.2f}")