import py2ecotect as p2e

#CREATE A MASK
p2e.doc.shading_calculations.clear_shading_masks()
print "num masks  = ", p2e.doc.shading_calculations.num_shading_masks()
mask = p2e.ent.ShadingMask.create()
mask_index = mask._eco_id
print "mask index = ", mask_index
print "num masks  = ", p2e.doc.shading_calculations.num_shading_masks()

#APPLY TO SURFACE AND SELECT
wall = p2e.doc.model.objects()[1]
wall.prop.set_mask(mask)
wall.state.select()

#SET SOME SETTINGS
p2e.doc.shading_calculations.set_display_shading_rays_flag(1)
p2e.doc.shading_calculations.set_shading_mask_angles(2, 2)
p2e.doc.shading_calculations.set_overshadowing_precision(precision="high")
print "detailed = ", p2e.doc.shading_calculations.detailed_shading_mask_flag()

#RUN THE CALC
p2e.doc.shading_calculations.calc_shading_percentage(cumulative=True)
#p2e.doc.shading_calculations.calc_shading_direct(cumulative=True)
#p2e.doc.shading_calculations.calc_shading_total()
#p2e.doc.shading_calculations.calc_shading_diffuse()
mask.prop.update()

#GET THE DATA
#100 = fully shaded
for time in range(8,18,1):
    #print mask.prop.percentage_by_day_time(20, time)
    p2e.doc.model.set_date(21, 6, time)
    print time, mask.prop.percentage_by_current_day_time()


print wall.prop.attr_1(), wall.prop.attr_2(), wall.prop.attr_3()
mask_index = wall.prop.mask()._eco_id
print "mask index = ", mask_index

p2e.app.view.redraw()
print "done"