##### find the the length of the list###############
# input_list=input("enter the list seperated by space:")
# input_list=input_list.split()
# print(input_list)
# length=len(input_list)
# print ("length of input_list is:",length)

############# Get input from user and greet the person using function
# input_name=input("Enter the name of the person to be greeted:")
# # Conver the input name to upper case
# name=input_name.upper()
# def greet():
#     greeting=("Hello")
#     print(greeting,name)
# greet()

# ##################Max number from the list#########

# list=input("enter the number seperated by space:")
# use the white space to split
# if the entered number is seperated by comma we can use split(',')
# list=list.split()
# print(list)
# max_number = list[0]
# for number in list:
#     if number>max_number:
#         max_number = number
# print ( max_number)

###############################local & Global variable#####3
# s = " Global variable "
# def f():
#     s=" local variable"
#     print(" you defined me inside the function.So i am only a", s)
# f()
# print("I am Happy you defined me outside Function. So i am a ", s)

#########################Calculate the area of a rectangle######
def rectangle_area(length, width=5):
    return (length * width)
# Case 1: Only length is provided
area1 = rectangle_area(10)
print(f"Area with only length provided: {area1}")
# Case 2: Both length and width are provided
area2 = rectangle_area(20, 10)
print(f"Area with both length and width provided: {area2}")


