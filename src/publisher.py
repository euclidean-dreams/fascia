from time import sleep

import flatbuffers
import zmq

from ImpresarioSerialization import IdentifierWrapper, Identifier, Axiomology, Phenomenon


class Publisher:
    def __init__(self, context, endpoint):
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(endpoint)
        sleep(1)

    def send_axiomology(self, axioms):
        identifier_builder = flatbuffers.Builder(0)
        IdentifierWrapper.IdentifierWrapperStart(identifier_builder)
        IdentifierWrapper.IdentifierWrapperAddIdentifier(
            identifier_builder, Identifier.Identifier.axiomology
        )
        identifier_builder.Finish(IdentifierWrapper.IdentifierWrapperEnd(identifier_builder))

        # wildcards
        axiomology_builder = flatbuffers.Builder(0)
        Axiomology.StartAxiomsVector(axiomology_builder, len(axioms))
        for axiom in reversed(axioms):
            axiomology_builder.PrependFloat32(axiom)
        value_offset = axiomology_builder.EndVector()

        # fields
        Axiomology.Start(axiomology_builder)
        Axiomology.AddAxioms(axiomology_builder, value_offset)

        # finish
        axiomology_builder.Finish(Axiomology.End(axiomology_builder))
        message = [identifier_builder.Output(), axiomology_builder.Output()]
        self.socket.send_multipart(message)

    def send_phenomenon(self, identity, quantity):
        identifier_builder = flatbuffers.Builder(0)
        IdentifierWrapper.IdentifierWrapperStart(identifier_builder)
        IdentifierWrapper.IdentifierWrapperAddIdentifier(
            identifier_builder, Identifier.Identifier.phenomenon
        )
        identifier_builder.Finish(IdentifierWrapper.IdentifierWrapperEnd(identifier_builder))

        # fields
        phenomenon_builder = flatbuffers.Builder(0)
        Phenomenon.Start(phenomenon_builder)
        Phenomenon.AddIdentity(phenomenon_builder, identity)
        Phenomenon.AddQuantity(phenomenon_builder, quantity)

        # finish
        phenomenon_builder.Finish(Phenomenon.End(phenomenon_builder))
        message = [identifier_builder.Output(), phenomenon_builder.Output()]
        self.socket.send_multipart(message)
