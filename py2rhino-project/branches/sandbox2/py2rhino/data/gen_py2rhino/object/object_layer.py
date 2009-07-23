object_layer = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectLayer",
    "output_package_name": "object",
    "output_module_name": "object_layer",

    "doc_html": """
        Returns or modifies the layer of an object.
    """,

    "syntax_html": {
        0: ("strObject", "strLayer"),
        1: ("arrObjects", "strLayer"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        1: {
            "name": "strLayer",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of an existing layer.  If omitted, the current object layer is returned.  Note, if arrObjects is specified, strLayer is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a layer is not specified,  the object's current layer if successful."
        },
        1: {
            "type": "number",
            "doc": "If a layer is specified, the object's previous layer if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 51,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLayer",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

