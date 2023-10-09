my_list=[]#creating a data structure
def add_element(data_structure, element):#craeting a an add Function,here data_structure is the our list(my_list)
    data_structure.append(element)
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")
add_element(my_list,"gg")#the values can be anything
add_element(my_list,17)
add_element(my_list,23)
print(my_list)
remove_element(my_list,23)
print("updated list:",my_list)