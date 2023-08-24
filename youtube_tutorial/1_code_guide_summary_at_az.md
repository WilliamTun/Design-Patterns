# Coding Best practices

# === Writing Functions Guide =======

1. Use type hints
```
# bad
def func(x)

# good
def func(x: str) -> str:
```

2. Add default values to function parameters when appropriate
```
def func(x: str = "x") -> str:
```

3. Generalise type hints when appropriate. 
eg. Iterable is better than list or sets, since it can take in both.
```
# ok
def func(x: List[str]) -> str:

# good
def func(x: Iterable[str]) -> str:
```

4. The name of a function should be a verb. Function parametes should be nounds.

5. A function should have a SINGLE task.

6. Do not use parameters to be used as boolean flags. If boolean flag parameters are present, this indicates we should have two separate functions instead. 

```
# bad
def func(flag: bool):
    if flag == true:
        do something x
    else:
        do something y


# good
def func_x():
    do_something_x

def func_y():
    do_something_y
```

7. A function should not have more than 3 parameters. If a function requires many parameters, consider holding the parameter values in a class and passing in the class object instead

```
# bad
def func(u, v, w, x, y, z):

# good
class func_input:
    def __init__(self, u, v, w, x, y, z):
        self.u = u 
        self.v = v
        self.w = w
        self.x = x
        self.y = y
        self.z = z

def func(in: func_input):
```

# ==== Code Documentation Guide =======

1. Minimize the amount of comments and doc strings written by writing clear concise code with good namng conventions

2. Categorize comments
```
a - todos                    # TODO
b - alerts                   # ! deprecated method
c - highlights               # * IMPORTANT
d - queries                  # > should this method be exposed?
e - parameters               # @param MyParameter
f - commented out code       #

3. Doc strings

```
class X:
    ```
    __description__

    Parameters
    ----------
    @param1: description
    @param2: description
    ```
```

```