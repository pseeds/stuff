
JOULES_PER_TON_TNT = 4.184*10**9
 
while 1:
  num_str = input( "Please enter a Richter value: ")
  num_float = float(num_str)
  energyj = 10**((1.5*num_float) + 4.8)
  energytnt = energyj / JOULES_PER_TON_TNT
  print( "Richter value: ", num_float, " Energy Joules: ", energyj, "Energy Tons TNT:", energytnt )
