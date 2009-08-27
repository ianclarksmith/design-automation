import py2ecotect as p2e

#from py2ecotect.doc.select import Select 
#from py2ecotect.doc.selection import Selection
#from py2ecotect.doc.rays import Rays

from py2ecotect.doc import calculation
from py2ecotect.doc import results
from py2ecotect.doc import weather

from py2ecotect.doc import model
from py2ecotect.doc import attribute
from py2ecotect.doc import grid
from py2ecotect.doc import project
from py2ecotect.doc import shading

#from py2ecotect.doc.ray import Ray
#from py2ecotect.doc.grid3d import Grid3D
#from py2ecotect.doc.masks import Masks
#from py2ecotect.doc.project_data import Project_Data


_zones = []
_objects = []
_nodes = []

def _populate():
    val = p2e._app.Request("get.model.zones")
    num_zones = p2e._util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
            p2e.ent.Zone(eco_id)

