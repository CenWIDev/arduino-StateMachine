class Transition:
    #typedef bool (*TransitionFn)()
    _to = ""
    #add TransitionFn

    def __init__(self, to):#add TransitionFn here
        self._to = to
        #self._f = _f

    def __del__(self):

    def ShouldTransition(self):
        shouldTransition = false #needs to be _f() for assignment
        return shouldTransition

    def To(self):
        return self._to
