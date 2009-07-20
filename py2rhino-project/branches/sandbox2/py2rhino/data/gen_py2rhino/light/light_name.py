light_name = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "light_name",

    "doc_html": """
        Returns or modifies the user-definable name of a light object.
    """,

    "syntax_html": """
        Rhino.LightName (strObject [, strName])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the light object.
            """
        },
        1: {
            "name": "Name",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new light name.  If omitted, the current light name is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strName is not specified,  the current light name if successful."
        },
        1: {
            "type": "string",
            "doc": "If strName is specified,  the previous light name if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 169,

    "params_com": {
        0: {
            "name": "vaLight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

