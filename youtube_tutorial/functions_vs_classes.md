# Functions vs classes https://www.youtube.com/watch?v=txRTzljmV0Q&ab_channel=ArjanCodes


Functions (Flow action based):
* organise programme around how data flows + what you do with the data
* functions are ACTION FOCUSED.
- functions has inputs + logic + outputs
- can pass outputs of one function to another
- functional languages like haskell allows passing functions to functions

Rule of thumb:
functional programming is better
1. code is broken into bitesized functions
2. code is easier to test
3. great for processing data in a sequence - eg. ETL pipelines

Objects (State based):
* organise programme around how information is STRUCTURED
- languages like java are object orientated
- groups variables into objects, 
  which are in an hierachical ontology of related objects
- inheritance can extend object definitions
- all objects represent the STATE of the application
- methods can modify the state of the application
- data structures like named tuples are good for this style

Example use cases for object orientated:
1. Bank account - have states (bank balance) that change over time 
                  methods: DEPOSIT + WITHDRAWAL + TRANSFER

