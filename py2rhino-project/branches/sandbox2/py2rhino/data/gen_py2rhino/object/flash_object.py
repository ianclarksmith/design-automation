flash_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "flash_object",

    "doc_html": """
        Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.
    """,

    "syntax_html": """
        Rhino.FlashObject (strObject [, blnStyle])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to flash.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the objects to flash.
            """
        },
        2: {
            "name": "Style",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The flash style.  If True (default), then the objects will flash between their object color and Rhino's selected object color.  If false, then the objects will flash between invisible and visible.
            """
        },
    },

    "returns_html": {
    },

    "id_com": 869,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

