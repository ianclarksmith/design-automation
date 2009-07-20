mesh_boolean_intersection = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshBooleanIntersection",
    "output_package_name": "mesh",
    "output_module_name": "mesh_boolean_intersection",

    "doc_html": """
        Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.MeshBooleanIntersection (arrInput0, arrInput1 [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Input0",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the meshes.
            """
        },
        1: {
            "name": "Input1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the meshes.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete all input objects. The default is to delete all input objects (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the newly created objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 733,

    "params_com": {
        0: {
            "name": "vaMeshes0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMeshes1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

