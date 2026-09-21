# Input bill amount
bill_amount = float(input("Enter the bill amount: "))
# Input service fee percentage
service_fee_percentage = float(input("Enter the service fee percentage (e.g.,10 for 10%): "))
# Calculate service fee
service_fee = bill_amount * (service_fee_percentage / 100)
print(f"The service fee is:${service_fee:.2f}")