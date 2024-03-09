# hf_gguf_converter

A tool for converting HuggingFace models to GGUF models (e.g. for use with llama.cpp)

#### Before running
Fetch the necessary submodules:
`git submodule update --init --recursive`

#### Usage
  convert_hf_to_gguf.py <model_id> [--local_dir <local_dir>] [--outfile <outfile>] [--outtype <outtype>]
  convert_hf_to_gguf.py (-h | --help)

#### Arguments
  model_id              HuggingFace model ID to download and convert

#### Options
  -h --help             Show this help message and exit
  --local_dir <local_dir>    Local directory to save the HuggingFace model [default: vicuna-hf]
  --outfile <outfile>  Output GGUF model file name [default: vicuna.gguf]
  --outtype <outtype>  Output GGUF model type [default: q8_0]
                        Options:
                          q8_0: 8-bit quantized
                          f16: 16-bit floating point
                          f32: 32-bit floating point
