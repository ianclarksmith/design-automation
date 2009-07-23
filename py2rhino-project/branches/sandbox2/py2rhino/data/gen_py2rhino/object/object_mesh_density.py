object_mesh_density = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshDensity",
    "output_package_name": "object",
    "output_module_name": "object_mesh_density",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's mesh density property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "dblDensity"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "dblDensity",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Density",
            "doc": """
        The render mesh density, which is a number between 0.0 and 1.0.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If dblDensity is not specified, the current render mesh density if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If dblDensity is specified, the previous render mesh density if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 858,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDensity",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

