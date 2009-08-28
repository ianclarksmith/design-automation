flash_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "FlashObject",
    "output_package_name": "object",
    "output_module_name": "flash_object",

    "doc_html": """
        Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.
    """,

    "syntax_html": {
        0: ("strObject", "blnStyle"),
        1: ("arrObjects", "blnStyle"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        The identifiers of the objects to flash.
            """
        },
        1: {
            "name": "blnStyle",
            "py_name": "style",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Style",
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

