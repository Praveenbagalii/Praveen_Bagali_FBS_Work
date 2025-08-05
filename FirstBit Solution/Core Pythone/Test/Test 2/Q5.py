### A man goes for shopping. He buys 5 products. Accept the price of all products and display 
# the total bill after adding 18% GST
price1 = int(input("Enter the price of product 1: "))
price2 = int(input("Enter the price of product 2: "))
price3 = int(input("Enter the price of product 3: "))
price4 = int(input("Enter the price of product 4: "))
price5 = int(input("Enter the price of product 5: "))
total_price = price1 + price2 + price3 + price4 + price5
gst = total_price * 0.18
total_bill = total_price + gst
print(f"The total bill after adding 18% GST is: {total_bill}")