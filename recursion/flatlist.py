# define flatten() below...
def flatten(my_list):
  result = []

  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      result += flat_list
    
    if isinstance(item, list) == False:
       result.append(item)

  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
