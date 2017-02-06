hexvar = raw_input("Input hex char: ")

base64var = hexvar.decode("hex").encode("base64")

print base64var
