def f(a, b, c=False, **kwargs):
    print(a, b, c, kwargs)

f(a=True, b=False, z=False, t='t')

def filter(**lookups):
    for i, j in lookups.items():
        print(i.split('__'), j)

filter(name__startswith='vin', age__lt=23, city__endswith='rechal')
# isso é utilizado para consultas no django

