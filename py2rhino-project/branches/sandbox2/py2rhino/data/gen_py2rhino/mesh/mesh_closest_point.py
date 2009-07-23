mesh_closest_point = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshClosestPoint",
    "output_package_name": "mesh",
    "output_module_name": "mesh_closest_point",

    "doc_html": """
        Returns the point on a mesh that is closest to a test point.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a mesh object.
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point to test.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The tolerance. Of omitted, a default tolerance of 0.0 is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the results of the calculation, if successful. The array elements are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The 3-D point on the mesh object."
        },
        2: {
            "type": "number",
            "doc": "The index of the mesh face on which the 3-D point lies."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 750,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

