#Taking inputs
print("Enter the first number:")
first_number = float(input())
print("Enter the second number:")
second_number = float(input())
#Calculating the sum
sum_of_numbers = first_number + second_number
#Calculating the difference
difference_of_numbers = first_number - second_number
#Calculating the product
product_of_numbers = first_number * second_number
#Calculating the quotient
if second_number != 0:
    quotient_of_numbers = first_number / second_number
else:
    quotient_of_numbers = "Undefined (division by zero)"

#Displaying the result
print("Addition:", sum_of_numbers)
print("Subtraction:", difference_of_numbers)
print("Multiplication:", product_of_numbers)
print("Division:", quotient_of_numbers)

