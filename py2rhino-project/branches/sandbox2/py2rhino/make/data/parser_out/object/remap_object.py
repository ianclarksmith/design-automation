remap_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "RemapObject",
    "output_package_name": "object",
    "output_module_name": "remap_object",

    "doc_html": """
        Remqps a single object from one plane, or coordinate system, to another.
    """,

    "syntax_html": {
        0: ("strObject", "arrSrcPlane", "arrDstPlane", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object to remap.
            """
        },
        1: {
            "name": "arrSrcPlane",
            "py_name": "src_plane",
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
            "py_name": "dst_plane",
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
            "py_name": "copy",
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
            "type": "string",
            "doc": "The identifier of the remapped object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 655,

    "params_com": {
        0: {
            "name": "vaObject",
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

