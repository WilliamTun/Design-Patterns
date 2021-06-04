'''
Neural networks

Some composed and singular objects need to have similar/identical behaviour
In this example,the Composite design pattern lets scalar objects (Neurons) and collections (Neuron layers)
to have similar behaviours. The scalar objects can act as a collection

Python supports iteration with __iter__
which permits composite design pattern
by allowing a single object to make itself iterable
by:
    def __iter__(self):
        yield self

^ So you can turn a single object, into use iteration to produce a collection of objects.
'''

class Neuron:
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    # __str__ allows you to define what is printed if print(Neuron) is called.
    def __str__(self):
        return f'{self.name}:\n{len(self.inputs)} inputs,\n{len(self.outputs)} outputs'

    '''
    This __iter__ function is key to composition
    Because of this, you can call the connect_to function 
    on both Neuron and Neuron Layer
    '''
    # Turn a scalar value to collection of one element
    def __iter__(self):
        yield self

class NeuronLayer(list):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'

def connect_to(self, other):
    if self == other: # you cannot connect to yourself
        return

    for s in self:
        for o in other:
            s.outputs.append(o)
            o.inputs.append(s)



if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    Neuron.connect_to = connect_to
    NeuronLayer.connect_to = connect_to

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)


