from py2ecotect.model import Model
from py2ecotect.zone import Zone

startDay = 219;

stopDay = startDay + 14

delimiter = "\t";

m = Model
z1 = Zone("TEST1")

currentZone = m.get_current_zone()
#currentZonename = 
