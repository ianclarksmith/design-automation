sdk_version = {

    "class": "Application",
    "method": "sdk_version",
    "doc": """
        Returns the version of the Rhino SDK supported by the running version of Rhino.  Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.
    """,

    "syntax": """
        Rhino.SdkVersion ()
    """,

    "params": {
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "The supported Rhino SDK version number if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

