# Day 02: Tip Calculator

# Display a greeting
print("Welcome to the tip calculator.")

# Ask the user for the total bill
bill = float(input("What was the total bill? $"))

# Ask the user for the percentage tip (10%, 12% or 15%)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask the user how many people to split the bill
person = int(input("How many people to split the bill? "))

# Convert percentage tip to decimal
tip = tip / 100

# Compute for the total tip
total_tip = bill * tip

# Compute for the total amount with total tip
total_amount_with_tip = bill + total_tip

# Computer for the bill for each person
bill_per_person = total_amount_with_tip / person

# Format the final amount using round() with 2-decimal point accuracy
final_amount = round(bill_per_person, 2)

# Print final amount using f-string
print(f"Each person should pay: ${final_amount}")