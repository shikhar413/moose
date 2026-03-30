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

rgmb_region_5 = openmc.Material(name="rgmb_region_5")
rgmb_region_5.add_nuclide('U235', 0.03)
rgmb_region_5.add_nuclide('U238', 0.97)
rgmb_region_5.add_nuclide('O16', 2.0)
rgmb_region_5.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3, rgmb_region_5])
openmc_mats.export_to_xml()

# Define surfaces
amg_radial_duct_0_surf_0 = openmc.Plane(d=-1.42063, b=-1, c=2.46716e-18, a=-7.815e-17, boundary_type='vacuum')
amg_radial_duct_0_surf_1 = openmc.Plane(d=-1.42063, b=-1.563e-16, c=0, a=1, boundary_type='vacuum')
amg_radial_duct_0_surf_2 = openmc.Plane(d=-1.42063, b=1, c=0, a=1.563e-16, boundary_type='vacuum')
amg_radial_duct_0_surf_3 = openmc.Plane(d=-1.42063, b=2.3445e-16, c=2.46716e-18, a=-1, boundary_type='vacuum')
pin1_radial_duct_1_surf_0 = openmc.Plane(d=-0.68, b=-1, c=-1.23358e-18, a=-8.1634e-17)
pin1_radial_duct_1_surf_1 = openmc.Plane(d=-0.68, b=-1.63268e-16, c=0, a=1)
pin1_radial_duct_1_surf_2 = openmc.Plane(d=-0.68, b=1, c=0, a=1.63268e-16)
pin1_radial_duct_1_surf_3 = openmc.Plane(d=-0.68, b=2.44902e-16, c=-1.23358e-18, a=-1)
pin1_radial_ring_0 = openmc.ZCylinder(r=0.2, y0=0, x0=0)

# Define cells, universes, and lattices
pin2_cell_radial_0 = openmc.Cell(fill=rgmb_region_3)
pin2_univ = openmc.Universe(cells=[pin2_cell_radial_0])
pin1_cell_radial_2 = openmc.Cell(fill=rgmb_region_5, region=(~(+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3)))
pin1_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=((+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3) & ~(-pin1_radial_ring_0)))
pin1_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_radial_ring_0))
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0, pin1_cell_radial_1, pin1_cell_radial_2])
amg_lattice = openmc.RectLattice()
amg_lattice.pitch = (1.42063, 1.42063)
amg_lattice.lower_left = (-1.42063, -1.42063)
amg_lattice.universes = [
  [pin1_univ, pin1_univ],
  [pin1_univ, pin2_univ]
]
amg_lattice_cell = openmc.Cell(fill=amg_lattice)
amg_univ = openmc.Universe(cells=[amg_lattice_cell])
amg_root_cell = openmc.Cell(fill=amg_univ, region=(+amg_radial_duct_0_surf_0 & +amg_radial_duct_0_surf_1 & +amg_radial_duct_0_surf_2 & +amg_radial_duct_0_surf_3))
root_universe = openmc.Universe(cells=[amg_root_cell])
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
xy_plot.width = (3, 3)
xy_plot.pixels = (1000, 1000)
xy_plot.color_by = 'material'
xy_plot.origin = (0, 0, 0)

yz_plot = openmc.Plot()
yz_plot.filename = 'yzplot'
yz_plot.width = (3, 3)
yz_plot.pixels = (1000, 1000)
yz_plot.color_by = 'material'
yz_plot.basis = 'yz'
yz_plot.origin = (0, 0, 0)

plots = openmc.Plots([xy_plot, yz_plot])
plots.export_to_xml()

openmc.run(threads=1)
openmc.plot_geometry()
