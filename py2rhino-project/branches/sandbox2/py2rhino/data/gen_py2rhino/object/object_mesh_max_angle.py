object_mesh_max_angle = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshMaxAngle",
    "output_package_name": "object",
    "output_module_name": "object_mesh_max_angle",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's maximum angle property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "dblAngle"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "dblAngle",
            "py_name": "angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The render mesh maximum angle in degrees.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If dblAngle is not specified, the current render mesh maximum angle if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If dblAngle is specified, the previous render mesh maximum angle if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 859,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAngle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

