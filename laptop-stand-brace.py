# Replacement brace for lasercut laptop stand
# Use at own risk

thickness = 3

length = 316/2
height = 36.5/2

slot_width = thickness
slot_height = 17

slot_spacing = 290/2

top_radius = 5
bottom_radius = 1


origin=V(0,0)

plane = camcam.add_plane(Plane('xy', cutter='laser'))

plane.add_layer('brace', 'perspex', thickness)

border=Path(closed=True, side='out')

border.add_point(PIncurve(V(length,height)*V(-1,1), radius=top_radius, direction='cw'))

border.add_point(PIncurve(V(slot_spacing+slot_width,height)*V(-1,1), radius=0.5, direction='cw'))
border.add_point(PIncurve(V(slot_spacing+slot_width,height-slot_height)*V(-1,1), radius=0, direction='cw'))
border.add_point(PIncurve(V(slot_spacing,height-slot_height)*V(-1,1), radius=0, direction='cw'))
border.add_point(PIncurve(V(slot_spacing,height)*V(-1,1), radius=0.5, direction='cw'))

border.add_point(PIncurve(V(slot_spacing,height)*V(1,1), radius=0.5, direction='cw'))
border.add_point(PIncurve(V(slot_spacing,height-slot_height)*V(1,1), radius=0, direction='cw'))
border.add_point(PIncurve(V(slot_spacing+slot_width,height-slot_height)*V(1,1), radius=0, direction='cw'))
border.add_point(PIncurve(V(slot_spacing+slot_width,height)*V(1,1), radius=0.5, direction='cw'))


border.add_point(PIncurve(V(length,height)*V(1,1), radius=top_radius, direction='cw'))
border.add_point(PIncurve(V(length,height)*V(1,-1), radius=bottom_radius, direction='cw'))
border.add_point(PIncurve(V(length,height)*V(-1,-1), radius=bottom_radius, direction='cw'))

brace=plane.add(Part(name='brace_piece', layer='brace', ignore_border=False, border=border))

brace.add(Hole(V(slot_spacing+slot_width,height-slot_height)*V(-1,1),  rad=.5))
brace.add(Hole(V(slot_spacing,height-slot_height)*V(-1,1),  rad=.5))
brace.add(Hole(V(slot_spacing+slot_width,height-slot_height)*V(1,1),  rad=.5))
brace.add(Hole(V(slot_spacing,height-slot_height)*V(1,1),  rad=.5))
