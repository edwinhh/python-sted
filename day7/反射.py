class Car:

    def run(self):
        print("跑")

    def driver(self, name):
        print("%s在开车" % name)


# print(hasattr(Car,'run1'))
bmw = Car()
func = getattr(bmw,'run')

func()