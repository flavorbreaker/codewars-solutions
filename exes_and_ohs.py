# https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python
# Program designed to return true if the number of x's in a string is equal to the number of o's, and return false otherwise. The program was required to be case-insensitive.

s = "xxxxxoooo"             # expect false
# xo = "xxxooo"              # expect true
# xo = "znbadsodsjklfax"     # expect true


def xo(s):                  # create xo function passing parameter s
    s = s.lower()           # sets s to all lowercase

    x_count = 0             # creates variable to hold count of x's
    o_count = 0             # creates variable to hold count of o's
    
    for l in s:             # loops over every index in s
        if l == 'x':
            x_count += 1    # adds 1 to x_count if l is an 'x'
        if l == 'o':
            o_count += 1    # adds 1 to o_count if l is an 'o'

    return x_count == o_count   # returns true if x_count is equal to o_count, otherwise returns false