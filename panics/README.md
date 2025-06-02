## Bugs

While testing, FourFuzz detected several bugs in software in out test set.
We prodive an overview including an example input that triggers the respective panic.

| Project | Fuzz target | Bug ID | Input | Status |
| ------- | ----------- | -----  | --- | ------ |
| syn     | parse_file  | 01     | b60f0515182325d25d7e885b8f0bcc595561f5e269a12e698de185828faeba3b | fixed |
| image   | fuzz_guess  | 02     | 69d05d1411c1ef1cdb88455cea295708c876df30650f7b7a3d3cf3ba9b6c1a3b | fixed |
| image   | fuzz_guess  | 03     | e6c7cf90379ac17575652d9e9186901477833f183d6bf0699118cca6c78d31b5 | fixed |
| image   | fuzz_guess  | 04     | ae383581843aec6012db9fa71173a0dc44075d5ac287d7bb7fa3e24426bfa831 | fixed |
| image   | fuzz_guess  | 05     | 770e1951df475f04659ea7357218675d12a688cf2e6979a46d37e7f8ae326868 | fixed |
| image   | fuzz_guess  | 06     | 63d890332eb0eb1c7d0e54ac067cffb303692daafa02e0a6d4e76271f7f9a7a2 | fixed |
| image   | fuzz_guess  | 07     | 3b72253deace200fbee95d12472f76a051f696aeed973af875402fae0b6006f1 | fixed |
| image   | fuzz_guess  | 08     | aef3b7f746d7c4c2de68a488b774b086b1af4ea24548ba8b02aae82ee1eb40f8 | fixed |
| image   | fuzz_guess  | 09     | 973637d38d2a2af9ecb773dcc5e3d4c62bb0e070c34b8e42ebfcaea4fffe9141 | fixed |
| image   | fuzz_guess  | 10     | be432099b1165a0c77ad52612fb371d092fc9ad879bc1f97b64a1a69ac56bea8 | fixed |
| image   | fuzz_guess  | 11     | e38fe52e667604eaac896a3df534ac38eb891c8ae8ad382177a524c69b819225 | fixed |
| image   | fuzz_guess  | 12     | cdae2fe1da0cb9d1a9c33497f733238daacfb627fd748c94b69a88063b614b34 | fixed |
| image   | fuzz_guess  | 13     | e7e0b2760b4180c08918710e5186e905202d6b77afccd34cc2d2287aa109a8f7 | [issue](https://github.com/image-rs/jpeg-decoder/issues/277) |
| rust-cssparser | cssparser | 14 | 64a4f3d80c6f9598cfc40255f7410db68675019d5c2be9eb5555ca5721c29516 | [issue](https://github.com/servo/rust-cssparser/issues/405) |
| toml | parse_document | 15 | 00d516b4f2705f509c4ac9106d0781215a43b8420c43b5ec3ecdcdb120669816 | fixed |



