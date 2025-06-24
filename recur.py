#La basura esta de recursividad 

# def atras(n):
#     if n <= 0:
#         print("hola")
#     else:
#         print(n, end = "... ")
#         atras(n-1)

# print(atras(10))
# abc = ["a", "b", "c"]
# def abc(n):
#     if n <= 0:
#         return "a"
#     else:
#         print(abc(n-1))
#         abc(n-1)

# abc(2)

# def gen_abc():
#     abecedario = ""
#     for i in range(97, 123,1):
#         abecedario += chr(i) + ", "
#     abecedario = abecedario.rstrip(", ")
#     return abecedario

# print(gen_abc())

def abc_rec(i):
    if i == "z":
        return i
    else:
        return i + ", " + abc_rec(chr(ord(i) + 1)) 
print(abc_rec("a"))
