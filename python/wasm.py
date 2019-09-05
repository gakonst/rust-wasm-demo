from wasmer import Instance

fname = '../rust-to-wasm/pkg/wasm_rust.wasm'

wasm_bytes = open(fname, 'rb').read()
instance = Instance(wasm_bytes)

print("Exported functions:", instance.exports)
f = instance.exports.sum
result = f(2, 37)
assert result == 39

# Note that even though we defined the function only for u32, negative numbers
# can be used since Python is not type safe (or is this a WASM thing?)
result = f(-5, -10)
assert result == -15

# Working with strings is slightly more involved
rev = instance.exports.reverse_string
bytestr = b"asdf"
mem_view = instance.memory.uint8_view()
# load our string to memory
for i, c in enumerate(bytestr):
    mem_view[i] = c
# apply the function
# get the address where our reversed string is
result = rev(0, len(bytestr))

# load the result from memory
codes = mem_view[result:result+len(bytestr)]
rev = ''
for i, c in enumerate(codes):
    rev += chr(c)
reversed = rev.encode()
assert reversed == b"fdsa"