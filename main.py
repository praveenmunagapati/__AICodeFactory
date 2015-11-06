import os
from Util import FileControl
from Util import CodeGenerator
from Util import TryTest
import pexpect

NAME_OF_GENERATED_FILE = '__generated.py'

filename = NAME_OF_GENERATED_FILE


hasGoodTry = False
while hasGoodTry is False:
    str = CodeGenerator.generate( 30, 5 )
    FileControl.write( filename, str )
    hasGoodTry = TryTest.tryAgain( filename )

FileControl.show( filename )

# child = pexpect.spawn( filename )
# child.expect( '.*' )
# child.sendline( 'aaa\n' )
