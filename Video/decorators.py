# from datetime import datetime

# def not_during_the_night(func,func2):
#     def second_wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             func2()
#             pass  # Hush, the neighbors are asleep
#     return second_wrapper

# def say_hi():
#     print("Hello!")

# def say_silence():
#     print("Shh!")

# say_hi = not_during_the_night(say_hi,say_silence)

# print(say_hi())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")
# #Primero llevar a una variable y despues imprimir
# say_whee = my_decorator(say_whee)

# print(say_whee())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")
# #Con el decorator no hay necesidad de pasarlo a una variable, solo lo llamas y ya
# say_whee()

#use *args and **kwargs
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
