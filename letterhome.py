# the beginning

print "Welcome to the automatic write-a-letter-home generator. Please answer these questions and I will write your letter for you.\n\n"

# asking questions

recipient = raw_input("Who are you writing the letter to? ")
thingididinclass = raw_input("What is one thing you did in class today? ")
opinionofclass = raw_input("How was class? (fun, boring, easy, exciting, etc) ")
friendname = raw_input("Name a friend you did something with today. ")
thingididwithfriend = raw_input("What did you do with that friend? ")
familymember = raw_input("Name a family member. ")
nextdayiwillcomehome = raw_input("When will you be home next? ")
thingineed = raw_input("Name something you need to get. ")
myname = raw_input ("What is your name? ")


# testing values -- comment out

"""
recipient = "Mom"
thingididinclass = "dissected a frog"
opinionofclass = "fun"
friendname = "David"
thingididwithfriend = "fixed my computer"
familymember = "Grandma"
nextdayiwillcomehome = "Friday"
myname = "Mel"
thingineed = "laundry detergent"
"""

# making the letter

letter = "Hello " + recipient + ", how are you? I am fine.\n\nSchool is going well. Today in class, I " + thingididinclass + ". I thought it was " + opinionofclass + ". Afterwards, " + friendname + " and I " + thingididwithfriend + ". Hope " + familymember + " is doing well, and I am looking forward to seeing you on " + nextdayiwillcomehome +"! Please send " + thingineed + ".\n\nLove,\n" + myname

# displaying the letter

print "\n\nHere is your letter:\n----------------------\n"
print letter
