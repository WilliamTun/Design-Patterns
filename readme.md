# Design Patterns

This repo consist of examples of common design patterns used in software engineering. 
It was adapted from the book "Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma, et al".  
On top of reviewing SOLID desing principles, we cover patterns for:
- Creation 
- Structure
- Behaviour 


## Creation
### Builder  
Use several calls to initialise an object. 
Builders can have interfaces for "chaining" calls together.

### Factories
Factory methods are more expressive than simple initialisers. 
Can have several methods with same sets of arguments but differently named. 

### Prototype
Make an object from an existing object, using deep-copy. 

### Singleton 
Ensure 1 instance of a class exists. 
Useful for initialising databases. 
Dependency injection can be useful for unit testing. 


## Structure

## Behaviour 