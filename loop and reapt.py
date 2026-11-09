

days = int(input("Enter number of days: "))
while days <= 0:
    print("Invalid input.")
    days = int(input("Enter number of days: "))

total_sales = 0
high_sales = 0
low_sales = 0

for i in range(1, days + 1):
    sales = float(input("Enter sales for day: "))
    while sales < 0:
        print("Sales cannot be negative.")
        sales = float(input("Enter sales for day: "))
    
    total_sales = total_sales + sales
    
    if sales >= 10000:
        high_sales = high_sales + 1
    else:
        low_sales = low_sales + 1

average_sales = total_sales / days

print("\nSALES SUMMARY")
print("Total sales: NGN", total_sales)
print("Average daily sales: NGN", average_sales)
print("Days with sales of at least NGN 10,000:", high_sales)
print("Days with sales below NGN 10,000:", low_sales)
