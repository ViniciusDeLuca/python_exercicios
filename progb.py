print('Begin fB', __name__)
from proga import fA

print('Define fB')
def fB():
    print('Dentro fB')
    fA()

print('Chama fB')
fB()


print('End fB', __name__)