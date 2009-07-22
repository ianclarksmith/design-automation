add_linear_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "AddLinearLight",
    "output_package_name": "light",
    "output_module_name": "add_linear_light",

    "doc_html": """
        Adds a new linear light object  to the document.
    """,

    "syntax_html": """
        Rhino.AddLinearLight (arrStartPoint, arrEndPoint [, dblWidth])
    """,

    "params_html": {
        0: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D starting point of the light.
            """
        },
        1: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D ending point and direction of the light.
            """
        },
        2: {
            "name": "Width",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The width of the light.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 154,

    "params_com": {
        0: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaWidth",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

