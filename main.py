import sys
from Parcer import Parcer
from Executor import Executor


from Functions import *

sourceFile = sys.argv[1]
parcer = Parcer(sourceFile)
executor = Executor(parcer)

parcer.parce()
executor.execute()
