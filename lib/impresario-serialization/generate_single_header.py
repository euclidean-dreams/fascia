import os

with open("include/ImpresarioSerialization.h", "w") as outputFile:
    headers = os.listdir("compiled/cpp")
    outputFile.write("#ifndef IMPRESARIO_SERIALIZATION_H\n")
    outputFile.write("#define IMPRESARIO_SERIALIZATION_H\n")
    outputFile.write("\n")

    for header in headers:
        outputFile.write(f"#include \"../compiled/cpp/{header}\"\n")

    outputFile.write("\n")
    outputFile.write("#endif //IMPRESARIO_SERIALIZATION_H\n")
