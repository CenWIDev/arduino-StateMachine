from State import State

class StateMachine:
    _nStates = 0
    _states = []
    _currentState = None
    _StateLastUpdated = 0

    def __del__(self):
        ClearStates()

    def AddState(self, stateName, StateFn):
        self._states.append(State(stateName, StateFn))

    def SetCurrentState(self, newState):
        self._currentState = newState
        #_stateLastUpdated =        Need to implement this

    #def SetCurrentState(stateName):

    def GetStateByName(stateName):
        for s in self._states:
            if(s.Is(stateName)):
                return s
        return None

    def ClearStates():
        for i in range(len(_states)):
            del self._states[i]

    def RunCurrentState():
        if(self._currentState == None):
            return
        self._currentState.RunState()

    def GetNextState():
        if(self._currentState == None):
            return
        return self._currentState.GetNextState()

    def AddTransition(self, stateFrom, stateTo, TransitionFn):
        if(stateFrom == "*"):
            return AddTransitionToAll(stateTo, TransitionFn)
        s = GetStateByName(stateFrom)
        if(s != None):
            s.AddTransition(stateTo, TransitionFn)

    def AddTransitionToAll(self, stateTo, TransitionFn):
        for s in self._states:
            if(s!=None): # and !s.Is(stateTo)
                s.AddTransition(stateTo, TransitionFn)

    #def TimoutSinceLastTransition(t)
                #return (time-_stateLastUpdated)>t
