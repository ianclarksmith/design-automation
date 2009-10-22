import py2ecotect as p2e


#SELECT
wall = p2e.model.scan.objects()[2]
p2e.model.select.none()
wall.state.select()

#SET SOME SETTINGS
p2e.model.shading_calcs.set_display_shading_rays_flag(1)
p2e.model.shading_calcs.set_shading_mask_angles(2, 2)
p2e.model.shading_calcs.set_shading_mask_accuracy(precision="high")
p2e.model.shading_calcs.set_detailed_shading_mask_flag(1)
p2e.model.shading_calcs.set_shading_both_sides_flag(0)

#RUN THE CALC
p2e.model.shading_calcs.calc_shading_percentage()
#p2e.doc.shading_calculations.calc_shading_direct(cumulative=True)
#p2e.doc.shading_calculations.calc_shading_total()
#p2e.doc.shading_calculations.calc_shading_diffuse()

#GET THE DATA
#100 = fully shaded
for time in range(8,18,1):
    
    p2e.model.time.set_date(21, 6, time)
    
    print time, p2e.model.shading_calcs.result_percentage_by_day_time(150, time)
    print time, p2e.model.shading_calcs.result_percentage_by_current_day_time()
    print "==="


p2e.app.view.redraw()
print "done"