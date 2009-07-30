import py2ecotect as p2e

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
        p2e.conversation.Exec("timer.restart")
    
    def start(self):
        """
        
        Starts the internal timer, resetting the count property to zero. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("timer.start")
        
    def stop(self):
        """
        
        Stops the internal timer. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("timer.stop")
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def count():
        def fget(self):
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
            val = p2e.conversation.Request("get.timer.count")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, count):
            """
            
            Sets the counter value for the number of times the OnTimer(count) event 
            has been triggered since it was first started. 
    
            Parameter(s)
            This property takes the following parameters.
            
            count 
            The number of timer triggers to report.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.timer.count", count)
            p2e.conversation.Exec(arg_str)     
        
        return property(**locals())
    
    @apply
    def interval():
        def fget(self):
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
            val = p2e.conversation.Request("get.timer.interval")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, msec):
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
            arg_str = p2e._util._convert_args_to_string("set.timer.interval", msec)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def running():
        def fget(self):
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
            val = p2e.conversation.Request("get.timer.running")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, running):
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
            arg_str = p2e._util._convert_args_to_string("set.timer.running", 
                                                          running)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())

    
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
