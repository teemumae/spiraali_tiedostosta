from turtle import *
def draw_spiral(line_color, arcs, r, r_growth, pen):
 
    up()
    color(line_color)
    pensize(pen)
    down()
    for i in range(arcs):
        circle(r,90)
        r+=r_growth
    up()
def piirra_tiedostosta(tiedosto):
    spiraali = []
    with open(tiedosto) as spiraalit:
        for rivi in spiraalit:
            spiraali.append(rivi.split(','))
    for i in range(len(spiraali)):
        for j in range(len(spiraali[i])):
            if j == 0:
                vari = spiraali[i][j]
                vari = vari.strip()
            if j == 1:
                kaaret = int(spiraali[i][j])
                kaaret = kaaret.strip()
            if j == 2:
                r = float(spiraali[i][j])
                r = r.strip()
            if j == 3:
                r_kasvu = float(spiraali[i][j])
                pisteet_2 = pisteet_2.strip()
            if j == 4:
                viiva = int(spiraali[i][j])
                viiva = viiva.strip
            draw_spiral(vari, kaaret, r, r_kasvu, viiva)
piirra_tiedostosta('spiraali.txt')
