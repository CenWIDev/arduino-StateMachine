from StateMachine import StateMachine
import time

sm = StateMachine()

def State1Behavior():
    print("You are in State 1")

def State2Behavior():
    print("You are in State 2")

def StateTransitionCondition():
    return sm.TimoutSinceLastTransition(.5)

sm.AddState("State1", State1Behavior)
sm.AddState("State2", State2Behavior)
sm.AddTransition("State2", "State1", StateTransitionCondition)
sm.AddTransition("State1", "State2", StateTransitionCondition)

sm.SetCurrentState(sm.GetStateByName("State1"))

print(len(sm._states[0]._transitions))
print(len(sm._states[1]._transitions))

while True:
    nextState = sm.GetNextState()
    #print(nextState)
    if(nextState != None):
        sm.SetCurrentState(sm.GetStateByName(nextState))
    sm.RunCurrentState()
    time.sleep(.25)
