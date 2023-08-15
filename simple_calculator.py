#create a function to do mathematical function based on 2 incoming parameters
def compute_response(variable1, variable2):
  print("the operation is", operation)
  if operation == 1:
    print("Addition of",
          variable1,
          variable2,
          "is =",
          variable1 + variable2,
          end='\n')
  elif operation == 2:
    print("Subtraction of",
          variable1,
          variable2,
          "is =",
          variable1 - variable2,
          end='\n')
  elif operation == 3:
    print("Division of",
          variable1,
          variable2,
          "is =",
          variable1 / variable2,
          end='\n')
  elif operation == 4:
    print("Multiply of",
          variable1,
          variable2,
          "is =",
          variable1 * variable2,
          end='\n')
  else:
    print("Invalid value", end='\n')


# Collect user input
print("What operation do you like to do")
print("1 : Add", "\n", "2: Sub", "\n", "3: Divide", "\n", "4: Multiply")

operation = int(input("Enter your response :"))
if operation > 4 or operation < 1:
  print("Please enter a valid response")
else:
  variable1 = int(input("Enter your first number :"))
  variable2 = int(input("Enter your second number :"))
  compute_response(variable1, variable2)
