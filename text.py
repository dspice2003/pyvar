numbers = input("How many numbers you want to calculate? ")
grade_list = []

def evaluate():
    for i in range (numbers):
        grades = float(input("Please enter a number between 1-1000: "))
        while grades < 0 or grades > 1000:
            print ("The number " + str(grades) + " is out of range")
            grades = float(input("Please enter a number between 1-1000: "))
        grade_list.append(grades)
    average = sum(grade_list)/numbers
    if (average >= 500):
        print("Good,", str(average))
    if (average <= 500):
        print("Bad,", str(average))

try:
    numbers = int(numbers)
    evaluate()
except:
    while True:
        try:
            numbers = int(numbers)
            evaluate()
            break
        except:
            print("You should not enter " + str(numbers) + " because it is not an integer.")  
            numbers = input("How many numbers you want to calculate? ") 
