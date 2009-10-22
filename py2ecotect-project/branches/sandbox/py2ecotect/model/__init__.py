import py2ecotect as p2e

#from py2ecotect.doc.rays import Rays
#from py2ecotect.doc.ray import Ray

#from py2ecotect.model import calculation
#from py2ecotect.model import results

from py2ecotect.model import settings
from py2ecotect.model import shading_calcs

from py2ecotect.model import sun
from py2ecotect.model import time
from py2ecotect.model import scan
from py2ecotect.model import select
from py2ecotect.model import selection
from py2ecotect.model import weather

from py2ecotect.model import attribute
from py2ecotect.model import grid
from py2ecotect.model import grid3d
from py2ecotect.model import project
from py2ecotect.model import project_data


from py2ecotect._base import _util

_zones = []
_objects = []
_nodes = []
_masks = []

def _populate():
    
    val = p2e._app.Request("get.model.zones")
    num_zones = _util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
        p2e.obj.Zone(eco_id)

    val = p2e._app.Request("get.masks.count")
    num_masks = p2e._base._util._convert_str_to_type(val, int)
    for eco_id in range(num_masks):
        p2e.obj.ShadingMask(eco_id)    