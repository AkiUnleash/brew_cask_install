import glob

print(glob.iglob('/Applications/**/*.app'))

# for filename in glob.iglob('/Applications/**/*.app'):
#     print(filename)
