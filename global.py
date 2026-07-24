
def display():
    a=10
    def show():
        global a
        a=15
        print(a)
    show()
    print(a)
display()
print(a)