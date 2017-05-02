from sys import argv

script, age, year = argv

print "You started high school when you were:", age
print "You started high school in:", year
print "You graduated when you were:", int(age)+4
print "You graduated in the year:", int(year)+4

#Keeps failing sayin gtoo many values to unpack

#Got'Em! Through further investigation, when using argv must have script as first
#piece of the argument.  Then list your variables.
