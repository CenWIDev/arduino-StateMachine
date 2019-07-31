from .. import StateMachine

sm = StateMachine.StateMachine()

def State1Behavior(self):
    print("You are in State 1")

def State2Behavior(self):
    print("You are in State 2")

sm.AddState("State1", State1Behavior)
sm.AddState("State2", State2Behavior)

sm.SetCurrentState("State1")
sm.RunCurrentState()
