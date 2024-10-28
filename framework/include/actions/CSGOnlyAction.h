//* This file is part of the MOOSE framework
//* https://www.mooseframework.org
//*
//* All rights reserved, see COPYRIGHT for full restrictions
//* https://github.com/idaholab/moose/blob/master/COPYRIGHT
//*
//* Licensed under LGPL 2.1, please see LICENSE for details
//* https://www.gnu.org/licenses/lgpl-2.1.html

#pragma once

#include "Action.h"

<<<<<<< HEAD
/**
 * Outputs the Constructive Solid Geometry to file then exits
 */
=======
>>>>>>> 1cdf47d43b (Preliminary design of csg_only action)
class CSGOnlyAction : public Action
{
public:
  static InputParameters validParams();

  CSGOnlyAction(const InputParameters & params);

  virtual void act() override;
<<<<<<< HEAD

protected:
  std::unique_ptr<CSG::CSGBase> _csg_mesh;
=======
>>>>>>> 1cdf47d43b (Preliminary design of csg_only action)
};
