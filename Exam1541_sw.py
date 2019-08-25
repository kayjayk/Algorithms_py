# -*- coding: utf-8 -*-

user_input = input()


temp_integer = ""

input_split_list = list()

for i in range(len(user_input)):
    
    
    c = user_input[i]

        
    if c == "-":
        
        input_split_list.append(int(temp_integer))
        input_split_list.append("-")
        
        temp_integer = ""
        
    elif c == "+":

        input_split_list.append(int(temp_integer))        
        input_split_list.append("+")        
    
        temp_integer = ""
    
    elif i != (len(user_input) - 1):
        
        temp_integer += c
    
    else:
        
        temp_integer += c
        input_split_list.append(int(temp_integer))  
        
def find_min(input_split_list):
    
    print(input_split_list)
    
    if len(input_split_list) == 1:
        
        return input_split_list[0]
    
    elif input_split_list[1] == "+":
        
        return (input_split_list[0] + find_min(input_split_list[2:]))
        
    else:
        
        return (input_split_list[0] - find_max(input_split_list[2:]))
        
def find_max(input_split_list):
    
    print(input_split_list)
    
    
    if len(input_split_list) == 1:
        
        return input_split_list[0]
    
    elif input_split_list[1] == "-":
        
        return (input_split_list[0] + find_min(input_split_list[2:]))
        
    else:
        
        return (input_split_list[0] - find_max(input_split_list[2:]))
        


print(find_min(input_split_list))
        