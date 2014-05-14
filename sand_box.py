import getopt
import sys
from datetime import datetime

def main():
    start_date = datetime(2014, 05, 15)
    END_DATE = datetime(2015, 05, 15)
    DAY_DELTA = 7
    WAIT_TIME = 40
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:e:d:t:h", ["Start Date", "End Date", "Day Delta", "Wait Time"])

    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'This is my help string'
        elif opt == '-s':
            print arg
            print 'hello'
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()