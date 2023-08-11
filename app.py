# Functions

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard!")


# greet("Chris", "Kubiak")


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Chris")
# # print(message)
# file = open("content.txt", "w")
# file.write(message)


# def greet(name):
#     print(f"Hi {name}")


# print(greet("Chris"))


# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="John", age=22)


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"   
    return input


print(fizz_buzz(15))