mesh_boolean_union = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshBooleanUnion",
    "output_package_name": "mesh",
    "output_module_name": "mesh_boolean_union",

    "doc_html": """
        Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.MeshBooleanUnion (arrInput [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Input",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the meshes to union.
            """
        },
        1: {
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

    "id_com": 731,

    "params_com": {
        0: {
            "name": "vaMeshes",
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

