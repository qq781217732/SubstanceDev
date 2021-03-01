# ADOBE CONFIDENTIAL
#
# Copyright 2019 Adobe
# All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
#

# =======================================================================================
# INTERNAL USE ONLY
# =======================================================================================
# Global variable used to store the CTypes binary from the C++ application
__runtimeCTypesBinary = None


def setRuntimeBinary(aRuntimeCTypesBinary):
    global __runtimeCTypesBinary
    __runtimeCTypesBinary = aRuntimeCTypesBinary


def getRuntimeBinary():
    return __runtimeCTypesBinary


# =======================================================================================
__gContext = None


def getContext():
    from sd import context

    global __gContext
    if not __gContext:
        __gContext = context.Context()
    return __gContext
