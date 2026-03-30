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

rgmb_region_5 = openmc.Material(name="rgmb_region_5")
rgmb_region_5.add_nuclide('U235', 0.03)
rgmb_region_5.add_nuclide('U238', 0.97)
rgmb_region_5.add_nuclide('O16', 2.0)
rgmb_region_5.set_density('g/cm3', 10.0)

openmc_mats = openmc.Materials([rgmb_region_1, rgmb_region_2, rgmb_region_3, rgmb_region_4, rgmb_region_5])
openmc_mats.export_to_xml()

# Define surfaces
amg_radial_duct_0_surf_0 = openmc.Plane(d=-1.7703, b=-0.866025, c=-8.79484e-19, a=-0.5)
amg_radial_duct_0_surf_1 = openmc.Plane(d=-1.7703, b=-0.866025, c=-1.11789e-18, a=0.5)
amg_radial_duct_0_surf_2 = openmc.Plane(d=-1.7703, b=-3.25871e-16, c=-3.70074e-18, a=1)
amg_radial_duct_0_surf_3 = openmc.Plane(d=-1.7703, b=0.866025, c=-4.08442e-18, a=0.5)
amg_radial_duct_0_surf_4 = openmc.Plane(d=-1.7703, b=0.866025, c=1.10835e-18, a=-0.5)
amg_radial_duct_0_surf_5 = openmc.Plane(d=-1.7703, b=6.51741e-16, c=0, a=-1)
amg_radial_duct_1_surf_0 = openmc.Plane(d=-1.8942, b=-0.866025, c=1.81985e-18, a=-0.5, boundary_type='vacuum')
amg_radial_duct_1_surf_1 = openmc.Plane(d=-1.8942, b=-0.866025, c=4.29766e-19, a=0.5, boundary_type='vacuum')
amg_radial_duct_1_surf_2 = openmc.Plane(d=-1.8942, b=-3.04555e-16, c=3.70074e-18, a=1, boundary_type='vacuum')
amg_radial_duct_1_surf_3 = openmc.Plane(d=-1.8942, b=0.866025, c=-1.38508e-18, a=0.5, boundary_type='vacuum')
amg_radial_duct_1_surf_4 = openmc.Plane(d=-1.8942, b=0.866025, c=-9.248e-19, a=-0.5, boundary_type='vacuum')
amg_radial_duct_1_surf_5 = openmc.Plane(d=-1.8942, b=7.10629e-16, c=-3.70074e-18, a=-1, boundary_type='vacuum')
pin1_radial_duct_1_surf_0 = openmc.Plane(d=-0.3404, b=-0.866025, c=-5.42568e-19, a=-0.5)
pin1_radial_duct_1_surf_1 = openmc.Plane(d=-0.3404, b=-0.866025, c=6.18525e-19, a=0.5)
pin1_radial_duct_1_surf_2 = openmc.Plane(d=-0.3404, b=-4.23684e-16, c=-9.25186e-19, a=1)
pin1_radial_duct_1_surf_3 = openmc.Plane(d=-0.3404, b=0.866025, c=-1.66901e-19, a=0.5)
pin1_radial_duct_1_surf_4 = openmc.Plane(d=-0.3404, b=0.866025, c=2.17908e-19, a=-0.5)
pin1_radial_duct_1_surf_5 = openmc.Plane(d=-0.3404, b=7.06141e-16, c=-9.25186e-19, a=-1)
pin1_radial_ring_0 = openmc.ZCylinder(r=0.1404, y0=0, x0=0)

# Define cells, universes, and lattices
amg_duct_cell_radial_0 = openmc.Cell(fill=rgmb_region_5, region=(~(+amg_radial_duct_0_surf_0 & +amg_radial_duct_0_surf_1 & +amg_radial_duct_0_surf_2 & +amg_radial_duct_0_surf_3 & +amg_radial_duct_0_surf_4 & +amg_radial_duct_0_surf_5)))
pin1_cell_radial_2 = openmc.Cell(fill=rgmb_region_3, region=(~(+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3 & +pin1_radial_duct_1_surf_4 & +pin1_radial_duct_1_surf_5)))
pin1_cell_radial_1 = openmc.Cell(fill=rgmb_region_2, region=((+pin1_radial_duct_1_surf_0 & +pin1_radial_duct_1_surf_1 & +pin1_radial_duct_1_surf_2 & +pin1_radial_duct_1_surf_3 & +pin1_radial_duct_1_surf_4 & +pin1_radial_duct_1_surf_5) & ~(-pin1_radial_ring_0)))
pin1_cell_radial_0 = openmc.Cell(fill=rgmb_region_1, region=(-pin1_radial_ring_0))
pin1_univ = openmc.Universe(cells=[pin1_cell_radial_0, pin1_cell_radial_1, pin1_cell_radial_2])
rgmb_region_4_cell = openmc.Cell(fill=rgmb_region_4)
rgmb_region_4_univ = openmc.Universe(cells=[rgmb_region_4_cell])
amg_lattice_unrotated = openmc.HexLattice()
amg_lattice_unrotated.orientation = 'x'
amg_lattice_unrotated.pitch = (0.7,)
amg_lattice_unrotated.center = (0, 0)
amg_lattice_unrotated.outer = rgmb_region_4_univ
amg_lattice_unrotated.universes = [
  [pin1_univ, pin1_univ, pin1_univ, pin1_univ, pin1_univ, pin1_univ],
  [pin1_univ]
]
amg_lattice_cell = openmc.Cell(fill=amg_lattice_unrotated)
amg_lattice_cell.rotation = (0, 0, 90)
amg_lattice = openmc.Universe(cells=[amg_lattice_cell])
amg_lattice_cell = openmc.Cell(fill=amg_lattice, region=(+amg_radial_duct_0_surf_0 & +amg_radial_duct_0_surf_1 & +amg_radial_duct_0_surf_2 & +amg_radial_duct_0_surf_3 & +amg_radial_duct_0_surf_4 & +amg_radial_duct_0_surf_5))
amg_univ = openmc.Universe(cells=[amg_lattice_cell, amg_duct_cell_radial_0])
amg_root_cell = openmc.Cell(fill=amg_univ, region=(+amg_radial_duct_1_surf_0 & +amg_radial_duct_1_surf_1 & +amg_radial_duct_1_surf_2 & +amg_radial_duct_1_surf_3 & +amg_radial_duct_1_surf_4 & +amg_radial_duct_1_surf_5))
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
