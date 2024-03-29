object_mesh_min_initial_grid_quads = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshMinInitialGridQuads",
    "output_package_name": "object",
    "output_module_name": "object_mesh_min_initial_grid_quads",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's minimum initial grid quads property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "intQuads"),
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
            "name": "intQuads",
            "py_name": "quads",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Quads",
            "doc": """
        The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If intQuads is not specified, the current render mesh minimum initial grid quads if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If intQuads is specified, the previous render mesh minimum initial grid quads if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 864,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaQuads",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

