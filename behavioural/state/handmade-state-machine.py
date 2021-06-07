'''
State Design Pattern

Objects behaviour determined by its state
There is a method to trigger transition from one state to another.
State machine: Formalised construct to manage state & transitions
'''

from enum import Enum, auto

class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(Enum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()

if __name__ == '__main__':
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
            # ^ If you are placed on hold by the trigger, you will be placed on on_hold state
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK) #State.ON_HOOK later declared as exit state
        ]
    }

    # starting state
    state = State.OFF_HOOK

    # exit state
    exit_state = State.ON_HOOK

    while state != exit_state: #if the state becomes exit state, exit the while loop
        print(f'The phone is currently {state}')

        # display all the rules that can be triggered given the state
        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}')

        idx = int(input('Select a trigger'))

        # transition to different state
        s = rules[state][idx][1]
        state = s

    print('we are done using the state machine')