add_planar_mesh = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "AddPlanarMesh",
    "output_package_name": "mesh",
    "output_module_name": "add_planar_mesh",

    "doc_html": """
        Creates a planar mesh from a closed, planar curve.
    """,

    "syntax_html": {
        0: ("strObject", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a closed, planar curve object.
            """
        },
        1: {
            "name": "blnDelete",
            "opt_or_req": "Required",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        If True, then the input curve will be deleted. If not specified or False (default), then the input curve will not be deleted.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "An string identifying the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 915,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

