numbers = []

def get_user_input():
    number_to_try = raw_input("What would you like to try? >")
    return int(number_to_try)

def do_weird_number_stuff(upper_boundary):
    
    i = 0
    while i < upper_boundary:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

try_this = get_user_input()
do_weird_number_stuff(try_this)

