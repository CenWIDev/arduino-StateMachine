class State:
    #typedef void (*StateFn)()
    #_f = StateFn()     (or something)
    _stateName = ""
    _transitions = []
    
    def __init__(self, stateName):#Need to add stateFn
        self._stateName = stateName
        
    def __del__(self):
        ClearTransitions()
        
    def ClearTransitions(self):
        for i in range(len(self._transitions)-1):
            del self._transitions[i]

    def AddTransition(self, to):#Need to add TransitionFn
        self._transitions.append(Transition(to))#finish Transition here

    def Is(self, stateName):
        return self._stateName == stateName

    def Name(self):
        return self._stateName

    #add RunState()

    #add GetNextState()
        
        
        
