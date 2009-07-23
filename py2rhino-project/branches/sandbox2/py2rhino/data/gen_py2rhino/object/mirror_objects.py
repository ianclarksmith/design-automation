mirror_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "MirrorObjects",
    "output_package_name": "object",
    "output_module_name": "mirror_objects",

    "doc_html": """
        Mirrors one or more objects.
    """,

    "syntax_html": {
        0: ("arrObjects", "arrStartPt", "arrEndPt", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to mirror.
            """
        },
        1: {
            "name": "arrStartPt",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPt",
            "doc": """
        The start of the mirror plane.
            """
        },
        2: {
            "name": "arrEndPt",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPt",
            "doc": """
        The end of the mirror plane.
            """
        },
        3: {
            "name": "blnCopy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Copy",
            "doc": """
        Copy the objects. If omitted, the objects will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "An array of strings identifying the mirrored objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 590,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCopy",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

