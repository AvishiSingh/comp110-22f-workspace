"""An example of a while loop statement"""

counter: int = 0
masimum: int = int(input("Count up to, but not including what?"))
while counter < masimum:
    counter_sqaured: int = counter ** 2
    print (("The square of ") + str(counter) + " is " + str(counter_sqaured))
    counter = counter 

print ("Done!")

