import tkinter as tk
import time, math, random
from model import Timer

KEY='#ff00ff'
class Pet:
    def __init__(self):
        self.root=tk.Tk(); self.root.title('Desktop Pet'); self.root.overrideredirect(True)
        self.root.attributes('-topmost',True); self.root.configure(bg=KEY)
        if self.root.tk.call('tk','windowingsystem')=='win32': self.root.attributes('-transparentcolor',KEY)
        self.root.geometry(f'240x240+{max(0,self.root.winfo_screenwidth()-270)}+{max(0,self.root.winfo_screenheight()-320)}')
        self.c=tk.Canvas(self.root,width=240,height=240,bg=KEY,highlightthickness=0); self.c.pack()
        self.timer=Timer(); self.start=time.monotonic(); self.blink_at=self.start+3; self.blink_end=0; self.drag=None; self.last_pointer=None; self.last_activity=self.start
        self.menu=tk.Menu(self.root,tearoff=False)
        for label,fn in [('Iniciar foco',lambda:self.timer.begin('focus')),('Iniciar pausa',lambda:self.timer.begin('break')),('Pausar / continuar',self.timer.toggle),('Voltar ao repouso',self.timer.reset),('Fechar',self.root.destroy)]: self.menu.add_command(label=label,command=fn)
        self.c.bind('<ButtonPress-1>',self.grab); self.c.bind('<B1-Motion>',self.move); self.c.bind('<ButtonRelease-1>',self.release); self.c.bind('<Button-3>',self.popup); self.root.bind('<Escape>',lambda e:self.root.destroy())
        self.draw(); self.root.mainloop()
    def grab(self,e): self.drag=(e.x_root,e.y_root,self.root.winfo_x(),self.root.winfo_y())
    def move(self,e):
        if self.drag:
            x,y,rx,ry=self.drag; self.root.geometry(f'{rx+e.x_root-x:+d}{ry+e.y_root-y:+d}')
    def release(self,e): self.drag=None
    def popup(self,e):
        try:self.menu.tk_popup(e.x_root,e.y_root)
        finally:self.menu.grab_release()
    def draw(self):
        now=time.monotonic(); self.timer.update(); c=self.c; c.delete('all')
        px,py=self.root.winfo_pointerxy()
        if (px,py)!=self.last_pointer: self.last_activity=now; self.last_pointer=(px,py)
        asleep=now-self.last_activity>60 and self.timer.mode=='idle'
        if now>=self.blink_at: self.blink_end=now+.14; self.blink_at=now+random.uniform(2.5,5.5)
        dy=math.sin((now-self.start)*2)*2
        def oval(x,y,w,h,**kw): c.create_oval(x,y+dy,x+w,y+h+dy,**kw)
        # Original rounded robot design, drawn entirely with vector primitives.
        oval(52,180,136,19,fill='#334155',outline='')
        c.create_line(120,49+dy,120,30+dy,fill='#64748b',width=5); oval(113,19,14,14,fill='#68e0ce',outline='')
        oval(76,139,88,61,fill='#dbe7ef',outline='#64748b',width=2)
        oval(36,67,168,99,fill='#e7eff6',outline='#64748b',width=2)
        oval(48,76,144,79,fill='#182637',outline='')
        dx=max(-7,min(7,(px-self.root.winfo_rootx()-120)/40)); ey=max(-4,min(4,(py-self.root.winfo_rooty()-115)/40))
        for x in (89,151):
            if asleep or now<self.blink_end: c.create_line(x-12,111+dy,x+12,111+dy,fill='#83f2db',width=4,capstyle='round')
            elif self.timer.mode=='done': c.create_text(x,110+dy,text='★',fill='#ffe080',font=('Segoe UI Symbol',25))
            else: oval(x-10+dx,96+ey,20,29,fill='#83f2db',outline='')
        c.create_arc(109,116+dy,131,137+dy,start=200,extent=140,style='arc',outline='#83f2db',width=3)
        label={'idle':'Zzz' if asleep else 'Pronto','focus':self.timer.display(),'break':self.timer.display(),'done':'Concluído!'}[self.timer.mode]
        c.create_text(120,173+dy,text=label,fill='#24364b',font=('Segoe UI',10,'bold'))
        self.root.after(100 if asleep else 40,self.draw)
if __name__=='__main__': Pet()
