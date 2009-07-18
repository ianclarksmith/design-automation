            
def w(f, text, tabs = 0, nls=0, nle=1):
    if isinstance(text, tuple):
        text = list(text)
    if not isinstance(text, list):
        text = [text]
    if tabs != 0:
        tab_str = ["    " * tabs]
        text = tab_str + text
    if nls != 0:
        nls_str = ["\n" * nls]
        text =  nls_str + text          
    if nle != 0:
        nle_str = ["\n" * nle]
        text = text + nle_str
    f.writelines(text)


def camel_to_underscore(name_cc):
    name_us = ""
    #get list of letters
    for i in range(len(name_cc)):
        if (name_cc[i].isupper()):
            name_us += "_"
            name_us += name_cc[i].lower()
        else:
            name_us += name_cc[i]
    #check we are not starting with an underscore
    if name_us.startswith("_"):
        name_us = name_us[1:]
    return name_us