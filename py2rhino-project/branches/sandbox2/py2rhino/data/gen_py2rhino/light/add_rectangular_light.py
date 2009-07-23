add_rectangular_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "AddRectangularLight",
    "output_package_name": "light",
    "output_module_name": "add_rectangular_light",

    "doc_html": """
        Adds a new rectangular light object  to the document.
    """,

    "syntax_html": {
        0: ("arrOrigin", "arrWidth", "arrHeight"),
    },

    "params_html": {
        0: {
            "name": "arrOrigin",
            "py_name": "origin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        The 3-D origin point of the light.
            """
        },
        1: {
            "name": "arrWidth",
            "py_name": "width",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Width",
            "doc": """
        The 3-D width and direction point of the light.
            """
        },
        2: {
            "name": "arrHeight",
            "py_name": "height",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Height",
            "doc": """
        The 3-D height and direction point of the light.
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

    "id_com": 156,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

