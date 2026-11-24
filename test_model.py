import unittest
from model import Timer
class TestTimer(unittest.TestCase):
    def setUp(self): self.t=0; self.timer=Timer(lambda:self.t)
    def test_focus(self):
        self.timer.begin('focus'); self.t=61; self.timer.update(); self.assertEqual(self.timer.display(),'23:59')
    def test_pause(self):
        self.timer.begin('break'); self.t=10; self.timer.toggle(); self.t=100; self.timer.update(); self.assertEqual(self.timer.remaining,290); self.timer.toggle(); self.t=390; self.timer.update(); self.assertEqual(self.timer.mode,'done')
    def test_reset(self):
        self.timer.begin('focus'); self.timer.reset(); self.assertEqual(self.timer.mode,'idle'); self.assertIsNone(self.timer.deadline)
if __name__=='__main__': unittest.main()
