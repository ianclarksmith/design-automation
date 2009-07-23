split_brep = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SplitBrep",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "split_brep",

    "doc_html": """
        Splits a brep.  A brep can be either a surface with a single face or a polysurface.
    """,

    "syntax_html": {
        0: ("strBrep", "strCutter", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "strBrep",
            "py_name": "brep",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Brep",
            "doc": """
        The identifier of the brep object to split.
            """
        },
        1: {
            "name": "strCutter",
            "py_name": "cutter",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Cutter",
            "doc": """
        The identifier of the brep object to split with.
            """
        },
        2: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input brep.  If omitted, the input brep will not be deleted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new brep objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 637,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCutter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

