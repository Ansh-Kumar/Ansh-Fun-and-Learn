# Ansh's Italian(not really) Pizzaria Palace
print("Welcome to Ansh's Italian(not really) Pizzaria Palace")

cost_of_large_pizza = 21.99 * 2

cost_of_medium_pizza = 17.99 * 2

cost_of_small_pizza = 12.99 * 2

amount_of_large_pizza = eval(input("How many large pizza's would you like to order?"))
 
amount_of_medium_pizza = eval(input("How many medium pizza's would you like to order?"))

amount_of_small_pizza = eval(input("How many small pizza's would you like to order?"))

subtotal = (cost_of_large_pizza * amount_of_large_pizza) + (cost_of_medium_pizza * cost_of_medium_pizza) + (cost_of_small_pizza * amount_of_small_pizza)
subtotal = round(subtotal, 2)
sales_tax = subtotal * 0.09
sales_tax = round(sales_tax, 2)
total = sales_tax + subtotal
total = round(total,  2)

print("Subtotal:     ", subtotal)

print()

print("Sales Tax:     ", sales_tax)

print()

print("Total:     ", total)

print("Thank you for choosing Ansh's Italian(not really) Pizzaria Palace!!!")
