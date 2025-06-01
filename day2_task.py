#functions
#def sum_numbers(num1, num2):
 #   result = num1 + num2
  #  return result

#print(sum_numbers(3,4))

#def print_hello():
 #   print("Hello")
#print_hello()
#print_hello()
#print_hello()
#print_hello()
#print_hello()

#function in list
#cities =["delhi", "faisalabad", "LAHORE","ISLAMABAD","karachi"]
#def print_len(cities):
 #   print("The length of cities is: ", len(cities))

#print_len(cities)

#cities =["delhi", "faisalabad", "LAHORE","ISLAMABAD","karachi"]
#def print_cities(cities):
 #   for city in cities:
  #      print(city, end="\n")


#print_cities(cities)

#  if a % 2 == 0:
  #      print("Even")
 #       return a
  #  else:
   #     print("Odd")

#print(number_eo(12))

#recursive function
#   if n==0:
 #       return
  #  print(n)
   # show(n-1)

#show(7)

#def factorial(n):
  #  if n==0 or n==1:
   #     return 1
    #else:
     #   return n*factorial(n-1)

#print(factorial(6))

#sum of natural num
#def sum_of_natural_numbers(n):
 #   if n==10:
  #      return 1
   # else:
    #    return n+sum_of_natural_numbers(n-1)

#print(sum_of_natural_numbers(10))



def find_list(list, idx=1):
    if idx==len(list):
        return
    print(list[idx])
    find_list(list,idx+1)

lists_num = [1,4,9,16,25,36,49,64,81,100]
find_list(lists_num)