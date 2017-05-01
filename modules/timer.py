import time
import datetime

class Timer(object):
    
    def __init__(self):
        "Initialize the class"
        pass
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start
    
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        
        self.stop = datetime.datetime.now()
        return "Total time: " + str(self.stop - self.start)
    
    def now(self):
        """Returns the current time with a message"""
        
        return "Now: " + ": " + str(datetime.datetime.now())
    
    def elapsed(self):
        """Time elapsed since start was called"""
        
        return "Elapsed: " + str(datetime.datetime.now() - self.start)
