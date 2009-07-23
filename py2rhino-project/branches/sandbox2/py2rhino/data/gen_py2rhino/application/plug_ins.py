plug_ins = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "PlugIns",
    "output_package_name": "application",
    "output_module_name": "plug_ins",

    "doc_html": """
        Returns an array of registered Rhino plug-ins.
    """,

    "syntax_html": {
        0: ("intTypes", "intStatus"),
    },

    "params_html": {
        0: {
            "name": "intTypes",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Types",
            "doc": """
        The type or types of plug-ins to return.  Plug-in types can be added together to filter several different kinds of plug-ins.  If omitted, all plug-in types are returned.
		Value
		Description
		0
		All plug-ins
		1
		Render plug-ins
		2
		File export plug-ins
		4
		File import plug-ins
		8
		Digitizer plug-ins
		16
            """
        },
        1: {
            "name": "intStatus",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Status",
            "doc": """
        The status, either loaded or unloaded, of the plug-ins to return.  If omitted, both loaded and unloaded plug-ins are returned.
		Value
		Description
		0
		Both loaded or unloaded plug-ins..
		1
		Loaded plug-ins.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings describing the plug-ins if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 315,

    "params_com": {
        0: {
            "name": "vaTypes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLoaded",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

