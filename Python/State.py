from Transition import Transition

class State:
    
    def __init__(self, stateName, StateFn):
        self._stateName = stateName
        self.StateFn = StateFn
        self._transitions = []
        
    def __del__(self):
        ClearTransitions()
        
    def ClearTransitions(self):
        for i in range(len(self._transitions)):
            del self._transitions[i]

    def AddTransition(self, to, TransitionFn):
        self._transitions.append(Transition(to, TransitionFn))

    def Is(self, stateName):
        return self._stateName == stateName

    def Name(self):
        return self._stateName

    def RunState(self):
        if(self.StateFn != None):
            self.StateFn()

    def GetNextState(self):
        for i in range(len(self._transitions)):
            t = self._transitions[i]
            if(t.ShouldTransition()):
                #print("GetNextState() is returning a new state")
                return t.To()
        #If no transitions, next state is the current state
        return self._stateName
        
        
        
        
