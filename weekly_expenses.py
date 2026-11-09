

name = input("Student name: ")
transport = float(input("Daily transport cost: "))
feeding = float(input("Daily feeding cost: "))
days = int(input("Days on campus: "))
other = float(input("Other weekly expenses: "))

transport_total = transport * days
feeding_total = feeding * days
weekly_total = transport_total + feeding_total + other

print("\nWEEKLY EXPENSE SUMMARY")
print(f"Student: {name}")
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")
