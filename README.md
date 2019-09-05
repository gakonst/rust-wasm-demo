1. `pip install wasmer`
1. `cargo install wasm-pack` or [from the official website](https://rustwasm.github.io/wasm-pack/)
1. Add `wasm-bindgen = "0.2.50"` to your `Cargo.toml`
1. Add the following your `Cargo.toml`. [Reason](https://doc.rust-lang.org/edition-guide/rust-2018/platform-and-target-support/cdylib-crates-for-c-interoperability.html).
```toml 
[lib]
crate-type = ["cdylib"]
```
1. Write your Rust code. I've included a simple example of a multi-file project.
1. Run wasm-pack with interface types enabled. This is an expeirmental feature
   so you need to execute: `WASM_INTERFACE_TYPES=1` wasm-pack build
1. You will find your WASM compiled file under `./pkg`.
1. Import it to your favorite language.
1. `cd python && python wasm.py && cd ..`
1. `cd node && node wasm.js && cd ..`
1. `cd golang && go run wasm.go && cd ..`

## Useful Resources

1. https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_wasm
1. https://hacks.mozilla.org/2019/08/webassembly-interface-types/