#The data below will be used to generate the Rhinoscript function wrappers
#===============================================================================
# Mesh
#===============================================================================
class Mesh(object):
    inherits = ("_MeshRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #mesh holds
        "modf": "_MeshRootMdfy",
        "func": "_MeshRootFuncOorc",
        "test": "_MeshRootTest",#inherits from object level
        "dupl": "_MeshDupl",
        "prop": "_MeshRootPropOorc",

    }
    class Constructors(object):    
        add_mesh = {
            "method_name": "create",
            "method_parameters": (("vertices","array_of dbl","REQ"),("face_vertices","array_of int","REQ"),("vertex_normals","array_of dbl","OPT"),("texture_coordinates","array_of dbl","OPT"),("vertex_colors","array_of int","OPT"),),
            "method_returns": ("SELF","null")
            }
       
#===============================================================================
# _MeshDupl
#===============================================================================
class _MeshDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._MeshRoot.Mesh","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation","array_of dbl","OPT"),),
            "method_returns": ("_ObjectRoot._MeshRoot.Mesh","null")         
            }
        mesh_offset = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._MeshRoot.Mesh","null")
            } 
             
#===============================================================================
# PlanarMesh
#===============================================================================
class PlanarMesh(object):
    inherits = ("_MeshRoot", )
    holds = {
                   
        #general object holds
        "defm": "_ObjectRootDefm",                
        "grps": "_ObjectRootGrps",
        "mtrl": "_ObjectRootMtrl",
        "rndr": "_ObjectRootRndr",
        "stat": "_ObjectRootStat",
        "trfm": "_ObjectRootTrfm",
        "util": "_ObjectRootUtil",        
  
        #mesh holds
        "modf": "_MeshRootMdfy",
        "func": "_MeshRootFuncOpen",
        "test": "_MeshRootTest",#inherits from object level
        "dupl": "_PlanarMeshDupl",#inherits from object level
        "prop": "_MeshRootPropOpen",

    }
    class Constructors(object):  
        add_planar_mesh = {#ed
            "method_name": "create_by_crv",
            "method_parameters": (("curve","_ObjectRoot._CurveRoot","REQ"),("delete","bln","OPT"),),#closed planar curve
            "method_returns": ("SELF","null")
            }
#===============================================================================
# _PlanarMeshDupl
#===============================================================================
class _PlanarMeshDupl(object):
    inherits = None
    class Methods(object):
        copy_object = {
            "method_name": "copy_move",
            "method_parameters": (("","SELF","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
            "method_returns": ("_ObjectRoot._MeshRoot.PlanarMesh","null")        
            }
        copy_object_2 = {
            "method_name": "copy_move_by_vec",
            "method_parameters": (("","SELF","REQ"),("translation","array_of dbl","OPT"),),
            "method_returns": ("_ObjectRoot._MeshRoot.PlanarMesh","null")         
            }
        mesh_offset = {#ed
            "method_name": "copy_by_offset",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),("distance","dbl","REQ"),),
            "method_returns": ("_ObjectRoot._MeshRoot.PlanarMesh","null")
            } 
#===============================================================================
# NurbsCurve
#===============================================================================
class NurbsCurve(object):
    inherits = ("_CurveRoot", )
    class Constructors(object):
        duplicate_mesh_border = {#ed
            "method_name": "create_by_mesh_border",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),),
            "method_returns": ("SELF","null")
            }
        pull_curve_to_mesh = {#ed
            "method_name": "create_by_mesh_pull",
            "method_parameters": (("mesh","_ObjectRoot._MeshRoot","REQ"),("curve","_ObjectRoot._CurveRoot","REQ"),),
            "method_returns": ("SELF","null")
            }
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


        
#===============================================================================
# _MeshRootType
#===============================================================================
class _MeshRootType(object):#TODO: move to object
    inherits = ("_ObjectRootTest", )
    class Methods(object):
        is_mesh = {#ed
            "method_name": "is_mesh",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
#===============================================================================
# _MeshRootTest
#===============================================================================    
class _MeshRootTest(object):
    inherits = ("_ObjectRootTest",)
    class Methods(object):
        is_mesh_closed = {#ed
            "method_name": "is_closed",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        is_mesh_manifold = {#ed
            "method_name": "is_manifold",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        mesh_has_face_normals = {#ed
            "method_name": "has_face_normals",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        mesh_has_texture_coordinates = {#ed
            "method_name": "has_texture_coordinates",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        mesh_has_vertex_colors = {#ed
            "method_name": "has_vertex_colors",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
        mesh_has_vertex_normals = {#ed
            "method_name": "has_vertex_normals",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
#===============================================================================
# _MeshRootMdfy
#===============================================================================
class _MeshRootMdfy(object):
    inherits = ("_ObjectRootMdfy",)
    class Methods(object):
        mesh_quads_to_triangles = {#ed
            "method_name": "quads_to_triangles",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("bln","null")
            }
#===============================================================================
# _MeshRootProp
#===============================================================================
class _MeshRootProp(object):
    inherits = ('_MeshRootFunc',)
    class Methods(object):    

        disjoint_mesh_count = {#ed
            "method_name": "disjoint_mesh_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }        
        mesh_area = {#ed
            "method_name": "area",
            "method_parameters": (("","SELF","REQ"),), #this was an array - hope it still works
            "method_returns": ("array_of number","null")
            }
        mesh_area_centroid = {#ed
            "method_name": "area_centroid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }        
        mesh_quad_count = {#ed
            "method_name": "quad_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }        
        mesh_face_centers = {#ed
            "method_name": "face_centers",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_face_count = {#ed
            "method_name": "face_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }
        mesh_face_normals = {#ed
            "method_name": "face_normals",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_face_vertices = {
            "method_name": "face_vertices",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_faces = {#ed
            "method_name": "faces",
            "method_parameters": (("","SELF","REQ"),("face_type","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_texture_coordinates = {#ed
            "method_name": "texture_coordinates",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_triangle_count = {#ed
            "method_name": "triangle_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }
        mesh_vertex_colors = {#ed
            "method_name": "vertex_colors",
            "method_parameters": (("","SELF","REQ"),("vertex_colors","array_of int","OPT"),),
            "method_returns": ("array_of int","null")
            }
        mesh_vertex_count = {#ed
            "method_name": "vertex_count",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }
        mesh_vertex_normals = {#ed
            "method_name": "vertex_normals",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_vertices = {#ed
            "method_name": "vertices",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }        
#===============================================================================
# _MeshRootProp
#===============================================================================
class _MeshRootPropClsd(object):
    inherits = ("_MeshRootProp",)
    class Methods(object):
        mesh_volume = {#ed
            "method_name": "mesh_volume",
            "method_parameters": (("objects","array_of str","REQ"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_volume_centroid = {#ed
            "method_name": "mesh_volume_centroid",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of dbl","null")
            }          
#===============================================================================
# _MeshRootPropOpen
#===============================================================================
class _MeshRootPropOpen(object):
    inherits = ("_MeshRootProp",)
    #empty
#===============================================================================
# _MeshRootPropOorc
#===============================================================================
class _MeshRootPropOorc(object):
    inherits = ("_MeshRootPropClsd", '_MeshRootPropOpen',)
    #empty
#===============================================================================
# _MeshRootFunc
#===============================================================================
class _MeshRootFunc(object):
    inherits = ("_ObjectRootFunc",)
    class Methods(object):
        split_disjoint_mesh = {#ed
            "method_name": "split_disjoint_mesh",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._MeshRoot.Mesh","null")
            }
        unify_mesh_normals = {#TODO: maybe move to mdfy
            "method_name": "unify_normals",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("number","null")
            }
        curve_mesh_intersection = {#ed
            "method_name": "curve_intersection",
            "method_parameters": (("","SELF","REQ"),("mesh","str","REQ"),("return_faces","bln","OPT"),),
            "method_returns": ("array_of number","null")
            }
        mesh_mesh_intersection = {#ed
            "method_name": "mesh_intersection",
            "method_parameters": (("","SELF","REQ"),("mesh_1","str","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of dbl","null")
            }        
        mesh_closest_point = {#ed
            "method_name": "closest_point",
            "method_parameters": (("","SELF","REQ"),("point","array_of dbl","REQ"),("tolerance","dbl","OPT"),),
            "method_returns": ("array_of number","null")
            }
        mesh_contour_points = {#ed
            "method_name": "contour_points",
            "method_parameters": (("","SELF","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),("remove_coincident_points","bln","OPT"),),
            "method_returns": ("array_of dbl","null")
            }
        mesh_naked_edge_points = {#ed
            "method_name": "naked_edge_points",
            "method_parameters": (("","SELF","REQ"),),
            "method_returns": ("array_of bln","null")
            }
        explode_meshes = {#ed
            "method_name": "explode",
            "method_parameters": (("","SELF","REQ"),("delete","bln","OPT"),), #this was an array - hope it still works
            "method_returns": ("array_of _ObjectRoot._MeshRoot","null")
            }
#===============================================================================
# _MeshRootFuncOpen
#===============================================================================
class _MeshRootFuncOpen(object):
    inherits = ('_MeshRootFunc',)
    #empty        
#===============================================================================
# _MeshRootFuncClsd
#===============================================================================
class _MeshRootFuncClsd(object):
    inherits = ('_MeshRootFunc',)
    class Methods(object):
        mesh_boolean_difference = {
            "method_name": "boolean_difference",
            "method_parameters": (("","SELF","REQ"),("meshes","array_of str","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._MeshRoot.Mesh","null")
            }
        mesh_boolean_intersection = {
            "method_name": "boolean_intersection",
            "method_parameters": (("","SELF","REQ"),("meshes","array_of str","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._MeshRoot.Mesh","null")
            }
        mesh_boolean_union = {#TODO: this has no SELF
            "method_name": "boolean_union",
            "method_parameters": (("meshes","array_of _ObjectRoot","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._MeshRoot.Mesh","null")
            }
        mesh_boolean_split = {#ed
            "method_name": "boolean_split",
            "method_parameters": (("","SELF","REQ"),("input_1","array_of str","REQ"),("delete","bln","OPT"),),
            "method_returns": ("array_of _ObjectRoot._MeshRoot.Mesh","null")
            }
#===============================================================================
# _MeshRootFuncOorc
#===============================================================================
class _MeshRootFuncOorc(object):
    inherits = ('_MeshRootFuncOpen','_MeshRootFuncClsd',)
    #empty    
     
#===============================================================================
# _MeshRoot
#===============================================================================
class _MeshRoot(object):
    inherits = ('_ObjectRoot',)

#===============================================================================
# 
#===============================================================================


