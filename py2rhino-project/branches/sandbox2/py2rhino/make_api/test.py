from py2rhino.data.gen_comtypes import rhinoscript as ct_rs

for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
    print i
    for j in i:
        print "\t", j
