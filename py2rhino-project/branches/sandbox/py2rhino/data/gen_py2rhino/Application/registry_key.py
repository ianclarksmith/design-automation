registry_key = {

    "class": "Application",
    "method": "registry_key",
    "doc": """
        Returns Rhino's Windows Registry key.
    """,

    "syntax": """
        Rhino.RegistryKey ()
    """,

    "params": {
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "Rhino's Windows Registry key if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

