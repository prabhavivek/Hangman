#
# Colors
#

endc = '\033[0m'
magenta = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
bold = '\033[1m'
underlne = '\033[4m'
black = '\033[98m'

def get(col, msg):
    return col + msg + endc
