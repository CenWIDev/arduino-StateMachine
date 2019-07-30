class StateMachine:
    _nStates = 0
    _states = []
    _currentState = None
    _StateLastUpdated = 0

    def __del__(self):
        ClearStates()

    def AddState(self, stateName, StateFn):
        _states.append(State(stateName, StateFn))

    def SetCurrentState(self, newState):
        _currentState = newState
        #_stateLastUpdated =        Need to implement this

    #def SetCurrentState(stateName):

    def GetStateByName(stateName):
        for s in _states:
            if(s.Is(stateName)):
                return s
        return None

    def ClearStates():
        for i in range(len(_states)):
            del _states[i]

    def RunCurrentState():
        if(_currentState == None):
            return
        _currentState.RunState()

    def GetNextState():
        if(_currentState == None):
            return
        return _currentState.GetNextState()

    def AddTransition(self, stateFrom, stateTo, TransitionFn):
        if(stateFrom == "*"):
            return AddTransitionToAll(stateTo, TransitionFn)
        s = GetStateByName(stateFrom)
        if(s != None):
            s.AddTransition(stateTo, TransitionFn)

    def AddTransitionToAll(self, stateTo, TransitionFn):
        for s in _states:
            if(s!=None): # and !s.Is(stateTo)
                s.AddTransition(stateTo, TransitionFn)

    #def TimoutSinceLastTransition(t)
                #return (time-_stateLastUpdated)>t
