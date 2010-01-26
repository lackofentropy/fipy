#!/usr/bin/env python

## 
 # -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "stdyConvDiffScEquation.py"
 #                                    created: 12/6/03 {10:39:23 AM} 
 #                                last update: 9/3/04 {10:41:40 PM} 
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-12 JEG 1.0 original
 # ###################################################################
 ##

from fipy.equations.matrixEquation import MatrixEquation
from fipy.terms.transientTerm import TransientTerm
from fipy.terms.implicitDiffusionTerm import ImplicitDiffusionTerm
from fipy.terms.powerLawConvectionTerm import PowerLawConvectionTerm
from fipy.terms.scSourceTerm import ScSourceTerm

class SteadyConvectionDiffusionScEquation(MatrixEquation):
    """
    Diffusion equation is implicit.
    """    
    def __init__(self,
                 var,
                 diffusionCoeff = 1.,
		 convectionCoeff = 1.,
                 sourceCoeff = 0.,
                 solver='default_solver',
		 convectionScheme = PowerLawConvectionTerm,
                 boundaryConditions=()):
		     
	mesh = var.getMesh()
	
	diffusionTerm = ImplicitDiffusionTerm(diffusionCoeff,mesh,boundaryConditions)
	convectionTerm = convectionScheme(convectionCoeff, mesh, boundaryConditions, diffusionTerm)
        sourceTerm = ScSourceTerm(sourceCoeff, mesh)

	terms = (
	    diffusionTerm,
	    convectionTerm,
            sourceTerm
            )
	    
	MatrixEquation.__init__(
            self,
            var,
            terms,
            solver)
