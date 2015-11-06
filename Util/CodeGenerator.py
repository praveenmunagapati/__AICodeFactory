import random

def generate( lineLengthLimit, lineLimit ):

    poem = '''\
print( "Hello World!" )
a = input( "Press ENTER to continue" )\
'''

    letters = ['a','b','c','d','e','f','g','h','i','j',
               'k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J',
               'K','L','M','N','O','P','Q','R','S','T',
               'U','V','W','X','Y','Z',
               '(',')','"',' ','=','!',
               '\n', '\t']

    parts1 = [ 'print( ', 'a = input( ' ]
    parts2 = [ "'Hello World!'", "'Press ENTER to continue'" ]
    parts3 = [ ' )\n' ]

    countLine = 0
    countLength = 0
    rlt = ''
    while countLine < lineLimit:
        str = ''
        if countLength >= lineLengthLimit:
            str = '\n'
        else:
            str = random.choice( parts1 ) + random.choice( parts2 ) + random.choice( parts3 )
        if str.rfind('\n') != None:
            countLine += 1
            countLength = 0
        rlt += str
        countLength += 1

    return rlt
