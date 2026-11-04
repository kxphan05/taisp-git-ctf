# Decodes a message that was Caesar-shifted by 7 letters.
# Only letters are shifted; digits and symbols are unchanged.
# Run it: python3 decoder.py
# It prints garbage. Fix the bug so it prints the flag.
SHIFT = 7
ENCODED = "AHPZW{jshbkl_mpelk_pa}"

def decode(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out

print(decode(ENCODED, SHIFT))
