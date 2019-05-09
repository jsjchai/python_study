#!/usr/bin/python3

import _thread
import time


def run(a, b):
  print("a=%d,b=%d,id=%s\n" % (a, b, _thread.get_ident()))
  time.sleep(100)


_thread.start_new_thread(run, (3, 4))
_thread.start_new_thread(run, (3, 4))

while 1:
  pass
