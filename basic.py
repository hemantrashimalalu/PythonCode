
# Numbers

x = 1    # INT
y = 2.9  # FLOAT
z = x + y

print(type(x))
print(type(y))
print(type(z))

# Lambda
# A lambda function can take any number of arguments, but can only have one expression.
# Example

x = lambda a, b: a * b
print(x(3, 10))

y = lambda a, b, c: a + b * c
print(y(2, 4, 8))

# If ... Elif ... Else

a = 10
b = 20

if a > b:
    print("Yes A is greater than B")

    else
    print("B is Greater that A")