set_user_text = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "SetUserText",
    "output_package_name": "user_data",
    "output_module_name": "set_user_text",

    "doc_html": """
        Sets or removes user text stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.
    """,

    "syntax_html": {
        0: ("strObject", "strKey", "strValue", "blnAttachToGeometry"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "strKey",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Key",
            "doc": """
        The key name to set.
            """
        },
        2: {
            "name": "strValue",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Value",
            "doc": """
        The string value to set. If omitted the key/value pair specified by strKey will be deleted.
            """
        },
        3: {
            "name": "blnAttachToGeometry",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "AttachToGeometry",
            "doc": """
        The location on the object to store the User Text.
		Value
		Description
		True
		Attaches text information to the object geometry. If the information is closely associated with the geometry, attach it to the geometry. For example, a circle's radius should be attached to the geometry because the information will be invalid if the circle is control-point edited and changed into a NURBS curve.
		False (Default)
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 728,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKey",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

