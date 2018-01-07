
# Tab length compensation a negative number will increase the gap between the tabs
# a fudge factor that increases the gap along the finger joint when
# negative - it should be 1/4 of the gap you want

fudge = 0.1

thickness = 3
number_of_disks = 6

#
box_height = 40 * number_of_disks
box_width = 220
box_depth = 95


cutter = 'laser'

tab_length = 10
centre = V(0, 0)

module = camcam.add_plane(Plane('plane', cutter=cutter))

module.add_layer('end', material='perspex',
                           thickness=thickness, z0=0, zoffset=-thickness - box_depth)

module.add_layer('partition', material='perspex',
                          thickness=thickness, z0=0, zoffset=-thickness - box_depth)
module.add_layer('bottom', material='perspex',
                           thickness=thickness, z0=0, zoffset=-thickness - box_depth)
module.add_layer('side', material='perspex',
                           thickness=thickness, z0=0, zoffset=-thickness - box_depth)

back_border = FingerJointBoxSide(centre, box_width, box_height, 'in', corners={'left': 'off', 'top': 'off', 'right': 'off', 'bottom': 'off'}, sidemodes={
}, tab_length=tab_length, thickness=thickness, cutterrad=0, cutter=cutter, centred=True, fudge=fudge, auto=True)


end_border = FingerJointBoxSide(centre, box_width, box_depth, 'in', corners={'left': 'off', 'top': 'on', 'right': 'off', 'bottom': 'on'}, sidemodes={'top': 'straight'}, tab_length=tab_length, thickness={
    'left': thickness, 'right': thickness, 'bottom': thickness, 'top': thickness}, cutterrad=0, cutter=cutter, centred=True, fudge=fudge, auto=True)

side_border = FingerJointBoxSide(centre, box_depth, box_height, 'in', corners={'left': 'on', 'top': 'on', 'right': 'on', 'bottom': 'on'}, sidemodes={'right': 'straight'}, tab_length=tab_length, thickness={
'left': thickness, 'right': thickness, 'bottom': thickness, 'top': thickness}, cutterrad=0, cutter=cutter, centred=True, fudge=fudge, auto=True)



bottom = module.add_path(Part(name='bottom', border=back_border, layer='bottom'))
end = module.add_path(Part(name='end', border=end_border,  layer='end'))
side = module.add_path(Part(name='side', border=side_border, layer='side'))




partition_border = FingerJointBoxSide(centre, box_width, box_depth, 'in', corners={'left': 'on', 'top': 'on', 'right': 'on', 'bottom': 'on'}, sidemodes={'top': 'straight'}, tab_length=tab_length*2, thickness={
    'left': thickness, 'right': thickness, 'bottom': thickness, 'top': thickness}, cutterrad=0, cutter=cutter, centred=True, fudge=fudge, auto=True)

disk_mount_width = 30
disk_mount_height = 30

partition = module.add_path(Part(name='partition', border=partition_border,  layer='partition'))

y = 0 + 10 + disk_mount_width/2
x = 0 + box_depth/2 -disk_mount_height/2 + thickness/2

partition.add(Rect(V(y,x), width=disk_mount_width, height=disk_mount_height, centred='true'))
partition.add(Rect(V(-y,x), width=disk_mount_width, height=disk_mount_height, centred='true'))


partion_ends = box_width/2

module.add_path(FingerJointMid(
	start = V(-partion_ends,0),
	end = V(partion_ends, 0),
	side = 'left',
	linemode = 'internal',
	startmode = 'off',
	endmode = 'off',
	tab_length = tab_length*2,
	thickness = thickness,
	cutterrad = 0,#3.17/2,#cutterrad,
	prevmode = 'off',
	nextmode = 'off', fudge = -fudge*2),['bottom']
)

partion_side = box_depth/2#+ thickness
# partion_side_end = (box_depth + thickness)/2 - thickness

# module.add_path(FingerJointMid(
# 	start = V(partion_side ,0),
# 	end = V(-partion_side, 0),
# 	side = 'left',
# 	linemode = 'internal',
# 	startmode = 'off',
# 	endmode = 'off',
# 	tab_length = tab_length*2.3,
# 	thickness = thickness,
# 	cutterrad = 0,
# 	prevmode = 'off',
# 	nextmode = 'off', fudge = -fudge*2),['side']
# )

module.add_path(Rect(V(partion_side-17.125-tab_length, 0), centred=True, width = tab_length*2 + fudge, height = thickness + fudge, rad = 0), ['side'])

module.add_path(Rect(V(partion_side-55.125-tab_length, 0), centred=True, width = tab_length*2 + fudge, height = thickness + fudge, rad = 0), ['side'])
