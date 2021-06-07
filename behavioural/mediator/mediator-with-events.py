'''
Mediator with Event
'''
class Event(list):
    '''
    event is basically a list of functions
    you can call when something happens
    '''
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    '''
    Centrally available mediator component
    which is events injected into Player & Coach classes
    player and coaches can subscribe to the events
    '''
    def __init__(self):
        self.events = Event() # anyone can take game.events and subscribe to it.

    def fire(self, args):
        self.events(args) # utility method for firing an event. How to invoke the event so all subscribers get information.

class GoalScoredInfo:
    '''
    Information about who scored goal & how many goals were scored by the player.
    '''
    def __init__(self, who_scored, goals_scored):
        self.who_scored = who_scored
        self.goals_scored = goals_scored

class Player:
    '''
    someone who scores the goal
    '''
    def __init__(self, name, game):
        '''
        :param name: player name
        :param game: Event subscribed to
        '''
        self.game = game
        self.name = name
        self.goals_scored = 0

    def score(self):
        '''
        Method for scoring a goal
        '''
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored) #structure to send off info to event
        self.game.fire(args) # use mediator and fire event on mediator.

class Coach:
    '''
    Coach need to subscribe to the game
    in order to congratulate player
    '''
    def __init__(self, game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        '''
        Coaches celebrate for first 2 goals of player
        afterwards coach stops being impressed.

        If args is an instance of GoalScoredInfo class
        AND goals score is less then 3,
        let coach celebrate
        '''
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done, {args.who_scored}!')

if __name__ == '__main__':
    game = Game()
    player = Player('Sam', game)  # game is mediator
    coach = Coach(game) # let coach subscribe to mediator

    player.score() # player scores a goal
    player.score() # since coach is subscribed to the same mediator as sam, coach will celebrate
    player.score()

    '''
    Essentially game is the mediator component
    and both players and coaches can subscribe to the mediator
    players can generate events within the mediator
    and coaches, via the mediator, can respond to events that take place
    within the game mediator. 
    '''


