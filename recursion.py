# # 5! =  5 * 4!
# # 4! =  4 * 3!
# # 3! =  3 * 2!
# # 2! =  2 * 1!
# # 1! =  1 =>base condition

# # 5! =  5 * (5-1)!


# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(5))



#base = 5, power = 3 = 125
#base = 2, power = 3 = 8
def exponent(base, power):
    if power == 0:
        return 1
    return base * exponent(base, power-1)
    

print(exponent(5,3))
print(exponent(2,3))
