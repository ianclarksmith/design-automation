import py2ecotect
from py2ecotect import StringUtil

class Zone(object):
    
    def delete(self, zone):
        """
        
        Use this method to delete the specified zone and all the objects it 
        contains. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index of the zone to delete.
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.delete", zone)
        py2ecotect.conversation.Exec(arg_str)
    
    def extrude(self, zone, dx, dy, dz):
        """
        
        Extrudes the FLOOR object(s) in the specified zone a distance of 
        (dx, dy, dz) in the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.extrude", zone, dx, 
                                                     dy, dz)
        py2ecotect.conversation.Exec(arg_str)

    def isolate(self, zone):
        """
        
        Hides all other zones and isolates the specified zone within the current 
        view. Effectively the same as interactively pressing the F4 key. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index of the zone to isolate. 

        """
        arg_str = StringUtil._convert_args_to_string("zone.isolate", zone)
        py2ecotect.conversation.Exec(arg_str)

    def move(self, zone, dx, dy, dz):
        """
        
        Moves all objects in the specified zone a distance of dx , dy and dz in 
        the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates.
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.move", zone, dx, dy, 
                                                     dz)
        py2ecotect.conversation.Exec(arg_str)

    def nudge(self, zone, dir):
        """
        
        Nudges the all objects in the specified zone in the given axis. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        dir 
        An integer value corresponding to the Nudge Direction table below. 
        
        Relevant Data Table(s)
        
        Nudge Directions 
        Value Description 
        1, -1 In the X axis. 
        2, -2 In the Y axis. 
        3, -3 In the Z axis. 

        """
        arg_str = StringUtil._convert_args_to_string("zone.nudge", zone, dir)
        py2ecotect.conversation.Exec(arg_str)

    def rotate(self, zone, azi, alt):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done about the Y axis first 
        (altitude) and then the Z axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        azi 
        The azimuth value in degrees. 
        
        alt 
        The altitude value in degrees. 
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.rotate", zone, azi, 
                                                     alt)
        py2ecotect.conversation.Exec(arg_str)

    def rotateaxis(self, zone, rx, ry, rz):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done by the given angles in 
        each axis. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        rx 
        The degrees of rotation in the X-Axis. 
        
        ry 
        The degrees of rotation in the Y-Axis. 
        
        rz 
        The degrees of rotation in the Z-Axis.
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.rotateaxis", zone, 
                                                     rx, ry, rz)
        py2ecotect.conversation.Exec(arg_str)

    def rotatereverse(self, zone, azi, alt):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done about the Z axis first 
        (altitude) and then the Y axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        azi 
        The azimuth value in degrees. 
        
        alt 
        The altitude value in degrees.
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.rotatereverse", zone, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def scale(self, zone, sx, sy, sz):
        """
        
        Scales all objects in the specified zone by a factor of sx, sy and sz in 
        the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        sx, sy, sz 
        A value representing the scaling factor in each of the X, Y and Z axis.
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.scale", zone, 
                                                     sx, sy, sz)
        py2ecotect.conversation.Exec(arg_str)

    def xform(self, zone, trans, x, y, z):
        """
        
        Apply a generic transform to all objects in the specified zone. 

        Parameter(s)
        This command takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        trans 
        The transformation to use, given as a token corresponding to the 
        Transformation Types table. 
        
        x 
        A value specified by the table below. 
        
        y 
        A value specified by the table below. 
        
        z 
        A value specified by the table below. 
        
        Relevant Data Table(s)
        
        Transformation Types 
        Token Description 
        axis Axial rotation, where x , y and z are axial angles in degrees. 
        reverse Reverse polar rotation, where x and y are azi and alt in degrees. 
        rotate Polar rotation, where x and y are azi and alt in degrees. 
        move Translate objects by x , y and z values in the major axis. 
        scale Scale objects by x , y and z in the major axis. 
        mirror Mirror objects around About Point and vector formed by x , y and z.  
        normal Extrude objects a distance of x along its surface normal. 
        extrude Extrude objects by x , y and z in the major axis. 
        revolve Revolve objects around axis x , y degrees and in z segments. 
        nudge Nudge objects a distance of x , y and z in the major axis. 
        
        """
        arg_str = StringUtil._convert_args_to_string("zone.xform", zone, trans, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)
        
    def add_zone(self, name):
        """
        
        Use this command to create new zones in the model. It returns the 
        zero-based index of the zone just added which you can then use to edit 
        properties. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A text string containing the name of the zone to create. If this name 
        already exists, it will be incremented by adding '(X)' to the end, where 
        X is the first unique name. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        zoneIndex 
        The zero-based index of the zone just added. A value of -1 indicates 
        that the operation failed. 
        
        """
        arg_str = StringUtil._convert_args_to_string("add.zone", name)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def get_activity(self, zone):
        """
        
        Retrieves the occupant activity rate in the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The activity rate index based on the following Zone Activity Rates table. 
        
        Relevant Data Table(s)
        
        Zone Activity Rates 
        Token Value Description 
        sedentary 0 Sitting at a desk (70W) 
        walking 1 Moving about (80W) 
        exercising 2 Significant activity (100W) 
        strenuous 3 Significant exertion (150W) 
        sleeping 5 Sleeping (40 W, 0.7 Met) 
        resting 6 Resting (45 W, 0.8 Met) 
        reading 7 Reading (55 W, 1.0 Met) 
        typing 8 Typing (65 W, 1.1 Met) 
        clerical 9 Clerical (70 W, 1.2 Met) 
        cooking 10 Cooking, lite (95 W, 1.6 Met) 
        cleaning 12 Cleaning, lite (115 W, 2.0 Met) 
        slow walking 13 Slow Walking (115 W, 2.0 Met) 
        dancing 14 Dancing, lite (140 W, 2.4 Met) 
        lite execise 16 Light Exercise (175 W, 3.0 Met) 
        fast walking 17 Fast Walking (200 W, 3.4 Met) 
        hvyexercise 19 Exercise, hvy (235 W, 4.0 Met) 
        work 20 Heavy Work (235 W, 4.0 Met) 
        sport 22 Team Sport (440 W, 7.6 Met) 
  
        """
        arg_str = StringUtil._convert_args_to_string("get.zone.activity", zone)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def set_activity(self, zone, type):
        """
        
        Sets the average occupant activity rate in the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        type 
        An integer value corresponding to the following Zone Activity Rates 
        table. 
        
        Relevant Data Table(s)
        
        Zone Activity Rates 
        Token Value Description 
        sedentary 0 Sitting at a desk (70W) 
        walking 1 Moving about (80W) 
        exercising 2 Significant activity (100W) 
        strenuous 3 Significant exertion (150W) 
        sleeping 5 Sleeping (40 W, 0.7 Met) 
        resting 6 Resting (45 W, 0.8 Met) 
        reading 7 Reading (55 W, 1.0 Met) 
        typing 8 Typing (65 W, 1.1 Met) 
        clerical 9 Clerical (70 W, 1.2 Met) 
        cooking 10 Cooking, lite (95 W, 1.6 Met) 
        cleaning 12 Cleaning, lite (115 W, 2.0 Met) 
        slow walking 13 Slow Walking (115 W, 2.0 Met) 
        dancing 14 Dancing, lite (140 W, 2.4 Met) 
        lite execise 16 Light Exercise (175 W, 3.0 Met) 
        fast walking 17 Fast Walking (200 W, 3.4 Met) 
        hvyexercise 19 Exercise, hvy (235 W, 4.0 Met) 
        work 20 Heavy Work (235 W, 4.0 Met) 
        sport 22 Team Sport (440 W, 7.6 Met) 

        """
        arg_str = StringUtil._convert_args_to_string("set.zone.activity", 
                                                     zone, type)
        py2ecotect.conversation.Exec(arg_str)

    def get_admittance(self, zone):
        """
        
        Retrieves the specified zone's current value for the total zone 
        admittance (W/m^2K). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = StringUtil._convert_args_to_string("get.zone.admittance", zone)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_admittance(self, zone, value):
        """
        
        Sets the specified zone's value for the total zone admittance (W/m^2K). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the total zone admittance (W/m^2K). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.zone.admittance", 
                                                     zone, value)
        py2ecotect.conversation.Exec(arg_str)
        
    
    airspeed = property(fget = get_airspeed, fset = set_airspeed)
    def get_airspeed(self, zone):
        """
        
        Retrieves the specified zone's current value for the designed internal 
        air-speed (m/s). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = StringUtil._convert_args_to_string("get.zone.airspeed", zone)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)









if __name__ == "__main__":
    x = Zone()
    
    #print x.add_zone("malakian")
    #print x.get_activity(34)
    #x.set_activity(34, 9)
    #print x.get_admittance(34)
    #x.set_admittance(34, 2.5)
    print x.airspeed
    
    

    print "Tests completed"