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


def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)