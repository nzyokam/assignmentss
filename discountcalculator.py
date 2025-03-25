# Get user input
price = float(input("Enter the original price of the item: KSH "))
discount = float(input("Enter the discount percentage: "))

# Calculate discount amount and final price
if discount >= 20:
    discount_amount = (discount / 100) * price
    print(f"Discount Amount: KSH {discount_amount:.2f}")
    final_price = price - discount_amount
    print(f"Final Price after Discount: KSH {final_price:.2f}")
else:
    print("Discount is less than 20, no discount applied.")
    print("Final Price: KSH ", price)
