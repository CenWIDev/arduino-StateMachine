class Transition:
    TransitionFn = None
    _to = ""

    def __init__(self, to, TransitionFn):
        self._to = to
        self.TransitionFn = TransitionFn

    def ShouldTransition(self):
        shouldTransition = self.TransitionFn()
        return shouldTransition

    def To(self):
        return self._to
