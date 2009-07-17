plug_ins = {

    "class": "Application",
    "method": "plug_ins",
    "doc": """
        Returns an array of registered Rhino plug-ins.
    """,

    "syntax": """
        Rhino.PlugIns ([intTypes [, intStatus]])
    """,

    "params": {
        0: {
            "name": "types",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
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
            "name": "status",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
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

    "returns": {
        0: {
            "type_vb": "Array",
            "doc": "An array of strings describing the plug-ins if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

