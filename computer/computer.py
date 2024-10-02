class Computer(object):
    def display(self):
        temp = vars(self)
        for i in temp:
            print("Feature {} : {}".format(i, temp[i]))