mirror_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "MirrorObjects",
    "output_package_name": "object",
    "output_module_name": "mirror_objects",

    "doc_html": """
        Mirrors one or more objects.
    """,

    "syntax_html": """
        Rhino.MirrorObjects (arrObjects, arrStartPt, arrEndPt [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to mirror.
            """
        },
        1: {
            "name": "StartPt",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The start of the mirror plane.
            """
        },
        2: {
            "name": "EndPt",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The end of the mirror plane.
            """
        },
        3: {
            "name": "Copy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

