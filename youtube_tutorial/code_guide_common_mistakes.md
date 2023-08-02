# Source: https://www.youtube.com/watch?v=ZZs0nsNyuqg&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&ab_channel=ArjanCodes


# Common mistake 1: Asking for more data then they need
If the code needs only a specific column from a dataset to run,
do not call in all the columns, read in only the necessary specific column.

# Common mistake 2: Not specific about the type of data you can handle as an argument or return as a result
Avoid writing one function which take take in an argument which allows multiple data types as the input variable.
eg.
def func(s: str | int | byte ) -> bool: 
    ``` xxx ```

instead write multiple functions
def func_str(s: str) -> bool: 
def func_int(s: int) -> bool: 
def func_byte(s: byte) -> bool: 


# Common mistakes 3: be too specific about the type of thing a function accepts
On the other side... 
For example this function:


def func(a: list[str]):
    result = []
    for word in words:
        result.append(len(word))
    return result


- can be improved by adding in more generic inputs like:
- we can also make MORE specific the output return types like:

from typing import Iterable, Sized
def func(a: Iterable[Sized]) -> list[int]:
    result: list[int] = []
    for word in words:
        result.append(len(word))
    return result

Which would make the function more flexible and able to take in sets, lists, etc..
