add_directional_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "AddDirectionalLight",
    "output_package_name": "light",
    "output_module_name": "add_directional_light",

    "doc_html": """
        Adds a new directional light object  to the document.
    """,

    "syntax_html": {
        0: ("arrStartPoint", "arrEndPoint"),
    },

    "params_html": {
        0: {
            "name": "arrStartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPoint",
            "doc": """
        The 3-D starting point of the light.
            """
        },
        1: {
            "name": "arrEndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPoint",
            "doc": """
        The 3-D ending point and direction of the light.
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

    "id_com": 153,

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
    },

    "returns_com": "tagVARIANT",

}

