objects_by_type = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "ObjectsByType",
    "output_package_name": "selection",
    "output_module_name": "objects_by_type",

    "doc_html": """
        Returns the identifiers of all objects based on the objects' geometry type.
    """,

    "syntax_html": """
        Rhino.ObjectsByType (intType [, blnSelect])
    """,

    "params_html": {
        0: {
            "name": "Type",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The type(s) of geometry objects (points, curves, surfaces, meshes, etc.) that can be selected.  Object types can be added together to filter several different kinds of geometry.
		Value
		Description
		0
		All objects
		1
		Point
		2
		Point cloud
		4
		Curve
		8
		Surface or single-face brep
		16
		Polysurface or multiple-face
		32
		Mesh
		256
		Light
		512
		Annotation
		4096
		Instance or block reference
		8192
		Text dot object
		16384
		Grip object
		32768
		Detail
		65536
		Hatch
		131072
		Morph control
		134217728
		Cage
		268435456
		Phantom
		536870912
            """
        },
        1: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the objects.  If omitted, the objects are not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 41,

    "params_com": {
        0: {
            "name": "vaType",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

