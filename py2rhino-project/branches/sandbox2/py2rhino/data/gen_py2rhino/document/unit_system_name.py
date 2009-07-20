unit_system_name = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitSystemName",
    "output_package_name": "document",
    "output_module_name": "unit_system_name",

    "doc_html": """
        Returns the name of the current unit system.
    """,

    "syntax_html": """
        Rhino.UnitSystemName ([blnCapitalize [, blnSingular [, blnAbbreviate]])
    """,

    "params_html": {
        0: {
            "name": "Capitalize",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Capitalize the first character of the units system name (e.g. return "Millimeter" instead of "millimeter"). The default is not to capitalize the first character (false).
            """
        },
        1: {
            "name": "Singular",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return the singular form of the units system name (e.g. "millimeter" instead of "millimeters"). The default is to return the singular form of the name (true).
            """
        },
        2: {
            "name": "Abbreviate",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Abbreviate the name of the units system (e.g. return "mm" instead of "millimeter"). The default is not to abbreviate the name (false).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the current units system if successful."
        },
    },

    "id_com": 492,

    "params_com": {
        0: {
            "name": "vaCapitalize",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSingular",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAbbreviate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

