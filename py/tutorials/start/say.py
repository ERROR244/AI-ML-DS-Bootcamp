import sys
from sayings import goodbye

if (len(sys.argv)) != 2:
    sys.exit()

goodbye(sys.argv[1])