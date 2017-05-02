from sys import argv

script, filename = argv
# states that to user we are going to erase the file they have provided to as the argument.
print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-CTRL-C (^C)."
print "If you do want that, hit ENTER."
# if user does not exit out of the program then it will proceed with the following instructions.
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file now."

target.writelines(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()
