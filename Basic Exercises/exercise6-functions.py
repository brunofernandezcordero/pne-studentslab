print("--- Exercise 6a ---")
def is_even(number):
    even = number % 2 == 0
    return even
print("is_even(4):",is_even(4))
print("is_even(7):",is_even(7))
print("is_even(0):",is_even(0))
print("is_even(-3):",is_even(-3))
print("is_even(10):",is_even(10))

print("\n--- Exercise 6b ---")
def classify_triangle(a,b,c):
    if a == b and b == c and c == a:
        triangle = "equilateral"
    elif a == b or b == c or c == a:
        triangle = "isosceles"
    else:
        triangle = "scalene"
    return triangle

print("classify_triangle(5,5,5)",classify_triangle(5,5,5))
print("classify_triangle(3,3,4)",classify_triangle(3,3,4))
print("classify_triangle(3,4,5)",classify_triangle(3,4,5))
