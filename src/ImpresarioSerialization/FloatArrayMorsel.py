# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ImpresarioSerialization

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FloatArrayMorsel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FloatArrayMorsel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFloatArrayMorsel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FloatArrayMorsel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FloatArrayMorsel
    def Field(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # FloatArrayMorsel
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FloatArrayMorsel
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # FloatArrayMorsel
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FloatArrayMorsel
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def FloatArrayMorselStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddField(builder, field): builder.PrependUint64Slot(0, field, 0)
def FloatArrayMorselAddField(builder, field):
    """This method is deprecated. Please switch to AddField."""
    return AddField(builder, field)
def AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def FloatArrayMorselAddValue(builder, value):
    """This method is deprecated. Please switch to AddValue."""
    return AddValue(builder, value)
def StartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FloatArrayMorselStartValueVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartValueVector(builder, numElems)
def End(builder): return builder.EndObject()
def FloatArrayMorselEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)