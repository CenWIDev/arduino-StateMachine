from State import State
from time import time

class StateMachine:

    def __init__(self):
        self._nStates = 0
        self._states = []
        self._currentState = None
        self._stateLastUpdated = 0.0

    def __del__(self):
        ClearStates()

    def AddState(self, stateName, StateFn):
        self._states.append(State(stateName, StateFn))

    def SetCurrentState(self, newState):
        if(newState == self._currentState):
            return
        self._currentState = newState
        self._stateLastUpdated = time()
        print("Just changed to state: " + self._currentState.Name())

    #def SetCurrentState(stateName):

    def GetStateByName(self, stateName):
        for s in self._states:
            if(s.Is(stateName)):
                return s
        return None

    def ClearStates(self):
        for i in range(len(_states)):
            del self._states[i]

    def RunCurrentState(self):
        if(self._currentState == None):
            return
        self._currentState.RunState()

    def GetNextState(self):
        #print("as of StateMacine.GetNextState(), _currentState = " + self._currentState.Name())
        if(self._currentState == None):
            return
        return self._currentState.GetNextState()

    def AddTransition(self, stateFrom, stateTo, TransitionFn):
        if(stateFrom == "*"):
            return AddTransitionToAll(stateTo, TransitionFn)
        s = self.GetStateByName(stateFrom)
        if(s != None):
            s.AddTransition(stateTo, TransitionFn)

    def AddTransitionToAll(self, stateTo, TransitionFn):
        for s in self._states:
            if(s!=None and not s.Is(stateTo)):
                s.AddTransition(stateTo, TransitionFn)

    def TimoutSinceLastTransition(self, t):
        return (time() - self._stateLastUpdated)>t
        #return True
