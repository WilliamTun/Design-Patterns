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

### Facade
Attempt to hide low level code, but still give user-friendly options to access low level features. Can be combined with permissions for power-users.

### Flyweight
Save large numbers of similar objects without storing them in memory to make memory utilisation more efficient.

### Proxy 
A surrogate object that forwards calls to real object, whilst performing additional functions. Various types of proxy exist such as for access control, communication and logging. 


## Behaviour 
### Chain of Responsibility
Allows processing information/events in a chain. 

### Command
Encapsulates a request into a separate object. Each request is packaged, sent to a central authority and the request gets processed. Good for adding funcationality to do with Audits, replays, undo/redo. Suitable for a set of sequenced events. Abides by good practise of SEPARATION of commands & queries. Good for database processing systems and favours EVENTUAL consistency over immediate consistency. 

### Memento
Tokens to allow access to various system states back and forward through time. Also good for replays & undo/redo. 

### Interpretor
Transforms text input into Object orientated structures. 

### Iterator
Provides interface for accessing elements of an aggregate object. 

### Mediator
Provide messaging between two objects eg. Message passing & chatroom

### Observer
Allows notifications of changes in a component

### State Machines 
Model systems by having one of possible states and transition between states. 





