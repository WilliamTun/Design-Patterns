# Source: https://www.youtube.com/watch?v=woIkysZytSs&t=607s&ab_channel=ArjanCodes

# Tip 1.
No wild card imports

wildcard imports "eg. import *" are bad because: 
- as this will pollute the global variable namespace
- it's not clear what comes from where

# Tip 2. Import package, call module.function
bad: 
```
import my_package.my_module import function 
function(x)
```

good:
```
from my_package import my_module
my_module.function(x)
```

reason:
It makes it easier to trace the function code. 

# Tip 3. Use List comprehensions and generators - only for simple cases!
Why? Because the code becomes harder to understand with complex list comprehensions. 
Having readable code is more important than "efficient code"

# Tip 4. default arguments
use default arguments in function where appropriate - so you don't have to call every argument when calling the function. 

Do NOT have default arguments as mutable data structures.
eg. function(a, b=[])
b is by default of type empty list - which is mutable! 
This leads to strange behaviour!! -> risks BUGS! 

# Tip 5. getters and setters
Getters and setters are an alternative to properties
If getting and setting a property value is complex, getters and setters may be more appropriate.
- see. 10.34 of video for example

# Tip 6. Exception handling
Do not over use try-except statments to handle errors.
If error catch is not useful, just ignore the error. 







