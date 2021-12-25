import part1
import part2
import part3
import part4
import part5

program = int()

while program != '':
  program = input("Which part(1, 2, 3, 4, or 5)? ")
  if program == '1':
    part1.code()  
  elif program == '2':
    part2.code()  
  elif program == '3':
   part3.code()
  elif program == '4':
   part4.code()  
  elif program == '5':
    part5.code()
