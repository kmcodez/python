# ********************************
# if __name__ == '__main__':
# ********************************

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# python interpretor sets "special variables", one of which is __name__
# then python will execute the code found within __main__

# python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

print(__name__)

import modules.module_one as mo

print(mo.__name__)

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running this module indirectly")