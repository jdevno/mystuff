name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
centi_height =  height * 2.54
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilo_weight = weight * .453592  

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % centi_height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's %d kilograms heavy." % kilo_weight
print "He likes this weight better lol."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exaclty right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)