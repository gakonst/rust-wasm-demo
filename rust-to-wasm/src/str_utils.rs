#[no_mangle]
pub extern fn reverse_string(pointer: *mut u8, length: usize) -> *const u8 {
    let slice: &[u8] = unsafe { std::slice::from_raw_parts(pointer, length) };
    let string = std::str::from_utf8(slice).unwrap();
    let result = string.chars().rev().collect::<String>();
    result.into_bytes().as_ptr()
}