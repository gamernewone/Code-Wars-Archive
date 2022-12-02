def valid_braces(string):
  # This function check if a string is has valid paired braces
  # str -> bool
  # Example: "()" -> True
  # Example: "[(])" -> False

  braces = dict()
  for i in string:
    if i in braces:
      braces[i] += 1
    else:
      braces[i] = 1
  if braces.get('(', 0) == braces.get(')', 0) and braces.get('[', 0) == braces.get(']', 0) and braces.get('{', 0) == braces.get('}', 0):
    hit = 0
    for i in range(int(len(string)/2)):
      if  i%2 != 0: continue
      if string[i] == string[-(i+1)].replace(')','(').replace('}','{').replace(']','[') or string[i] == string[i+1].replace(')','(').replace('}','{').replace(']','['):
        pass
      else:
        hit = 1
        break
    if hit == 0:
      return True
    else:
        return False
  else:
    return False