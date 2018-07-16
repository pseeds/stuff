for i in range(1,101):
  Mod3 = i % 3
  Mod5 = i % 5
  if (Mod3 == 0) and (Mod5 == 0):
    print("FizzBuzz")
  elif (Mod3 == 0):
    print("Fizz")
  elif (Mod5 == 0):
    print("Buzz")
  else:
    print(i)
