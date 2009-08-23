import py2ecotect as p2e

#from wrappers.doc_functions.select import Select 
#from wrappers.doc_functions.selection import Selection
#from wrappers.doc_functions.rays import Rays

from wrappers.doc_functions import calculation
from wrappers.doc_functions import results
from wrappers.doc_functions import weather

from wrappers.doc_functions import model
from wrappers.doc_functions import attribute
from wrappers.doc_functions import grid
from wrappers.doc_functions import project
from wrappers.doc_functions import shading

#from wrappers.doc_functions.ray import Ray
#from wrappers.doc_functions.grid3d import Grid3D
#from wrappers.doc_functions.masks import Masks
#from wrappers.doc_functions.project_data import Project_Data


_zones = []
_objects = []
_nodes = []

def _populate():
    val = p2e._app.Request("get.model.zones")
    num_zones = p2e._util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
            p2e.ent.Zone(eco_id)

