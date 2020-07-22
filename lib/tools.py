
class Printer():

    def __init__(self):
        pass

    @staticmethod #I forget, what is the purpose of a static method?
    def output(string):
        #lines = []
        for x in string:
            print(x, end='', flush=True)
        sleep (0.1) # switch to one after debugging.
    print()

    #def output_fast(string):
        #for x in string:
            #print (x, end='', flush=True)
        #sleep(0.1)
    #print()
