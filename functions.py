from flask import session
import random

def addcookie(key, value):
  session[key] = value

def delcookie(keyname):
  session.clear()

def getcookie(key):
  try:
    if (x := session.get(key)):
      return x
    else:
      return False
  except:
    return False

def cartesianproduct(*args):
  thelen = len(args)
  for theset in args:
    if str(type(theset)) != "<class 'set'>":
      return False
  if thelen == 2:
    cps = [{x, y} for x in args[0] for y in args[1]]
    return cps
  if thelen == 3:
    cps = [{x, y, z} for x in args[0] for y in args[1] for z in args[2]]
    return cps
  if thelen == 4:
    cps = [{x, y, z, w} for x in args[0] for y in args[1] for z in args[2] for w in args[3]]
    return cps

def intersection(*args):
  i = []
  setlen = len(args)
  for x in args[0]:
    if setlen == 2:
      if x in args[1]:
        i.append(x)
    if setlen == 3:
      if x in args[1] and x in args[2]:
        i.append(x)
    if setlen == 4:
      if x in args[1] and x in args[2] and x in args[3]:
        i.append(x)
  return set(i)

def difference(*args):
  if len(args) != 2:
    return False
  return args[0] - args[1]

def randomunion():
  amount1 = random.randint(0,9)
  amount2 = random.randint(0,9)
  list1 = []
  for i in range(amount1):
    number = random.randint(0,50)
    list1.append(number)
  list2 = []
  for i in range(amount2):
    number = random.randint(0,50)
    list2.append(number)
  set1 = set(list1)
  set2 = set(list2)
  answer = set1.union(set2)
  return set1, set2, answer

# def solveunion():
#   string = "6, 5, 4"
#   string2 = "3, 9, 7, 6"
#   print(set(string.split(", ")).union(set(string2.split(", "))))

# solveunion()

print(randomunion())

# print(intersection({5, 4, 3}, {3, 2, 1}))
# print(difference({3,5,74,54}, {5,73,32}))