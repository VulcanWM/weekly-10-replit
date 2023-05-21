from flask import Flask, render_template, redirect, send_file, request
import random
from functions import getcookie, addcookie, delcookie, cartesianproduct, difference, intersection, randomunion
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route('/')
def index():
  return render_template("index.html", start=getcookie("Stage"))

@app.route("/start")
def start():
  if getcookie("Stage") != False:
    return "You already have started the tutorial!"
  addcookie("Stage", "1-Info")
  return redirect("/do")

@app.route("/changestage/<stage>")
def changestage(stage):
  if getcookie("Stage") == False:
    return "You haven't started the interactive tutorial."
  try:
    split = stage.split("-")
    number = int(split[0])
    if number in [1, 2, 3, 4]:
      pass
    else:
      return f"{str(number)} isn't a real stage number!"
    if split[1] == "Info" or split[1] == "Questions":
      pass
    else:
      return f"There is no stage section such as {split[1]}"
  except:
    return "This isn't a correct stage!"
  delcookie("Stage")
  addcookie("Stage", stage)
  return redirect("/do")

@app.route("/1-Questions/<object1>/<letter1>/<object2>/<letter2>/<object3>", methods=['POST', 'GET'])
def onequestions(object1, letter1, object2, letter2, object3):
  if request.method == 'POST':
    answer = ""
    a = request.form['a']
    if a == ("{" + object1 + "}"):
      answer = answer + "<p>You got question 1 right!</p>"
    else:
      answer = answer + "<p>You got question 1 wrong! The set of " + object1 + " is written as {" + object1 + "}</p>"
    b = request.form['b']
    b = b.replace(" ", "")
    if b == (letter1 + "={" + object2 + "}"):
      answer = answer + "<p>You got question 2 right!"
    else:
      answer = answer + "<p>You got question 2 wrong! Set " + letter1 + " is the set of " + object2 + " is written as " + letter1 + "={" + object2 + "}</p>"
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    c = request.form['c']
    if letter2 in numbers:
      if object3 == "{numbers}":
        if c == "is":
          answer = answer + "<p>You got question 3 right!"
        else:
          answer = answer + "<p>You got question 3 wrong! ∈ means is an element in the set, and ∉ means is not an element in the set."
      if object3 == "{letters}":
        if c == "isnot":
          answer = answer + "<p>You got question 3 right!"
        else:
          answer = answer + "<p>You got question 3 wrong! ∈ means is an element in the set, and ∉ means is not an element in the set."
    if letter2 in letters:
      if object3 == "{letters}":
        if c == "is":
          answer = answer + "<p>You got question 3 right!"
        else:
          answer = answer + "<p>You got question 3 wrong! ∈ means is an element in the set, and ∉ means is not an element in the set."
      if object3 == "{numbers}":
        if c == "isnot":
          answer = answer + "<p>You got question 3 right!"
        else:
          answer = answer + "<p>You got question 3 wrong! ∈ means is an element in the set, and ∉ means is not an element in the set."
    return render_template("answers.html", stagenumber="1", feedback=answer, new="2", course=False)

@app.route("/main.css")
def maincss():
  return send_file("static/main.css")

@app.route("/pic-1")
def pic1():
  return send_file("static/pic-1.png")

@app.route("/setfunctions")
def setfunctionspage():
  return render_template("union.html")

@app.route("/setfunctions", methods=['POST', 'GET'])
def setfunctionsfunc():
  if request.method == 'POST':
    a = request.form['a']
    astuff = set(a.split(","))
    b = request.form['b']
    bstuff = set(b.split(","))
    c = request.form['c']
    cstuff = set(c.split(","))
    d = request.form['d']
    dstuff = set(d.split(","))
    if d == "" and c != "":
      cps = cartesianproduct(astuff, bstuff, cstuff)
      if cps == False:
        render_template("union.html", error="One or more of the text in the inputs aren't sets.")
      union = astuff.union(bstuff, cstuff)
      strunion = "{"
      for smth in union:
        strunion = strunion + smth + ","
      strunion = strunion[:-1]
      strunion = strunion + "}"
      answer = "The union of {" + a + "}, {" + b + "} and {" + c + "} is " + strunion + ".<br><br>"
      answer = answer + f"The cartesian product of the three sets is {cps}.<br><br>"
      i = intersection(astuff, bstuff, cstuff)
      answer = answer + f" The intersection is {i}."
      return render_template("union.html", answer=answer)
    elif d == "" and c == "":
      cps = cartesianproduct(astuff, bstuff)
      if cps == False:
        render_template("union.html", error="One or more of the text in the inputs aren't sets.")
      union = astuff.union(bstuff)
      strunion = "{"
      for smth in union:
        strunion = strunion + smth + ","
      strunion = strunion[:-1]
      strunion = strunion + "}"
      answer = "The union of {" + a + "} and {" + b + "} is " + strunion + ".<br><br>"
      answer = answer + f"The cartesian product of the two sets is {cps}.<br><br>"
      i = intersection(astuff, bstuff)
      answer = answer + f" The intersection is {i}.<br><br>"
      d = difference(astuff, bstuff)
      answer = answer + f"The difference is {d}."
      return render_template("union.html", answer=answer)
    elif d != "" and c != "":
      cps = cartesianproduct(astuff, bstuff, cstuff, dstuff)
      if cps == False:
        render_template("union.html", error="One or more of the text in the inputs aren't sets.")
      union = astuff.union(bstuff, cstuff, dstuff)
      strunion = "{"
      for smth in union:
        strunion = strunion + smth + ","
      strunion = strunion[:-1]
      strunion = strunion + "}"
      answer = "The union of {" + a + "}, {" + b + "}, {" + c + "} and {" + d + "} is " + strunion + ".<br><br>"
      answer = answer + f"The cartesian product of the three sets is {cps}.<br><br>"
      i = intersection(astuff, bstuff, cstuff, dstuff)
      answer = answer + f" The intersection is {i}."
      return render_template("union.html", answer=answer)
    if d != "" and c == "":
      cps = cartesianproduct(astuff, bstuff, dstuff)
      if cps == False:
        render_template("union.html", error="One or more of the text in the inputs aren't sets.")
      union = astuff.union(bstuff, dstuff)
      strunion = "{"
      for smth in union:
        strunion = strunion + smth + ","
      strunion = strunion[:-1]
      strunion = strunion + "}"
      answer = "The union of {" + a + "}, {" + b + "} and {" + d + "} is " + strunion + ".<br><br>"
      answer = answer + f"The cartesian product of the three sets is {cps}.<br><br>"
      i = intersection(astuff, bstuff, dstuff)
      answer = answer + f" The intersection is {i}."
      return render_template("union.html", answer=answer)

@app.route("/2-Questions/<theset>", methods=['POST', 'GET'])
def twoquestions(theset):
  if request.method == 'POST':
    answer = ""
    a = request.form['a']
    if a == "square":
      answer = answer + "<p>You got question 1 right!</p>"
    else:
      answer = answer + "<p>You got question 1 wrong! A venn diagram can be drawn as a rough circle, egg shape or oval; it cannot be drawn as a rough square.</p>"
    b = request.form['b']
    if b == "null":
      answer = answer + "<p>You got question 2 right!</p>"
    else:
      answer = answer + "<p>You got question 2 wrong! A null set is shown with Ø.</p>"
    c = "n(" + str(request.form['c'])
    c = c.replace(" ", "")
    count = 0
    for i in theset:
      if i == ',':
        count = count + 1
    count = count + 1
    setlen = "n(A)=" + str(count)
    if c == setlen:
      answer = answer + "<p>You got question 3 right!</p>"
    else:
      answer = answer + f"<p>You got question 3 wrong! A set with {str(count)} elements called A's number of values can be written as n(A)={str(count)}</p>"
    return render_template("answers.html", feedback=answer, new="3", course=False, stagenumber="2")

@app.route("/3-Questions/<set1>/<set2>", methods=['POST', 'GET'])
def threequestions(set1, set2):
  if request.method == 'POST':
    answer = ""
    a = request.form['a']
    if a == "isnot":
      answer = answer + "<p>You got question 1 right!</p>"
    else:
      answer = answer + '<p>You got question 1 wrong! The symbol for "is not a subset of" is ⊄.</p></p>'
    b = request.form['b']
    if b == "null":
      answer = answer + "<p>You got question 2 right!</p>"
    else:
      answer = answer + '<p>You got question 2 wrong! The symbol meaning "does not contain as a subset" is ⊅.</p>'
    # print(set(set1))
    # print(set(set2))
    return render_template("answers.html", feedback=answer, new="4", course="Ended!", stagenumber="3")

@app.route("/do")
def do():
  if getcookie("Stage") == False:
    return redirect("/start")
  if getcookie("Stage") == "1-Info":
    return render_template("1.html")
  elif getcookie("Stage") == "1-Questions":
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    options = ["{letters}", "{numbers}"]
    objects = ["books", "anime", "songs", "apps", "websites", "files", "searches", "wifis", "routes"]
    object1 = random.choice(objects)
    letter1 = random.choice(letters)
    object2 = random.choice(objects)
    option = random.choice(options)
    if option == "{letters}":
      letter2 = random.choice(letters)
    else:
      letter2 = random.choice(numbers)
    object3 = option
    return render_template("1questions.html", object1=object1, letter1=letter1, object2=object2, letter2=letter2, object3=object3)
  elif getcookie("Stage") == "2-Info":
    return render_template("2.html")
  elif getcookie("Stage") == "2-Questions":
    amount = random.randint(1,9)
    thelist = []
    for i in range(amount):
      number = random.randint(0,50)
      thelist.append(number)
    theset = set(thelist)
    return render_template("2questions.html", theset=theset)
  elif getcookie("Stage") == "3-Info":
    return render_template("3.html")
  elif getcookie("Stage") == "3-Questions":
    ru = randomunion()
    return render_template("3questions.html", set1=ru[0],set2=ru[1])
  elif getcookie("Stage") == "4-Info":
    return render_template("answers.html", course="ended!")
  else:
    return render_template("answers.html", course="ended!")

@app.route("/sticky.js")
def stickyjs():
  return send_file("static/sticky.js")