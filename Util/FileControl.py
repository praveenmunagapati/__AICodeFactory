
def show( name ):
    f = open(name)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")
    f.close()

def write( name, str ):
    f = open( name, 'w')
    f.write( str )
    f.close()