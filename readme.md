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
### Adapter 
Adapts one interface to another interface, perhaps for dealing with different input data structures

### Bridge
Decouples abstraction from implementation. For example, if Colour and Shape were two abstract base classes that is combined to make an object, there would be many combinations of colors (red, blue, yellow etc) that can be combined with shapes (circle, square, star).
In order to avoid cartesian product explosion, use the bridge pattern.   

### Composit
Giving individual components within an aggregation of components, identical interfaces so they can all be treated uniformly. For example, giving both individual neurons and layers of neurons within an ANN, the ability to call the connect_to method. 

### Decorator
Attach additional responsibility to objects without directly modifying objects. 


## Behaviour 