#class NextStateException(Exception):
 #   pass

__doc__='''Classes responsaveis pelo controle da maquina de estados bem como a troca de estados'''

class NextState(object):
	def __init__(self,*params):#next_state,game=None):
		#self.next_state = next_state
		#self.game = game
		self.params = params
	def setNext(self,next):
		self.next_state = next

class State(object):
    '''classe abstrata'''
    def __init__(self):
        self.initialized = False

    def enter(self,*params):
        pass

    def exit(self):
        pass

    def event_handler(self):
        pass


class StateMachine(object):
    '''Maquina de estados'''

    def __init__(self, states):
        self.states = states
        self.current_state = None

        if self.states:
            self.current_state = self.states[0]
            self.states[0].enter()

    def next_state(self,params):
        self.current_state.exit()
        args = (params[1],params[2])


        self.current_state = self.states[params[0]]#next]
        self.current_state.enter(args)

    def previous_state(self):
        state_index = self.states.index(self.current)
        previous = (state_index - 1)
        if previous == -len(self.states):
            previous = 0
        return self.states[next]

    def get_handler(self):
        if self.current_state:
            return self.current_state.event_handler()
        else:
            pass

    def handle_events(self):
        handler = self.get_handler()

        if 'list' in str(type(handler)):
            pass

        elif handler.__class__.__name__ == 'NextState':
            self.next_state(handler.params)



def make_state_machine(*states):
    return StateMachine(list(states))
