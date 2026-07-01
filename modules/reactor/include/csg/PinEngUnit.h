//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#pragma once

#include "CSGCellEngUnit.h"
#include "CSGBase.h"

namespace CSG
{

/**
 * PinEngUnit is a CSGCellEngUnit that represents a collection of concentric rings of a pin
 * with their axes all aligned with the z-axis. Each ring is represented by an infinite z-cylinder.
 *
 * Implements:
 *   - expandUnit(): creates a CSGZCylinder surface for each ring in _internal_base defines the cell and material fill of each incremental radial region
 *   - clone(): returns a deep copy
 *   - getAttributes(): returns ring radii, and list of materials corresponding to each incremental radial region
 */
class PinEngUnit : public CSGCellEngUnit
{
public:
  /**
   * @brief Constructor for PinEngUnit
   *
   * @param name unique name of the unit
   * @param ring_radii list of radii corresponding to each ring in the pin
   * @param fill_mats list of fill materials of each incremental radial region
   */
  PinEngUnit(const std::string & name, const std::vector<Real> & radii, const std::vector<std::string> & fill_mats);

  /**
   * @brief Return the pin attributes for this object.
   *
   * @return map containing: ring_radii (std::vector<Real>) and fill_mats (std::vector<std::string>)
   */
  std::unordered_map<std::string, AttributeVariant> getAttributes() const override;

protected:
  /**
   * @brief Return a deep copy of this unit.
   *
   * @return unique_ptr to a new PinEngUnit with identical parameters
   */
  std::unique_ptr<CSGCellEngUnit> clone() const override;

  /**
   * @brief Represent the pin as a universe with cells and surfaces corresponding to each radial region
   */
  void expandUnit() override;

private:
  /// Number of sides of the regular polygon
  const std::vector<Real> _radii;

  /// Distance from the polygon center to the midpoint of each side
  const std::vector<std::string> _fill_mats;
};

} // namespace CSG
