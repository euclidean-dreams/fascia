// automatically generated by the FlatBuffers compiler, do not modify


#ifndef FLATBUFFERS_GENERATED_DISPLAYSIGNAL_IMPRESARIOSERIALIZATION_H_
#define FLATBUFFERS_GENERATED_DISPLAYSIGNAL_IMPRESARIOSERIALIZATION_H_

#include "flatbuffers/flatbuffers.h"

namespace ImpresarioSerialization {

struct DisplaySignal;
struct DisplaySignalBuilder;

struct DisplaySignal FLATBUFFERS_FINAL_CLASS : private flatbuffers::Table {
  typedef DisplaySignalBuilder Builder;
  enum FlatBuffersVTableOffset FLATBUFFERS_VTABLE_UNDERLYING_TYPE {
    VT_ORIGINTIMESTAMP = 4,
    VT_SAMPLES = 6
  };
  uint64_t originTimestamp() const {
    return GetField<uint64_t>(VT_ORIGINTIMESTAMP, 0);
  }
  const flatbuffers::Vector<float> *samples() const {
    return GetPointer<const flatbuffers::Vector<float> *>(VT_SAMPLES);
  }
  bool Verify(flatbuffers::Verifier &verifier) const {
    return VerifyTableStart(verifier) &&
           VerifyField<uint64_t>(verifier, VT_ORIGINTIMESTAMP) &&
           VerifyOffset(verifier, VT_SAMPLES) &&
           verifier.VerifyVector(samples()) &&
           verifier.EndTable();
  }
};

struct DisplaySignalBuilder {
  typedef DisplaySignal Table;
  flatbuffers::FlatBufferBuilder &fbb_;
  flatbuffers::uoffset_t start_;
  void add_originTimestamp(uint64_t originTimestamp) {
    fbb_.AddElement<uint64_t>(DisplaySignal::VT_ORIGINTIMESTAMP, originTimestamp, 0);
  }
  void add_samples(flatbuffers::Offset<flatbuffers::Vector<float>> samples) {
    fbb_.AddOffset(DisplaySignal::VT_SAMPLES, samples);
  }
  explicit DisplaySignalBuilder(flatbuffers::FlatBufferBuilder &_fbb)
        : fbb_(_fbb) {
    start_ = fbb_.StartTable();
  }
  flatbuffers::Offset<DisplaySignal> Finish() {
    const auto end = fbb_.EndTable(start_);
    auto o = flatbuffers::Offset<DisplaySignal>(end);
    return o;
  }
};

inline flatbuffers::Offset<DisplaySignal> CreateDisplaySignal(
    flatbuffers::FlatBufferBuilder &_fbb,
    uint64_t originTimestamp = 0,
    flatbuffers::Offset<flatbuffers::Vector<float>> samples = 0) {
  DisplaySignalBuilder builder_(_fbb);
  builder_.add_originTimestamp(originTimestamp);
  builder_.add_samples(samples);
  return builder_.Finish();
}

inline flatbuffers::Offset<DisplaySignal> CreateDisplaySignalDirect(
    flatbuffers::FlatBufferBuilder &_fbb,
    uint64_t originTimestamp = 0,
    const std::vector<float> *samples = nullptr) {
  auto samples__ = samples ? _fbb.CreateVector<float>(*samples) : 0;
  return ImpresarioSerialization::CreateDisplaySignal(
      _fbb,
      originTimestamp,
      samples__);
}

inline const ImpresarioSerialization::DisplaySignal *GetDisplaySignal(const void *buf) {
  return flatbuffers::GetRoot<ImpresarioSerialization::DisplaySignal>(buf);
}

inline const ImpresarioSerialization::DisplaySignal *GetSizePrefixedDisplaySignal(const void *buf) {
  return flatbuffers::GetSizePrefixedRoot<ImpresarioSerialization::DisplaySignal>(buf);
}

inline bool VerifyDisplaySignalBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifyBuffer<ImpresarioSerialization::DisplaySignal>(nullptr);
}

inline bool VerifySizePrefixedDisplaySignalBuffer(
    flatbuffers::Verifier &verifier) {
  return verifier.VerifySizePrefixedBuffer<ImpresarioSerialization::DisplaySignal>(nullptr);
}

inline void FinishDisplaySignalBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<ImpresarioSerialization::DisplaySignal> root) {
  fbb.Finish(root);
}

inline void FinishSizePrefixedDisplaySignalBuffer(
    flatbuffers::FlatBufferBuilder &fbb,
    flatbuffers::Offset<ImpresarioSerialization::DisplaySignal> root) {
  fbb.FinishSizePrefixed(root);
}

}  // namespace ImpresarioSerialization

#endif  // FLATBUFFERS_GENERATED_DISPLAYSIGNAL_IMPRESARIOSERIALIZATION_H_
