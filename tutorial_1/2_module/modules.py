# module = a file containing python code.May contain functions, classes, etc.
# used with modular programing, which is to operate a program into parts.

# import messages
# messages.hello()
# messages.bye()

# # best practice more safer
# import messages as msg
# msg.hello()
# msg.bye()


# # don't use it in big programs to avoid the functions which have the same names in other modules
# from messages import hello, bye
# hello()
# bye()


# # don't use it in big programs to avoid the functions which have the same names in other modules
# from messages import *
# hello()
# bye()


# to list the available modulesin python
help("modules")
