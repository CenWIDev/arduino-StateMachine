class State:
    StateFn = None
    _stateName = ""
    _transitions = []
    
    def __init__(self, stateName, StateFn):#Need to add stateFn
        self._stateName = stateName
        self.StateFn = StateFn
        
    def __del__(self):
        ClearTransitions()
        
    def ClearTransitions(self):
        for i in range(len(self._transitions)):
            del self._transitions[i]

    def AddTransition(self, to):#Need to add TransitionFn
        self._transitions.append(Transition(to))#finish Transition here

    def Is(self, stateName):
        return self._stateName == stateName

    def Name(self):
        return self._stateName

    def RunState(self):
        if(StateFn != None):
            StateFn()

    def GetNextState(self):
        for i in range(len(self._transitions)):
            t = self._transitions[i]
            if(t.ShouldTransition()):
                return t.To()
        
        
        
        
