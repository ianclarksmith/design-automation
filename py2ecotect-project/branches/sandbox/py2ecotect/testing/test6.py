import py2ecotect as p2e
import py2rhino as p2r


p2e.doc.weather.load_all('C:\Program Files\Autodesk\Ecotect 2009\Weather Data\Australia-SydneyNSW-1.wea')

print p2e.doc.weather.location_name()
print p2e.doc.weather.beam_solar(1, 8)
print p2e.doc.weather.temperature(1, 8)

p2e.doc.model.set_day_of_year(1, 9)
print p2e.doc.model.sun_angles()

#dec solstice
p2e.doc.model.set_date(21, 12, 9)
dec_sol_am_angles = p2e.doc.model.sun_angles()
p2e.doc.model.set_date(21, 12, 17)
dec_sol_pm_angles = p2e.doc.model.sun_angles()

#june solstice
p2e.doc.model.set_date(21, 6, 9)
jun_sol_am_angles = p2e.doc.model.sun_angles()
p2e.doc.model.set_date(21, 6, 17)
jun_sol_pm_angles = p2e.doc.model.sun_angles()

print dec_sol_am_angles, dec_sol_pm_angles
print jun_sol_am_angles, jun_sol_pm_angles

