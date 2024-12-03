# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import numpy as np


def assignMaterial(polyNUM):
    MaterialName = 'Material-' + str(polyNUM)
    sectionName = 'Section-' + str(polyNUM)
    regionName = 'POLY' + str(polyNUM)
    modelName = 'g10hax0'
    partName = 'TESS'
    
    
    # User material properties
    devper = 10
    mat1 = 1    
    mat2 = 2
    mat3 = 3
    mat4 = 4
    
    
    # Do not change the following code unless you know what you are doing
    p = mdb.models[modelName].parts[partName]
    mdb.models[modelName].Material(name=MaterialName)
    mdb.models[modelName].materials[MaterialName].Depvar(n=devper)
    mdb.models[modelName].materials[MaterialName].UserMaterial(
        mechanicalConstants=(mat1, mat2, mat3, mat4))
    mdb.models[modelName].HomogeneousSolidSection(name=sectionName, 
        material=MaterialName, thickness=None)
    p = mdb.models[modelName].parts[partName]
    region = p.sets[regionName]
    p.SectionAssignment(region=region, sectionName=sectionName, offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


# loop through all grains
for i in range(1, 11):
    assignMaterial(i)