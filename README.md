## Targeted Fuzzing for Unsafe Rust Code: Leveraging Selective Instrumentation

This repo contains data associated with our paper "Targeted Fuzzing for Unsafe Rust Code: Leveraging Selective Instrumentation" which has been accepted to EASE 2025.

### Description

To use FourFuzz you need to:
1. Build and install the FourFuzz compiler.
2. Build your project with the FourFuzz compiler to create the list of unsafe functions (`RUST_UNSAFE_LIST`) and generate the LLVM CG data (`--emit=llvm-bc`). One can provide a list of packages that should be part of the analysis (`RUST_UNSAFE_CRATES`). It is further useful to remove entries for functions that are, e.g., already covered by the seed set.
3. Generate the list of functions that should not be instrumented based on the previously generated list of unsafe functions and the LLVM CG data.
4. Rebuild the target with the list (`AFLRS_LLVM_DENYLIST`) generated in Step 3.
5. Fuzz your target program.

### Citation

```
@inproceedings{Paa2025,
  author = {David Paaßen and Jens-Rene Giesen and Lucas Davi},
  title = {{Targeted Fuzzing for Unsafe Rust Code: Leveraging Selective Instrumentation}},
  booktitle = {International Conference on Evaluation and Assessment in Software Engineering (EASE)},
  year= {2025},
}
```
