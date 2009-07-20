import py2ecotect
from py2ecotect import string_util

class Timer(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    def restart(self):
        """
        
        Restarts the internal timer. The count property continues from it's 
        last value. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("timer.restart")
    
    def start(self):
        """
        
        Starts the internal timer, resetting the count property to zero. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("timer.start")
        
    def stop(self):
        """
        
        Stops the internal timer. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("timer.stop")
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_count(self):
        """
        
        Retrieves the number of times the OnTimer(count) event has been 
        triggered since it was first started. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of times the timer has triggered since it was started. 
        
        """
        val = py2ecotect.conversation.Request("get.timer.count")
        return string_util._convert_str_to_type(val, int)

    def set_count(self, count):
        """
        
        Sets the counter value for the number of times the OnTimer(count) event 
        has been triggered since it was first started. 

        Parameter(s)
        This property takes the following parameters.
        
        count 
        The number of timer triggers to report.
        
        """
        arg_str = string_util._convert_args_to_string("set.timer.count", count)
        py2ecotect.conversation.Exec(arg_str)     

    def get_interval(self):
        """
        
        Retrieves the timer interval in milliseconds. This is basically the 
        time gap between each calling of the OnTimer(count) event. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        msec 
        The number of milliseconds (thousandths of a second) between each 
        triggerering of the timer. Thus, a value of 1000 would mean one call 
        every second.
        
        """
        val = py2ecotect.conversation.Request("get.timer.interval")
        return string_util._convert_str_to_type(val, int)

    def set_interval(self, msec):
        """
        
        Sets the timer interval in milliseconds between each calling of the 
        OnTimer(count) event. 

        Parameter(s)
        This property takes the following parameters.
        
        msec 
        The number of milliseconds (thousandths of a second) between each 
        triggerering of the timer. Thus, a value of 1000 would mean one call 
        every second. The minimum time gap you can set is 50 milliseconds 
        (20 times per second). 
        
        """
        arg_str = string_util._convert_args_to_string("set.timer.interval", msec)
        py2ecotect.conversation.Exec(arg_str)

    def get_running(self):
        """
        
        Retrieves a value that shows whether the timmer is currently running or 
        not. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        running 
        This is a boolean value where 1 means running and 0 means stopped. 

        """
        val = py2ecotect.conversation.Request("get.timer.running")
        return string_util._convert_str_to_type(val, int)

    def set_running(self, running):
        """
        
        Sets the status of the timer to running or not. Sending 0 or false is 
        the same as calling timer.stop whilst 1 or true is the same as calling 
        timer.restart. 

        Parameter(s)
        This property takes the following parameters.
        
        running 
        This is a boolean value where 1 or true sets the timer running and 0 or 
        false stops it. 
        
        """
        arg_str = string_util._convert_args_to_string("set.timer.running", 
                                                      running)
        py2ecotect.conversation.Exec(arg_str)

    count= property(fget = get_count, fset = set_count, 
                        doc = "The number of times the OnTimer(count) event has"
                        " been triggered since it was first started")
    
    interval = property(fget = get_interval, fset = set_interval, 
                        doc = "The timer interval in milliseconds. This is"
                        " basically the time gap between each calling of the"
                        " OnTimer(count) event")
    
    running = property(fget = get_running, fset = set_running, 
                        doc = "A value that shows whether the timmer is"
                        " currently running or not")



    
if __name__ == "__main__":
    x = Timer()
    
    
    #print x.get_count()
    #x.set_count(12)
    #print x.get_interval()
    #x.set_interval(55)
    #print x.get_running()
    #x.set_running(0)
    #x.start()
    #print x.running
    #x.running = 1
    

    print "Tests completed"