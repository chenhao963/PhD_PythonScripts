"""
Script to read in Odb and open Abaqus CAE with the required:
displaygroups/viewport options.
Can also print files directly from script??
"""

#open modulus, create viewport and open odb
from abaqus import *
from abaqusConstants import *
import displayGroupOdbToolset
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=268.952117919922,
height=154.15299987793)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
leafTest = LeafFromElementLables(partInstanceName='I_Cube', elementLabels = '1,2,4,5,6,7,8:1024')
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(name='/home/cerecam/Desktop/GP_BoundaryConditionTests/Flux2_NoUEL.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
### CREATE OUTPUT ###
session.DisplayGroup(name='Tester', leaf= leafTest)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
CONTOURS_ON_DEF, ))
session.printToFile(fileName='/home/cerecam/Desktop/GP_BoundaryConditionTests/PrintToFileExample', format=TIFF, canvasObjects=(
session.viewports['Viewport: 1'], ))
