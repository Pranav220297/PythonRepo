try:
   fh = open("test.txt", "r")
   fh.write("This is my test file for exception handling!!")
except FileNotFoundError:
   print ("Error: can\'t find file or read data")
except NameError:
    print("Hello")
except:
   print("Default exception handler")

