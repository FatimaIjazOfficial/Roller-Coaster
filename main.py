print("Welcome to Roller Coaster Ride !")
height=int(input("Customer Height : "))
if height > 120:
  print("\t\t\t\t\t\tCustomer want to ride")
  age=int(input("Customer age : "))
  if age<12:
    ticket=5
  elif age >=12 and age<18:
    ticket=7
  elif age>=18:
    ticket=12
    if age >=45 and age<=55:
      ticket=0
  photo=input("Customer want photo ? Yes / No ? ") .lower()
  if photo=="yes":
    totalbill=ticket+3
    print(f"Total Bill : ${ticket+3}")
  else:
    print(f"Total Bill : ${ticket}")
else:
  print("Customer can't ride")