import subprocess

def tryAgain( filename ):
    isGoodTry = True
    try:
        subprocess.check_call( "python "+ filename )
        # os.system("python " + filename)
    except:
        isGoodTry = False
        pass
    return isGoodTry