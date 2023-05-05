# second example from following website
# https://appsilon.com/use-r-and-python-together/#:~:text=You%20can%20import%20any%20Python,and%20functions%20declared%20with%20R.&text=And%20that's%20how%20you%20can%20run,in%20R%20and%20R%20Markdown.

from rpy2 import robjects

pi = robjects.r['pi']
print(pi)
print(type(pi))

robjects.r('''
    add_nums <- function(x, y) {
        return(x + y)
    }

    print(add_nums(x = 5, y = 10))
    print(add_nums(x = 10, y = 20))

''')