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
from .sdmdlvalue import SDMDLValue
from ..sdapiobject import SDAPIObject
from ..sdapiobject import SDApiError
from ..apiexception import APIException

class SDMDLValueCall(SDMDLValue):
    """
    Class used to store information about a MDL call value
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDMDLValueCall
        """
        SDMDLValue.__init__(self, APIContext, handle, *args, **kwargs)

    def getValue(self):
        """
        Get the value as a string reference those content is implementation defined

        :rtype: string
        """
        outValue = ctypes.c_char_p()
        _res = self.mAPIContext.SDMDLValueCall_getValue(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value.decode('utf-8')

    def setValue(self, value):
        """
        Reset the value of the reference

        :param value: The new item reference value
        :type value: string
        :rtype: None
        """
        _res = self.mAPIContext.SDMDLValueCall_setValue(self.mHandle, ctypes.create_string_buffer(value.encode('utf-8')))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return None
