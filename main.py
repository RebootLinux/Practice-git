
def for_function(x):
	for y in range(1, x+1):
            print(y)

def getInput():
    _max = int(input("Give the amount to loop: "))
    for_function(_max)


getInput()
