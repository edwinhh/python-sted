import time,os


D = dict([('name', 'tom'), ('age', 12)])
F={'age': 15}# {'age': 12, 'name': 'tom'}
D.update(F)
print(D)