import openmc

# Define material fills as materials
rgmb_region_1 = openmc.Material(name="rgmb_region_1")
rgmb_region_1.add_nuclide('U235', 0.03)
rgmb_region_1.add_nuclide('U238', 0.97)
rgmb_region_1.add_nuclide('O16', 2.0)
rgmb_region_1.set_density('g/cm3', 10.0)

rgmb_region_2 = openmc.Material(name="rgmb_region_2")
rgmb_region_2.add_nuclide('U235', 0.03)
rgmb_region_2.add_nuclide('U238', 0.97)
rgmb_region_2.add_nuclide('O16', 2.0)
rgmb_region_2.set_density('g/cm3', 10.0)

rgmb_region_3 = openmc.Material(name="rgmb_region_3")
rgmb_region_3.add_nuclide('U235', 0.03)
rgmb_region_3.add_nuclide('U238', 0.97)
rgmb_region_3.add_nuclide('O16', 2.0)
rgmb_region_3.set_density('g/cm3', 10.0)

rgmb_region_4 = openmc.Material(name="rgmb_region_4")
rgmb_region_4.add_nuclide('U235', 0.03)
rgmb_region_4.add_nuclide('U238', 0.97)
rgmb_region_4.add_nuclide('O16', 2.0)
rgmb_region_4.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3, rgmb_region_4])
openmc_mats.export_to_xml()

# Define surfaces
pin1_radial_duct_3_surf_0 = openmc.Plane(d=-0.710315, b=-1, c=1.23358e-18, a=-7.815e-17, boundary_type='vacuum')
pin1_radial_duct_3_surf_1 = openmc.Plane(d=-0.710315, b=-1.563e-16, c=0, a=1, boundary_type='vacuum')
pin1_radial_duct_3_surf_2 = openmc.Plane(d=-0.710315, b=1, c=0, a=1.563e-16, boundary_type='vacuum')
pin1_radial_duct_3_surf_3 = openmc.Plane(d=-0.710315, b=2.3445e-16, c=1.23358e-18, a=-1, boundary_type='vacuum')
pin1_radial_ring_0 = openmc.ZCylinder(r=0.3385, y0=0, x0=0)
pin1_radial_ring_1 = openmc.ZCylinder(r=0.3705, y0=0, x0=0)
pin1_radial_ring_2 = openmc.ZCylinder(r=0.4665, y0=0, x0=0)

# Define cells, universes, and lattices
pin1_cell_radial_3 = openmc.Cell(fill=rgmb_region_4, region=(~(-pin1_radial_ring_2)))
pin1_cell_radial_2 = openmc.Cell(fill=rgmb_region_3, region=(-pin1_radial_ring_2 & ~(-pin1_radial_ring_1)))
pin1_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=(-pin1_radial_ring_1 & ~(-pin1_radial_ring_0)))
pin1_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_radial_ring_0))
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0, pin1_cell_radial_1, pin1_cell_radial_2, pin1_cell_radial_3])
pin1_root_cell = openmc.Cell(fill=pin1_univ, region=(+pin1_radial_duct_3_surf_0 & +pin1_radial_duct_3_surf_1 & +pin1_radial_duct_3_surf_2 & +pin1_radial_duct_3_surf_3))
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
