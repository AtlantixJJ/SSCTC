import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-file')
args = parser.parse_args()
img = plt.imread(args.file)
plt.imshow(img)
plt.show()
