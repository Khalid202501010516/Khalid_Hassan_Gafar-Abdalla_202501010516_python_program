while True:
   
   #Students Quiz Inputs

    mark1 = float(input("Enter mark 1: "))
    mark2 = float(input("Enter mark 2: "))
    mark3 = float(input("Enter mark 3: "))
  
   #The process 

    total = mark1 + mark2 + mark3
    average = total / 3

    print("Average mark:", average)
   
   #The Outputs pass/fall 

    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    again = input("Do you want to enter another student's marks? (yes/no): ")

    if again.lower() != "yes":
        break