# pypollution
[Python Pypi](https://pypi.org/project/pypollution/)

-----------
pollution is a python library for ploating real time COM port data. This library is project dependent library made for pollution detection and analysis. for more details [Click Here](https://github.com/Pamelabanerjee11/pypollution)

*This library is based on specified Hardware*

Ex:
---
```
import pypollution as plot
import serial.tools.list_ports as ports
import os

print("Available ports : \nPort\t Hardwere")
for i in range(len(ports.comports())):
print(ports.comports()[i])

inputPort = input("\nEnter Ardiuno Port Number : ")
try:
p = plot.pyAnalysis(inputPort, os.path.dirname(__file__))
p.genrateLineAnalysis()
except:
print("An error is occurred while plotting the graph. Probable reason may be :")
print("1. You are running app in read only memory.")
print("2. Check your hardware port(COM port).")
print("3. Wrong port assignment.")
```
