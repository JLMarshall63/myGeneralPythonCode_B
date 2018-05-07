try:
    x = raw_input("fnum: ")
    y = raw_input("snum: ")
    z = float(x) / float(y)
    print z

except ZeroDivisionError:
    print "You cannot divide by zero."
except TypeError:
    print "Only numbers are valid entries."
except ValueError:
    print "Culd not convert string to float."

try:
    x = raw_input("fnum: ")
    y = raw_input("snum: ")
    z = float(x) / float(y)
    print z

except Exception as e:
    print e

while True:
    try:
        x = raw_input("fnum: ")
        y = raw_input("snum: ")
        z = float(x) / float(y)
        print z
    except:
        print "An exception has occured.  You may have tried to divide by zero or not have entered numeric values. Please try again."
    else:
        break

try:
    x = input("fnum: ")
    y = input("snum: ")
    print x/y

except Exception as e:
    print e.message
    


    