import argparse
import os
import subprocess
from huggingface_hub import snapshot_download

def download_model(model_id, local_dir):
    snapshot_download(repo_id=model_id, local_dir=local_dir,
                      local_dir_use_symlinks=False, revision="main")

def convert_model(hf_model_dir, outfile, outtype):
    convert_script = os.path.join("llama.cpp", "convert.py")
    subprocess.run(["python", convert_script, hf_model_dir,
                    "--outfile", outfile,
                    "--outtype", outtype])

def main():
    parser = argparse.ArgumentParser(description="Download and convert HuggingFace model to GGUF model")
    parser.add_argument("model_id", help="HuggingFace model ID")
    parser.add_argument("--local_dir", default="vicuna-hf", help="Local directory to save the HuggingFace model (default: vicuna-hf)")
    parser.add_argument("--outfile", default="vicuna.gguf", help="Output GGUF model file name (default: vicuna.gguf)")
    parser.add_argument("--outtype", choices=["q8_0", "f16", "f32"], default="q8_0", help="Output GGUF model type (default: q8_0)")

    args = parser.parse_args()

    # Download HuggingFace model
    download_model(args.model_id, args.local_dir)

    # Convert HF model to GGUF model
    convert_model(args.local_dir, args.outfile, args.outtype)

if __name__ == "__main__":
    main()