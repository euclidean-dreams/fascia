from time import sleep

import flatbuffers
import zmq

from ImpresarioSerialization import IdentifierWrapper, FloatMorsel, Identifier, FloatArrayMorsel


class MorselMessenger:
    def __init__(self, context, endpoint):
        self.socket = context.socket(zmq.PUB)
        self.socket.connect(endpoint)
        sleep(1)

    def send_float_morsel(self, field, value):
        identity_builder = flatbuffers.Builder(0)
        IdentifierWrapper.IdentifierWrapperStart(identity_builder)
        IdentifierWrapper.IdentifierWrapperAddIdentifier(
            identity_builder, Identifier.Identifier.floatMorsel
        )
        identity_builder.Finish(IdentifierWrapper.IdentifierWrapperEnd(identity_builder))

        morsel_builder = flatbuffers.Builder(0)
        FloatMorsel.FloatMorselStart(morsel_builder)
        FloatMorsel.FloatMorselAddField(morsel_builder, field)
        FloatMorsel.FloatMorselAddValue(morsel_builder, value)
        morsel_builder.Finish(FloatMorsel.FloatMorselEnd(morsel_builder))
        message = [identity_builder.Output(), morsel_builder.Output()]
        self.socket.send_multipart(message)

    def send_float_array_morsel(self, field, values):
        identity_builder = flatbuffers.Builder(0)
        IdentifierWrapper.IdentifierWrapperStart(identity_builder)
        IdentifierWrapper.IdentifierWrapperAddIdentifier(
            identity_builder, Identifier.Identifier.floatArrayMorsel
        )
        identity_builder.Finish(IdentifierWrapper.IdentifierWrapperEnd(identity_builder))

        morsel_builder = flatbuffers.Builder(0)

        FloatArrayMorsel.FloatArrayMorselStartValueVector(morsel_builder, len(values))
        for item in reversed(values):
            morsel_builder.PrependFloat32(item)
        value_offset = morsel_builder.EndVector()

        FloatArrayMorsel.FloatArrayMorselStart(morsel_builder)
        FloatArrayMorsel.FloatArrayMorselAddField(morsel_builder, field)
        FloatArrayMorsel.FloatArrayMorselAddValue(morsel_builder, value_offset)
        morsel_builder.Finish(FloatArrayMorsel.FloatArrayMorselEnd(morsel_builder))
        message = [identity_builder.Output(), morsel_builder.Output()]
        self.socket.send_multipart(message)
