marks = int(input("Enter marks: "))
Grade = 'F'

if marks >= 101:
  print ("Please enter a valid marks: ")
  exit()

if marks >= 90:
  Grade = 'A'
elif marks >= 80:
  Grade = 'B'

elif marks >= 70:
  Grade = 'C'

elif marks >= 60:
  Grade = 'D'

else:
  Grade = 'F'

print(Grade)