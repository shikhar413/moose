import openmc

# Define material fills as materials
rgmb_region_1 = openmc.Material(name="rgmb_region_1")
rgmb_region_1.add_nuclide('U235', 0.03)
rgmb_region_1.add_nuclide('U238', 0.97)
rgmb_region_1.add_nuclide('O16', 2.0)
rgmb_region_1.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1])
openmc_mats.export_to_xml()

# Define surfaces
pin1_radial_duct_0_surf_0 = openmc.Plane(d=-0.710315, b=-0.866025, c=-1.21574e-18, a=-0.5, boundary_type='vacuum')
pin1_radial_duct_0_surf_1 = openmc.Plane(d=-0.710315, b=-0.866025, c=2.25114e-18, a=0.5, boundary_type='vacuum')
pin1_radial_duct_0_surf_2 = openmc.Plane(d=-0.710315, b=-4.0608e-16, c=1.85037e-18, a=1, boundary_type='vacuum')
pin1_radial_duct_0_surf_3 = openmc.Plane(d=-0.710315, b=0.866025, c=5.65787e-19, a=0.5, boundary_type='vacuum')
pin1_radial_duct_0_surf_4 = openmc.Plane(d=-0.710315, b=0.866025, c=6.48672e-19, a=-0.5, boundary_type='vacuum')
pin1_radial_duct_0_surf_5 = openmc.Plane(d=-0.710315, b=6.76799e-16, c=1.85037e-18, a=-1, boundary_type='vacuum')

# Define cells, universes, and lattices
pin1_cell_radial_0 = openmc.Cell(fill=rgmb_region_1)
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0])
pin1_root_cell = openmc.Cell(fill=pin1_univ, region=(+pin1_radial_duct_0_surf_0 & +pin1_radial_duct_0_surf_1 & +pin1_radial_duct_0_surf_2 & +pin1_radial_duct_0_surf_3 & +pin1_radial_duct_0_surf_4 & +pin1_radial_duct_0_surf_5))
root_universe = openmc.Universe(cells=[pin1_root_cell])
geom = openmc.Geometry(root_universe)
geom.export_to_xml()

# Define settings
point = openmc.stats.Point((0, 0, 0))
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
xy_plot.origin = (0, 0, 0)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (5, 5)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
