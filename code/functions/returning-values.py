def function_1(list_1):
  for index in range(len(list_1)):
    list_1[index] = list_1[index] * 5
  
  return(list_1)
  print("Hello")
  
my_modified_list = function_1([1,2,3,4,5])
print(my_modified_list[0])