mesh_volume = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_volume",

    "doc_html": """
        Returns the approximate volume of one or more closed mesh objects.
    """,

    "syntax_html": """
        Rhino.MeshVolume (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of object identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing three numbers if successful.  The three elements of the array are as follows:"
        },
        1: {
            "type": "number",
            "doc": "The number of meshes used in the volume calculation."
        },
        2: {
            "type": "number",
            "doc": "The total volume of all meshes."
        },
        3: {
            "type": "number",
            "doc": "The error estimate."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 354,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

