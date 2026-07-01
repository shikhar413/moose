//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#include "PinEngUnit.h"
#include "CSGZCylinder.h"

namespace CSG
{

PinEngUnit::PinEngUnit(const std::string & name, const std::vector<Real> & radii, const std::vector<std::string> & fill_mats)
  : CSGCellEngUnit(name, MooseUtils::prettyCppType<PinEngUnit>()),
    _radii(radii),
    _fill_mats(fill_mats)
{
  // Check radii in ascending order
  for (const auto i : make_range(_radii.size() - 1))
    if (_radii[i] >= _radii[i + 1])
      mooseError("Pin engineering unit must have radii defined in strictly ascending order");

  // Check ring radii and fill mat size agree
  if (_radii.size() != _fill_mats.size())
    mooseError("Pin engineering unit must have the same number of elements in ring radii and fill materials");
}

std::unordered_map<std::string, AttributeVariant>
PinEngUnit::getAttributes() const
{
  return {{"radii", _radii}, {"fill_mats", _fill_mats}};
}

std::unique_ptr<CSGCellEngUnit>
PinEngUnit::clone() const
{
  return std::make_unique<PinEngUnit>(_name, _radii, _fill_mats);
}

void
PinEngUnit::expandUnit()
{
  // Create separate universe that will be the container for all cells that represent
  // radial pin rings
  const auto & pin_univ = _internal_base->createUniverse(_name + "_univ");

  unsigned int radial_index = 0;
  CSG::CSGRegion inner_region, outer_region;
  std::vector<std::reference_wrapper<const CSG::CSGSurface>> radial_ring_surfaces;
  // Add surfaces, regions, and cells corresponding to pin rings
  for (const auto & radius : _radii)
  {
    CSG::CSGRegion radial_region;
    bool is_last_radial_region = radial_index == _radii.size() - 1;
    const auto surf_name = _name + "_radial_ring_" + std::to_string(radial_index);
    std::unique_ptr<CSG::CSGSurface> ring_surf_ptr =
        std::make_unique<CSG::CSGZCylinder>(surf_name, 0, 0, radius);
    const auto & ring_surf = _internal_base->addSurface(std::move(ring_surf_ptr));
    radial_ring_surfaces.push_back(ring_surf);

    if (inner_region.getRegionType() == CSG::CSGRegion::RegionType::EMPTY)
    {
      if (!is_last_radial_region)
      {
        // We are in the innermost radial region, the radial region is inner_region
        inner_region = -ring_surf;
        radial_region = inner_region;
      }
    }
    else
    {
      // For all other regions, the radial region is the intersection of inner_region and
      // outer_region
      outer_region = ~inner_region;
      inner_region = -ring_surf;
      radial_region = is_last_radial_region ? outer_region : (inner_region & outer_region);
    }

    auto cell_name = _name + "_cell_radial_" + std::to_string(radial_index);
    const auto mat_name = _fill_mats[radial_index];
    _internal_base->createCell(cell_name, mat_name, radial_region, &pin_univ);

    ++radial_index;
  }

  // Create new cell to bound universe based on pin outer boundaries and add this cell to the root
  // universe
  auto pin_region = -radial_ring_surfaces.back();
  _internal_base->createCell(_name + "_root_cell", pin_univ, pin_region);
}

} // namespace CSG
