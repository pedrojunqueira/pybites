#  2:
#   3:
#   4: def gen_hex_color():
#   5:     while True:
# - 6:         (r, g, b) = sample(range(0, 256), 3)
# + 6:         (r, g, b) = sample(range(1, 256), 3)
#   7:         yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()
# --------------------------------------------------------------------------------
