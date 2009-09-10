import py2ecotect as p2e


#from py2ecotect.doc.rays import Rays

from py2ecotect.doc import select
from py2ecotect.doc import selection
from py2ecotect.doc import calculation
from py2ecotect.doc import results
from py2ecotect.doc import weather

from py2ecotect.doc import model
from py2ecotect.doc import attribute
from py2ecotect.doc import grid
from py2ecotect.doc import grid3d
from py2ecotect.doc import project
from py2ecotect.doc import project_data

#from py2ecotect.doc.ray import Ray
#from py2ecotect.doc.masks import Masks


from py2ecotect._base import _util

_zones = []
_objects = []
_nodes = []

def _populate():
    val = p2e._app.Request("get.model.zones")
    num_zones = _util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
        p2e.ent.Zone(eco_id)

