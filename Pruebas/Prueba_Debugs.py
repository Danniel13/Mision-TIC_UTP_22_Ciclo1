# def sum(x):
#     res = 0
#     for i in range(x):
#         res+=i
#     return res
    
# print(sum(4))

# def print_nums(x):
#   for i in range(x):
#     print(i)
#   return
# print_nums(10)

def Search(a:str,b:str): 
  if b in a:
    return("Word found")
  else:
    return("Word not found")
  

text = str(input())
word = str(input())



print(Search(text, word))







# text = "los patos vuelan"
# word = "patos"

# if word in text:
#   print("Word found")
# else:
#   print("Word not found")