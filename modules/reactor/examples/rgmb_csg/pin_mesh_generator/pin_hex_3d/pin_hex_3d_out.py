import openmc

# Define material fills as materials
rgmb_region_11 = openmc.Material(name="rgmb_region_11")
rgmb_region_11.add_nuclide('U235', 0.03)
rgmb_region_11.add_nuclide('U238', 0.97)
rgmb_region_11.add_nuclide('O16', 2.0)
rgmb_region_11.set_density('g/cm3', 10.0)

rgmb_region_12 = openmc.Material(name="rgmb_region_12")
rgmb_region_12.add_nuclide('U235', 0.03)
rgmb_region_12.add_nuclide('U238', 0.97)
rgmb_region_12.add_nuclide('O16', 2.0)
rgmb_region_12.set_density('g/cm3', 10.0)

rgmb_region_13 = openmc.Material(name="rgmb_region_13")
rgmb_region_13.add_nuclide('U235', 0.03)
rgmb_region_13.add_nuclide('U238', 0.97)
rgmb_region_13.add_nuclide('O16', 2.0)
rgmb_region_13.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_11, rgmb_region_12, rgmb_region_13])
openmc_mats.export_to_xml()

# Define surfaces
pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0 = openmc.ZCylinder(r=0.4665, y0=0, x0=0)
pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0 = openmc.ZCylinder(r=0.4665, y0=0, x0=0)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 = openmc.Plane(d=0.68, b=0, c=0, a=1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 = openmc.Plane(d=0.68, b=0.866025, c=0, a=0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 = openmc.Plane(d=0.68, b=0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 = openmc.Plane(d=0.68, b=1.22465e-16, c=0, a=-1)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 = openmc.Plane(d=0.68, b=-0.866025, c=0, a=-0.5)
pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5 = openmc.Plane(d=0.68, b=-0.866025, c=0, a=0.5)
pin1_radial_boundary_expanded_surf_0 = openmc.Plane(d=0.710315, b=0, c=0, a=1, boundary_type='vacuum')
pin1_radial_boundary_expanded_surf_1 = openmc.Plane(d=0.710315, b=0.866025, c=0, a=0.5, boundary_type='vacuum')
pin1_radial_boundary_expanded_surf_2 = openmc.Plane(d=0.710315, b=0.866025, c=0, a=-0.5, boundary_type='vacuum')
pin1_radial_boundary_expanded_surf_3 = openmc.Plane(d=0.710315, b=1.22465e-16, c=0, a=-1, boundary_type='vacuum')
pin1_radial_boundary_expanded_surf_4 = openmc.Plane(d=0.710315, b=-0.866025, c=0, a=-0.5, boundary_type='vacuum')
pin1_radial_boundary_expanded_surf_5 = openmc.Plane(d=0.710315, b=-0.866025, c=0, a=0.5, boundary_type='vacuum')
rgmb_axial_plane_0 = openmc.Plane(d=1, b=0, c=1, a=0)
rgmb_axial_plane_bottom_boundary = openmc.Plane(d=0, b=0, c=1, a=0, boundary_type='vacuum')
rgmb_axial_plane_top_boundary = openmc.Plane(d=2, b=0, c=1, a=0, boundary_type='vacuum')

# Define cells, universes, and lattices
pin1_ducted_pin_unit_cell_radial_1_axial_1 = openmc.Cell(fill=rgmb_region_13, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5) & +rgmb_axial_plane_0))
pin1_ducted_pin_unit_cell_radial_1_axial_0 = openmc.Cell(fill=rgmb_region_13, region=(~(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5) & -rgmb_axial_plane_0))
pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_1 = openmc.Cell(fill=rgmb_region_12, region=(~(-pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0)))
pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_0 = openmc.Cell(fill=rgmb_region_11, region=(-pin1_ducted_pin_unit_pin_unit_axial_1_radial_ring_0))
pin1_ducted_pin_unit_pin_unit_axial_1_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_0, pin1_ducted_pin_unit_pin_unit_axial_1_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_0_axial_1 = openmc.Cell(fill=pin1_ducted_pin_unit_pin_unit_axial_1_expanded_root, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5 & +rgmb_axial_plane_0))
pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_1 = openmc.Cell(fill=rgmb_region_12, region=(~(-pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0)))
pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_0 = openmc.Cell(fill=rgmb_region_11, region=(-pin1_ducted_pin_unit_pin_unit_axial_0_radial_ring_0))
pin1_ducted_pin_unit_pin_unit_axial_0_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_0, pin1_ducted_pin_unit_pin_unit_axial_0_cell_radial_1])
pin1_ducted_pin_unit_cell_radial_0_axial_0 = openmc.Cell(fill=pin1_ducted_pin_unit_pin_unit_axial_0_expanded_root, region=(-pin1_ducted_pin_unit_radial_duct_0_expanded_surf_0 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_1 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_2 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_3 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_4 & -pin1_ducted_pin_unit_radial_duct_0_expanded_surf_5 & -rgmb_axial_plane_0))
pin1_ducted_pin_unit_expanded_root = openmc.Universe(cells=[pin1_ducted_pin_unit_cell_radial_0_axial_0, pin1_ducted_pin_unit_cell_radial_0_axial_1, pin1_ducted_pin_unit_cell_radial_1_axial_0, pin1_ducted_pin_unit_cell_radial_1_axial_1])
pin1_root_cell = openmc.Cell(fill=pin1_ducted_pin_unit_expanded_root, region=(-pin1_radial_boundary_expanded_surf_0 & -pin1_radial_boundary_expanded_surf_1 & -pin1_radial_boundary_expanded_surf_2 & -pin1_radial_boundary_expanded_surf_3 & -pin1_radial_boundary_expanded_surf_4 & -pin1_radial_boundary_expanded_surf_5 & +rgmb_axial_plane_bottom_boundary & -rgmb_axial_plane_top_boundary))
root_universe = openmc.Universe(cells=[pin1_root_cell])
geom = openmc.Geometry(root_universe)
geom.export_to_xml()

# Define settings
point = openmc.stats.Point((0, 0, 1))
src = openmc.Source(space=point)
settings = openmc.Settings()
settings.source = src
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.export_to_xml()

xy_plot = openmc.Plot()
xy_plot.filename = 'xyplot'
xy_plot.width = (5, 5)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 1)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (5, 5)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 1)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
