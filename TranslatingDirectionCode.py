# Porgramming in Python, by Mohammed Alhamid
#
""" Making a prototype of translating a direction code recieved from a GPS sensor."""


def direction(x):
    """ Returns the associated intersection instruction string.
    PreC: x is an intersection string.
    """
    if x[0]==x[1]:
        M = 'Continue Straight'
    elif x=='ES' or x == 'SW' or x == 'WN' or x=='NE':
        M = 'Turn Right'
    elif x=='EN' or x == 'NW' or x == 'WS' or x=='SE':
        M = 'Turn Left'
    elif x=='EW' or x == 'WE' or x == 'NS' or x=='SN':
        M = 'Make a U-Turn'
    else:
        M = 'Pull Over'
    return M


# Helper function for alternate implementation of SiriSez
def code(d):
    """ d is a direction string 'N', 'E, 'S', 'W'.
     code(d) returns 0, 1, 2, or 3, respectively, to allow for "direction arithmetic".
     Returns None otherwise."""

    if d == 'N':
        return 0
    elif d == 'E':
        return 1
    elif d == 'S':
        return 2
    elif d == 'W':
        return 3


def SiriSez2(x):
    """Returns the associated intersection instruction string.
    PreC: x is an intersection string."""
    # Alternate implementation

    # convert directions into numbers in {0,1,2,3}
    dir1=code(x[0])
    dir2=code(x[1])

    if dir1 == dir2:
        return 'Continue Straight'
    elif dir2 == ((dir1 + 1) % 4): # use modular arithmetic
        return 'Turn Right'
    elif dir2 == ((dir1 + 2) % 4):
        return 'Make a U-Turn'
    else:
        return 'Turn Left'


def TripAdvisor(Route):
    print ()
    print (Route)
    if Route[0] == 'N':
        print ('Start Driving North')
    elif Route[0] == 'W':
        print ('Start Driving West')
    elif Route[0] == 'S':
        print ('Start Driving South')
    else:
        print ('Start Driving East')
    print (direction(Route[0:2]))
    print (direction(Route[1:3]))
    print (direction(Route[2:4]))
    print (direction(Route[3:5]))
    print (direction(Route[4:6]))
	
	#for i in range((len(Route)-1)):
		#print (direction(Route[i:i+2]))

if __name__ == '__main__':
    Route = input('Enter a length-6 route string: ')
    #Route = Fix(Route)
    TripAdvisor(Route)














