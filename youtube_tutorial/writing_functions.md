
# Writing Functions: https://www.youtube.com/watch?v=yatgY4NpZXE&ab_channel=ArjanCodes

# 1. Functions perform a SINGLE task
... but single task functions can contain "soft tasks". 
     eg. 1) LOOP through an iterable list/set
         2) apply an operation per item 
... all logic should be on same level of abstraction
    If the second step of applying an operation to each item of the loop is
    too complicated, move step 2 to a separate function. 

# 2. Do not pass unnecessary information into a function. 

ie. Let's say we have a class with 10 class variables
    and a function that requires 3 of those class variables.
    1) do NOT pass the entire class into the function as input
    
    bad:
    def function(x: MyClass):
        do_something(x)

    2) create the function so that the input is only the 3 class variables. 

    good:
    def function(a: str, b: int, c: bool):
        do_something(a)
        do_something(b)
        do_something(c)


# 3. If a function has parameter names, make sure to call those names when calling the function
    function(a = "hey", b=2, c=True)

# 4. Keep number of parameters in a function minimal
    every parameter we add to a function,
    the greater the complexity of understanding the function

    Remedy 1:
    provide default values - so atleast the multi-parameter function 
                             is easier to read when it is called
    

    Remedy 2:
    introduce an abstraction - create a class that contains all the parameter variables
    and pass in the abstraction to the function! 
    ... so the function can take in a single parameter of type [the abstraction you made]


# 5. If we have a function that hypothetically takes in like hundreds of parameters
     ... apply Remedy 2 again - make the input an abstraction like a class
     ... have the class hold the parameters as class variables...
     ... but then, split the class variables to sub-groups, 
         and put the subgroups into their own abstract classes...    
    ... this is a "class within a class" approach to deal with extreme scenarios like this.


# 6. Don't use BOOLEAN flag parameters
     Do not have a boolean parameter...
     do NOT have an IF-ELSE statement in the function... 
     so that one block is applied IF boolean = true
     and another block is applied ELSE boolean = false. 

     This is usually an indication that the function SHOULD BE SPLIT INTO TWO FUNCTIONS. 

     ... one function for the TRUE block
     ... one function for the FALSE block. 


# 7. Remember functions are OBJECTs.
     so functions can be passsed into other functions as an argument
     and functions can be returned from a function. 

    - see 21:26 of the video:
    ``` 
     from typing import Callable 
     from functools import partial
    ```

# 8. naming convetions 
     function name should be a verb
     func argument should be a noun

     keep names short




