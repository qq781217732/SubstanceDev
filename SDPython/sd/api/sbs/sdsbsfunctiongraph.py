# ADOBE CONFIDENTIAL
#
# Copyright 2020 Adobe
# All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
#
# Autogenerated by ipa. Don't edit directly, edit the definitions and regenerate it when changing
#

import ctypes
import base64
import sd
from ..sdapiobject import SDAPIObject
from ..sdgraph import SDGraph
from ..sdapiobject import SDApiError
from ..apiexception import APIException

class SDSBSFunctionGraph(SDGraph):
    """
    Class managing a Substance function graph
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDSBSFunctionGraph
        """
        SDGraph.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(parent):
        """
        Create a new SDSBSFunctionGraph under the specified parent

        :param parent: The parent data that will contains the newly created Function graph. Can be SDPackage or SDResourceFolder
        :type parent: SDAPIObject
        :rtype: SDSBSFunctionGraph
        """
        outResource = ctypes.c_void_p()
        _res = sd.getContext().SDSBSFunctionGraph_sNew(parent.mHandle, ctypes.byref(outResource))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outResource, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outResource.value, ownHandle=True)
