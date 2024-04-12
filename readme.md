# Python tutorial for begginners 
### <a href="https://www.python.org">Official Website</a>
### <a href="https://www.python.org/downloads">Download</a>
<hr/>

## First program

```python
  print("Hello, World!");
```
 ### Internal working of python
 <img src="https://miro.medium.com/max/1200/1*1athPfdP9St4mkB_hElM6g.png" alt="Internal working"/>

 #### Byte Code:
 - These are written in lower level language.
 - Platform independent code but requires python virtual machine to run program.
 - Runs faster
 - Create a new file with extension of .pyc
 - Are mostly hidden from the user.
 - Also called as frozen binaries but cannot be run directly on cpu for than they have to create a .exe file

 ##### \_\_pycache\_\_ 
 - Is a directory containing .pyc files that is created only for imported files.
 - .pyc files are named as \<filename>.cpython-version.pyc

- Filename: hello_chai.py
 ```python
 def chai(n):
  print(n);
 ```
- Main.py file
```python
from hello_chai import chai
chai("ginger tea")
```
- just run the above program
- this will generate `__pycache__` directory with `hello_chai.cpython-version.pyc`


#### Python Virtual Machine
Python virtual machine is a software program for python programming which: 

+ Has a code loop to iterate byte code and python scripts
+ Also called as `runtime engine`.
+ Also known as `Python Interpreter`

``` Note
Byte code is not machine code
- Used for only python specific interpretations
- cpython, jython, IronPython, Stackless, PyPy and there are many different implementations of python
- cpython is an standard implementation of python.
```

### Python in shell
With windows installation python provide an interpreter that is known `IDLE`. 
We can use python shell to interact with the interpreter and here we can test our program logic, functions and use as a simple calculator for basic calcultation

### How to use python shell

In Windows
``` bash 
python
```
In Mac/Linux
``` bash
python3
```

### Mutable and Immutable
- Mutable means that you can change the values of the data stored inside the variables.
- List, Set, Dictionary, ByteArray, and Array are mutable data types.
- Immutable means that you can never change the values of the data stored inside the variables.
- Integer, FloatingPoint numbers, Booleans, Strings, Tuples, Frozenset and Bytes are immutable data types.

### Datatypes
Also known as Object types in python as everything is an object in Python.

1- `Numbers`:
```
1234, 3.1459, 3+4j, 0b111, Decimal(), Fraction()
```
2- `String` : 
```
'spam', "Bobs's" b'a\x01c', u'sp\xc4m'
```
3- `List` : 
```
[1, [2, 'three], 4.5], list(range(10))
```
4- `Tuple` : 
```
(1, 'spam', 4, 'U'), tuple('spam'), namedTuple
```
5- `Dictionary` : 
```
{'food;: 'spam', 'taste': 'yum'}, dict(hours=10)
```
6- `Set` : 
```
set('abc'), {'a','b','c'}
```
7- `File` :
```
open('eggs.txt'), open(r'C:\ham.bin', 'wb')
```
8- `Boolean` : 
```
True, False
```
9- `None`: 
```
None
```
10- `functions, modules, classes`

11- `Advanced: Decorators, Generators, Iterators, Meta Programming`
