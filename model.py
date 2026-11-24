import time, math
class Timer:
    def __init__(self,clock=time.monotonic): self.clock=clock; self.reset()
    def reset(self): self.mode='idle'; self.remaining=0; self.deadline=None
    def begin(self,mode):
        self.mode=mode; self.remaining={'focus':1500,'break':300}[mode]; self.deadline=self.clock()+self.remaining
    def update(self):
        if self.deadline is not None:
            self.remaining=max(0,self.deadline-self.clock())
            if self.remaining==0: self.mode='done'; self.deadline=None
    def toggle(self):
        self.update()
        if self.mode not in ('focus','break'): return
        if self.deadline is None: self.deadline=self.clock()+self.remaining
        else: self.deadline=None
    def display(self):
        n=math.ceil(self.remaining); return f'{n//60:02d}:{n%60:02d}'
