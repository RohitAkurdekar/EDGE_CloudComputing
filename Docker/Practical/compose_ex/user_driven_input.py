'''
    This will run as a container
'''

#------ Add function ------------
def add_two_number(num1,num2):
    return num1+num2

#------ Main handler --------------

def my_handler():
    try:
        #------ Take numbers from user --
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        result = add_two_number(num1=num1,num2=num2)
        print(f"{num1}+{num2}={result}")
    except Exception as e:
        print("Exception in main handler: ",e)

# calling main handler
my_handler()
