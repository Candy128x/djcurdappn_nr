import sys
import django


print('python-version =')
print(sys.version)


print('\nDjango version =')
print(django.get_version())


'''
op:
python-version =
3.7.3 (default, Jul  6 2019, 19:58:31) 
[GCC 5.4.0 20160609]

Django version =
2.2.3
'''