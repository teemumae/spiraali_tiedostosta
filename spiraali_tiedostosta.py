from turtle import *
def draw_spiral(line_color, arcs, r, r_growth, pen=1):
    if pen==False:
        pen=1
    up()
    color(line_color)
    pensize(pen)
    down()
    for i in range(arcs):
        circle(r,90)
        r+=r_growth
    up()
def piirra_tiedostosta(tiedosto):

    draw_spiral(vari, kaaret, r, r_kasvu, viiva)
piirra_tiedostosta('spiraali.txt')
