# Adaptor for fitting an ikea melodi lampshade to a standard uk bayonet fitting
# Use at own risk


inner_rad = 30/2
outer_rad = 97.5/2

vent_rad = 10
vent_number = 7

#Do not edit below this line


origin=V(0,0)
distance = (outer_rad - inner_rad)/2 + inner_rad
vent_pos = origin + V(0, distance)

plane = camcam.add_plane(Plane('xy', cutter='laser'))

plane.add_layer('adaptor_plate', 'perspex', 3)

border=Circle(origin, outer_rad)

adaptor=plane.add(Part(name='adaptor', layer='adaptor_plate', ignore_border=False, border=border))
adaptor.add(Hole(origin, rad=inner_rad))


for i in range(0,vent_number):
    vent_hole = adaptor.add(Hole(vent_pos, rad=vent_rad))
    vent_hole.rotate(origin, (i*360/vent_number))
