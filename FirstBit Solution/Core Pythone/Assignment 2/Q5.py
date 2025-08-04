### This program calculates the selling price of a book after applying a discount.
cost_price = int(input("Enter the cost price of the book: "))
discount_percent = int(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * cost_price
selling_price = cost_price + discount_amount
print(f'The selling price after a discount of {discount_percent}% is: {selling_price:.2f}')
