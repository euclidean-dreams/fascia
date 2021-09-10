# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ImpresarioSerialization

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PitchProcessorParameters(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PitchProcessorParameters()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPitchProcessorParameters(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PitchProcessorParameters
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PitchProcessorParameters
    def Method(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # PitchProcessorParameters
    def Threshold(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PitchProcessorParameters
    def Silence(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(3)
def PitchProcessorParametersStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddMethod(builder, method): builder.PrependInt8Slot(0, method, 0)
def PitchProcessorParametersAddMethod(builder, method):
    """This method is deprecated. Please switch to AddMethod."""
    return AddMethod(builder, method)
def AddThreshold(builder, threshold): builder.PrependFloat32Slot(1, threshold, 0.0)
def PitchProcessorParametersAddThreshold(builder, threshold):
    """This method is deprecated. Please switch to AddThreshold."""
    return AddThreshold(builder, threshold)
def AddSilence(builder, silence): builder.PrependFloat32Slot(2, silence, 0.0)
def PitchProcessorParametersAddSilence(builder, silence):
    """This method is deprecated. Please switch to AddSilence."""
    return AddSilence(builder, silence)
def End(builder): return builder.EndObject()
def PitchProcessorParametersEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)