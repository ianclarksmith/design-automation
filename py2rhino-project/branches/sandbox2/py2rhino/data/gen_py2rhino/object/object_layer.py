object_layer = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectLayer",
    "output_package_name": "object",
    "output_module_name": "object_layer",

    "doc_html": """
        Returns or modifies the layer of an object.
    """,

    "syntax_html": """
        Rhino.ObjectLayer (strObject [, strLayer])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        2: {
            "name": "Layer",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

