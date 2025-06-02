#dictionaries
#info={
 #  "name":"maryam ",
  #  "age":"20 ",
   #"degree":"BS Ai",
#}
#print(info)

#nested dictionaries
#info={
 #  "name":"maryam ",
  #  "age":20 ,
   #"degree":"BS Ai",
   #"subjects":{
    #   "maths":60,
     #  "dld":59,
      # "C++":55,
       #"English":54,
   #}
#}
#print(info)

#dict methods
info={
   "name":"maryam ",
    "age":20 ,
   "degree":"BS Ai",
   "subjects":{
       "maths":60,
       "dld":59,
       "C++":55,
       "English":54,
   }
}
print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
new_dict={"name":"zainab ","age":21,"gender":"female"}
res = info.update(new_dict)
print(info)