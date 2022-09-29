from logic import *
import datetime


# hier nieuwe plaatjes, tekst etc
baseImg = PlaceImage(root,'h.png',0.52,0.52,canvas,foto_x_resize=root.winfo_screenwidth()-390,foto_y_resize=root.winfo_screenheight())
windmolen = PlaceGif(root, canvas, 'fw1.gif',0.25,0.42,speed=50)
sung = PlaceGif(root, canvas, 'sun.gif',0.38,0.138,speed=50,resize='min',amount=4)
zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnepanelen',0.57,0.264,size=17)
powerwallTekst = PlaceTxt(root,canvas,'Powerwall',0.658,0.413,size=17) 
waterStofTekst = PlaceTxt(root,canvas,'Waterstof',0.778,0.643,size=17)
warmteKoudopslag = PlaceTxt(root,canvas,'Warmte-Koudopslag',0.27,0.743,size=17)
waterboiler = PlaceTxt(root,canvas,'Waterboiler',0.52,0.17,size=17)
windmolen = PlaceTxt(root,canvas,'Windmolen',0.171,0.55,size=17)

# grafieken

graph1 = PlaceGraph(root,canvas,fig, bus, 0.85,0.12,0x1000400,2,xtitle='Uren',ytitle='Waardenq', title='Zonnepanelen') 
ani2 = animation.FuncAnimation(fig,graph1.graph,interval=1000)

graph2 = PlaceGraph(root,canvas, fig2,bus, 0.123,0.13,0x1000400,4,xtitle='Uren',ytitle='Waarden', title='Windmolen') 
ani3 = animation.FuncAnimation(fig2,graph2.graph,interval=1000)

graph3 = PlaceGraph(root,canvas, fig3,bus, 0.87,0.9,0x1000400,0,xtitle='Uren',ytitle='Waarden', title='Waterstof') 
ani4 = animation.FuncAnimation(fig3,graph3.graph,interval=1000)

graph4 = PlaceGraph(root,canvas, fig4,bus, 0.123,0.89,0x1000400,1,xtitle='Uren',ytitle='Waarden', title='Warmte-Koudopslag') 
ani5 = animation.FuncAnimation(fig4,graph4.graph,interval=1000)


bus.start()
root.mainloop()
