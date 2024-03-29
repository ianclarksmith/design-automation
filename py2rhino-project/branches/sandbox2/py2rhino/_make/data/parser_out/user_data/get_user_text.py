get_user_text = {
    "input_folder_name": "User_Data_Methods",
    "input_file_name": "GetUserText",
    "output_package_name": "user_data",
    "output_module_name": "get_user_text",

    "doc_html": """
        Returns User Text that is stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.
    """,

    "syntax_html": {
        0: ("strObject", "strKey", "blnAttachToGeometry"),
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
        The object's identifier.
            """
        },
        1: {
            "name": "strKey",
            "py_name": "key",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Key",
            "doc": """
        The key name.  If omitted or an empty string ("") is specified, all key names for the object are returned.
            """
        },
        2: {
            "name": "blnAttachToGeometry",
            "py_name": "attach_to_geometry",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "AttachToGeometry",
            "doc": """
        The location on the object to retrieve the User Text.
		Value
		Description
		True
		Retrieve text information from the object geometry. If the information is closely associated with the geometry, attach it to the geometry. For example, a circle's radius should be attached to the geometry because the information will be invalid if the circle is control-point edited and changed into a NURBS curve.
		False (Default)
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strKey is specified, then the associated value if successful."
        },
        1: {
            "type": "array",
            "doc": "If strKey is not specified, then an array of key names if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 729,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKey",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

