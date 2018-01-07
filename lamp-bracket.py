# Adaptor for fitting an ikea lamp to a wall
# Use at own risk

#TODO CHECK DIMENSIONS FOR LAMP

cutterrad=3.175/2

inner_rad = 30/2
outer_rad = 70/2

inset_depth = 2

mount_number = 3
mount_cs_rad = 6.5/2
mount_cs_depth = 3

bolt_rad=6.5/2

rota_lock_rad = cutterrad+0.1
rota_lock_depth = 3 + inset_depth
rota_lock_distance = 15/2
#Do not edit below this line

origin=V(0,0)
distance = 2*((outer_rad - inner_rad)/3) + inner_rad
mount_pos = origin + V(0, distance)
mount_rad = 4.5/2

plane = camcam.add_plane(Plane('xy', cutter='1/8_endmill'))

plane.add_layer('bracket', 'pvc', 6)

border=Circle(origin, outer_rad)

adaptor=plane.add(Part(name='adaptor', layer='bracket', ignore_border=False, border=border))

adaptor.add(Hole(origin, rad=bolt_rad))
adaptor.add(Hole(origin + V(0, rota_lock_distance), rad=rota_lock_rad, z1=-rota_lock_depth))


clearing = int(math.floor(inner_rad/cutterrad*2))+1

for i in range(0,clearing):
    adaptor.add(Hole(origin, rad=inner_rad-i*cutterrad, z1=-inset_depth))

for i in range(0,mount_number):
    mount_hole = adaptor.add(Hole(mount_pos, rad=mount_rad))
    mount_cs = adaptor.add(Hole(mount_pos, rad=mount_cs_rad, z1=-mount_cs_depth))
    mount_hole.rotate(origin, (i*360/mount_number))
    mount_cs.rotate(origin, (i*360/mount_number))
