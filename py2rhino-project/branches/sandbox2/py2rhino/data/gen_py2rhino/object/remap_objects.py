remap_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "RemapObjects",
    "output_package_name": "object",
    "output_module_name": "remap_objects",

    "doc_html": """
        Remqps one or more objects from one plane, or coordinate system, to another.
    """,

    "syntax_html": {
        0: ("arrObjects", "arrSrcPlane", "arrDstPlane", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "arrObject",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Object",
            "doc": """
        The identifiers of the objects to remap.
            """
        },
        1: {
            "name": "arrSrcPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "SrcPlane",
            "doc": """
        The source plane to transform from.
            """
        },
        2: {
            "name": "arrDstPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "DstPlane",
            "doc": """
        The destination plane to transform to.
            """
        },
        3: {
            "name": "blnCopy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Copy",
            "doc": """
        Copy the object. If omitted, the object will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the remapped objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 656,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSrcPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDstPlane",
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

