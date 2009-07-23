from py2ecotect.view import View 
import time

v = View()

v.redraw()
v.set_font(8, "Arial")
v.set_pen("0xFF8888", 2)
v.draw_moveto(1000, 1000, 0)

v.draw_lineto(8000, 1000, 500)
v.draw_lineto(5000, 4000, 1000)
v.draw_lineto(1000, 4000, 1500)
v.draw_arrowto(1000, 1000, 2000, 3.0)


v.align = 24
v.draw_text(5000, 4000, 1000, "11 <i>This is</i> <b>some <r>formatted</r></b> text")

v.align = 14
v.draw_text(1000, 4000, 1500, "11 This is some plain text")

v.align = 2

width, height = v.get_size()

v.set_pen("0x0000FF", 1)

v.set_font(10, "Verdana")

v.draw_text2d(width - 10, 1 * 20 - 10, "15 This is the fourth node.")
v.draw_move2d(width - 215, -2 + 1 * 20)
v.draw_arrowto(1000, 1000, 2000, 3.0)
time.sleep(1)

v.draw_text2d(width - 10, 2 * 20 - 10, "15 This is the third node.")
v.draw_move2d(width - 215, -2 + 2 * 20)
v.draw_arrowto(1000, 4000, 1500, 3.0)
time.sleep(1)

v.draw_text2d(width - 10, 3 * 20 - 10, "15 This is the second node.")
v.draw_move2d(width - 215, -2 + 3 * 20)
v.draw_arrowto(5000, 4000, 1000, 3.0)
time.sleep(1)

v.draw_text2d(width - 10, 4 * 20 - 10, "15 This is the first node.")
v.draw_move2d(width - 215, -2 + 4 * 20)
v.draw_arrowto(8000, 1000, 500, 3.0)
time.sleep(1)


v.set_font(8, "Arial")
