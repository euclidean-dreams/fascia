// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_PITCHPROCESSORPARAMETERS_IMPRESARIOSERIALIZATION_H_
#define FLATBUFFERS_GENERATED_PITCHPROCESSORPARAMETERS_IMPRESARIOSERIALIZATION_H_

#include "flatbuffers/flatbuffers.h"

#include "PitchMethod_generated.h"

namespace ImpresarioSerialization {

struct PitchProcessorParameters;
struct PitchProcessorParametersBuilder;

struct PitchProcessorParameters FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef PitchProcessorParametersBuilder Builder;
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_METHOD = 4,
    VT_THRESHOLD = 6,
    VT_SILENCE = 8
  };
  ImpresarioSerialization::PitchMethod method() const {
    return static_cast<ImpresarioSerialization::PitchMethod>(GetField<int8_t>(VT_METHOD, 0));
  }
  float threshold() const {
    return GetField<float>(VT_THRESHOLD, 0.0f);
  }
  float silence() const {
    return GetField<float>(VT_SILENCE, 0.0f);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<int8_t>(verifier, VT_METHOD) &&
           VerifyField<float>(verifier, VT_THRESHOLD) &&
           VerifyField<float>(verifier, VT_SILENCE) &&
           verifier.EndTable();
  }
};

struct PitchProcessorParametersBuilder {
  typedef PitchProcessorParameters Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_method(ImpresarioSerialization::PitchMethod method) {
    fbb_.AddElement<int8_t>(PitchProcessorParameters::VT_METHOD, static_cast<int8_t>(method), 0);
  }
  void add_threshold(float threshold) {
    fbb_.AddElement<float>(PitchProcessorParameters::VT_THRESHOLD, threshold, 0.0f);
  }
  void add_silence(float silence) {
    fbb_.AddElement<float>(PitchProcessorParameters::VT_SILENCE, silence, 0.0f);
  }
  explicit PitchProcessorParametersBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<PitchProcessorParameters> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<PitchProcessorParameters>(end);
    return o;
  }
};

inline flatbuffers::Offset<PitchProcessorParameters> CreatePitchProcessorParameters(
    flatbuffers::FlatBufferBuilder &_fbb,
    ImpresarioSerialization::PitchMethod method = ImpresarioSerialization::PitchMethod::schmitt,
    float threshold = 0.0f,
    float silence = 0.0f) {
  PitchProcessorParametersBuilder builder_(_fbb);
  builder_.add_silence(silence);
  builder_.add_threshold(threshold);
  builder_.add_method(method);
  return builder_.Finish();
}

inline const ImpresarioSerialization::PitchProcessorParameters *GetPitchProcessorParameters(const void *buf) {
  return flatbuffers::GetRoot<ImpresarioSerialization::PitchProcessorParameters>(buf);
}

inline const ImpresarioSerialization::PitchProcessorParameters *GetSizePrefixedPitchProcessorParameters(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<ImpresarioSerialization::PitchProcessorParameters>(buf);
}

inline bool VerifyPitchProcessorParametersBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<ImpresarioSerialization::PitchProcessorParameters>(nullptr);
}

inline bool VerifySizePrefixedPitchProcessorParametersBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<ImpresarioSerialization::PitchProcessorParameters>(nullptr);
}

inline void FinishPitchProcessorParametersBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<ImpresarioSerialization::PitchProcessorParameters> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedPitchProcessorParametersBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<ImpresarioSerialization::PitchProcessorParameters> root) {
  fbb.FinishSizePrefixed(root);
}

}  // namespace ImpresarioSerialization

#endif  // FLATBUFFERS_GENERATED_PITCHPROCESSORPARAMETERS_IMPRESARIOSERIALIZATION_H_
