set_attribute_data = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "SetAttributeData",
    "output_package_name": "user_data",
    "output_module_name": "set_attribute_data",

    "doc_html": """
        Adds or sets a RhinoScript user data item to an object's attributes.
    """,

    "syntax_html": """
        Rhino.SetAttributeData (strObject, strSection, strEntry, strValue)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Section",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The application name.
            """
        },
        2: {
            "name": "Entry",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The key name.
            """
        },
        3: {
            "name": "Value",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The string value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The previous value if successful."
        },
        1: {
            "type": "null",
            "doc": "If no previous value exits, if not successful, or on error."
        },
    },

    "id_com": 683,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaApp",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKey",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

