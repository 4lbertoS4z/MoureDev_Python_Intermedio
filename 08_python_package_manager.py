### Python Package Manager ###

# PIP https://pypi.org

# pip3 install pip
# pip3 --version

# pip3 install numpy
import pandas
from mypackage import arithmetics
import requests
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip3 install pandas

# pip3 list
# pip3 uninstall pandas
# pip3 show numpy

# pip3 install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package


print(arithmetics.sum_two_values(1, 4))