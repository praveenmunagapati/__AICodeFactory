import os
from Util import FileControl
from Util import CodeGenerator
import pexpect

NAME_OF_GENERATED_FILE = '__generated.py'

filename = NAME_OF_GENERATED_FILE

str = CodeGenerator.generate()

FileControl.write( filename, str )


FileControl.show( filename )

print("\n=========================")

os.system("python " + filename)

# child = pexpect.spawn( filename )
# child.expect( '.*' )
# child.sendline( 'aaa\n' )
