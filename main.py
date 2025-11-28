History="History.txt"

def show_history():
    with open(History, "r") as file:
        lines=file.readlines()
        if len(lines)==0:
            print("No History Found")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    with open(History,"w"):
        print("History Cleared")

def save_to_history(equation, result):
    with open(History, "a") as file:
        file.write(f"{equation} = {result}\n")
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Not Proper Format; Eg: [ a + b ]")
        return
    try: 
        num1=float(parts[0])
        num2=float(parts[2])
    except ValueError:
        print("Only Number")
    
    operator=parts[1]
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        if num2==0:
            print("Cannot be Divided by Zero")
            return
        result=num1/num2
    else:
        print("Invalid Operator + - * /")
        return
    if int(result) == result:
        result= int(result)
    print(f"{user_input} = {result}")
    save_to_history(user_input,result)
def main():
    print("---Very Simple Calculator---\n---just +,-,*,/---")
    while True:
        user_input=input("Enter calculation or history or clear or exit: ")
        if user_input.lower()=="exit":
            break
        if user_input.lower()=="history":
            show_history()
        elif user_input.lower()== "clear":
            clear_history()
        else: 
            calculate(user_input)

main()     