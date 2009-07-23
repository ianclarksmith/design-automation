mesh_area = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshArea",
    "output_package_name": "mesh",
    "output_module_name": "mesh_area",

    "doc_html": """
        Returns the approximate area of one or more mesh objects.
    """,

    "syntax_html": {
        0: ("strObject"),
        1: ("arrObjects"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Objects",
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
            "doc": "The number of meshes used in the area calculation."
        },
        2: {
            "type": "number",
            "doc": "The total area of all meshes."
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

    "id_com": 353,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

