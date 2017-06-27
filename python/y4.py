#exp-10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#exp-11
print "How old are you?",
age = raw_input(22)
print "How tall are you?",
height = raw_input(180)
print "How much do you weigh?",
weight = raw_input(64)

print "So, you're %r old, %r tall and %r heavy." % (
    22, 180, 64)

#exp-12
age = raw_input("How old are you? 22")
height = raw_input("How tall are you? 180cm")
weight = raw_input("How much do you weigh? 64kg")

print "So, you're %r old, %r tall and %r heavy." % (
    '22', '180cm', '64kg')

