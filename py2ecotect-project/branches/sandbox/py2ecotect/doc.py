import py2ecotect as p2e

from _select import Select 
from _selection import Selection
from _calculation import Calculation
from _results import Results
from _rays import Rays
from _weather import Weather

from _model import Model
from _ray import Ray
from _attribute import Attribute
from _grid import Grid
from _grid3d import Grid3D
from _masks import Masks
from _shading import Shading
from _sunpath import Sunpath
from _project_data import Project_Data
from _project import Project

_zones = []
_objects = []
_nodes = []

def _populate():
    val = p2e._app.Request("get.model.zones")
    num_zones = p2e._util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
            p2e.ent.Zone(eco_id)

