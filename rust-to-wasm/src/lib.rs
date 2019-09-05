// Cargo gives a unused import error here, but it is required to call wasm-pack
use wasm_bindgen::prelude::*;

// All functions get exported directly (no modules)
pub mod utils;
pub mod str_utils;
mod private_utils;

#[no_mangle] // If you remove `no_mangle`, the function WILL NOT be exported.
pub fn fun() -> i64 {
    return private_utils::foo()
}