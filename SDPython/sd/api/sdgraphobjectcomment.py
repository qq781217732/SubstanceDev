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
from .sdgraph import SDGraph
from .sdnode import SDNode
from .sdgraphobject import SDGraphObject
from .sdapiobject import SDAPIObject
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDGraphObjectComment(SDGraphObject):
    """
    Class managing a Comment object in the graph
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDGraphObjectComment
        """
        SDGraphObject.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(sdGraph):
        """
        Create a new SDGraphObjectComment instance in the specified graph

        :param sdGraph: The SDGraph that should contains the new SDGraphObjectComment
        :type sdGraph: SDGraph
        :rtype: SDGraphObjectComment
        """
        outSDGraphObjectComment = ctypes.c_void_p()
        _res = sd.getContext().SDGraphObjectComment_sNew(sdGraph.mHandle, ctypes.byref(outSDGraphObjectComment))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDGraphObjectComment, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDGraphObjectComment.value, ownHandle=True)

    @staticmethod
    def sNewAsChild(sdNode):
        """
        Create a new SDGraphObjectComment instance attached to the specified parent node

        :param sdNode: The SDNode used to attach the new SDGraphObjectComment instance
        :type sdNode: SDNode
        :rtype: SDGraphObjectComment
        """
        outSDGraphObjectComment = ctypes.c_void_p()
        _res = sd.getContext().SDGraphObjectComment_sNewAsChild(sdNode.mHandle, ctypes.byref(outSDGraphObjectComment))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDGraphObjectComment, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDGraphObjectComment.value, ownHandle=True)

    def getParent(self):
        """
        Get the parent node of the current SDGraphObjectComment

        :rtype: SDNode
        """
        outSDNode = ctypes.c_void_p()
        _res = self.mAPIContext.SDGraphObjectComment_getParent(self.mHandle, ctypes.byref(outSDNode))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outSDNode, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outSDNode.value, ownHandle=True)
