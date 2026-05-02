# Conditionals and logical operators
temperature = int(input("What is temperature today? "))
raining = False

if (temperature > 80 or temperature < 60) or raining:
  print ("Stay inside")
else:
  print("Enjoy the outdoors")
print("Have a good day!")