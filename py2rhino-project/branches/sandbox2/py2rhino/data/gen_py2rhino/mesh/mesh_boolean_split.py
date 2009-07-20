mesh_boolean_split = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_boolean_split",

    "doc_html": """
        Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.MeshBooleanSplit (arrInput0, arrInput1, [, blnDelete])
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

    "id_com": 734,

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

