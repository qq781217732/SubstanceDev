import sd
import os

from sd.api.mdl.sdmdlgraphdefinition import *

import logging
logger = logging.getLogger(__name__)


class CustomGraph:
    @staticmethod
    def init(aSDGraphDefinitionId = 'custom_graph'):
        context = sd.getContext()
        sdApp = context.getSDApplication()

        # Add MDL Root path
        currentScriptAbsPath = os.path.abspath(os.path.split(__file__)[0])
        mdlRootPath = os.path.join(currentScriptAbsPath, 'data', 'mdl')
        sdApp.getModuleMgr().addRootPath('mdl', mdlRootPath)

        # Create new Graph definition
        graphDefinitionMgr = sdApp.getSDGraphDefinitionMgr()
        assert(graphDefinitionMgr)

        # Add Graph Definition if not already exist
        sdGraphDefinitionId = aSDGraphDefinitionId
        sdGraphDefinition = graphDefinitionMgr.getGraphDefinitionFromId(sdGraphDefinitionId)
        if not sdGraphDefinition:
            sdGraphDefinition = SDMDLGraphDefinition.sNew(sdGraphDefinitionId)
            assert(sdGraphDefinition)
            assert(sdGraphDefinition.getId() == sdGraphDefinitionId)
            sdGraphDefinition.setLabel('Custom Graph')
            sdGraphDefinition.setIconFile(os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'custom_graph_icon.png'))
            # Add the new graph definition
            graphDefinitionMgr.addGraphDefinition(sdGraphDefinition)
        else:
            assert(sdGraphDefinition.getId() == sdGraphDefinitionId)

        # Add some Node definition to teh graph definition
        sdModuleMgr = sdApp.getModuleMgr()
        sdModules = sdModuleMgr.getModules()
        selectedDefinitions = []
        selectedTypes = []
        for sdModule in sdModules:
            sdModuleId = sdModule.getId()

            # Discard non 'mdl' modules
            if not sdModuleId.startswith('mdl::'):
                continue

            # Add some definitions from the MDL 'builtin' module
            if sdModuleId == 'mdl::<builtins>':
                # Add some base types
                baseTypes = ['bool', 'bool2', 'bool3', 'bool4',
                             'int', 'int2', 'int3', 'int4',
                             'float', 'float2', 'float3', 'float4',
                             'double', 'double2', 'double3', 'double4',
                             'string', 'mdl::texture_2d']
                for sdType in sdModule.getTypes():
                    sdTypeId = sdType.getId()
                    logger.debug(sdTypeId)
                    if sdTypeId in baseTypes:
                        # Add some base Types
                        selectedTypes.append(sdType)
                    elif sdTypeId.startswith('matrix<'):
                        # Add matrices
                        selectedTypes.append(sdType)

                continue


            # Add all definitions from the MDL module 'mtlx'
            if sdModuleId.startswith('mdl::custom_graph'):
                for sdDefinition in sdModule.getDefinitions():
                    selectedDefinitions.append(sdDefinition)
                continue

        # Add the selected types
        for sdType in selectedTypes:
            # existingNodeDefinition = sdGraphDefinition.getNodeDefinitionFromId(definition.getId())
            # if existingNodeDefinition:
            #     sdGraphDefinition.removeNodeDefinition(existingNodeDefinition)

            logger.debug('[%s] Adding Type "%s"' % (sdGraphDefinition.getId(), sdType.getId()))
            sdGraphDefinition.addType(sdType)

        # Add the selected node definitions
        for definition in selectedDefinitions:
            existingNodeDefinition = sdGraphDefinition.getDefinitionFromId(definition.getId())
            if existingNodeDefinition:
                sdGraphDefinition.removeDefinition(existingNodeDefinition)

            logger.debug('[%s] Adding Definition "%s"' % (sdGraphDefinition.getId(), definition.getId()))
            sdGraphDefinition.addDefinition(definition)

    @staticmethod
    def uninit():
        pass
