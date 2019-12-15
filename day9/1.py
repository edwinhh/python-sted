import flask

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        cls.instance = super().__new__(cls)  #
        return cls.instance

print(Singleton.instance)
a=Singleton()
print(a.instance)
b=Singleton()
print(b.instance)