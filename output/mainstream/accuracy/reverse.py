#310,conv2d_1/convolution,0.7956
import sys

csv_file = sys.argv[1]
new_file = sys.argv[2]
with open(new_file, "w+") as nf:
    with open(csv_file) as f:
        for line in f:
            vals = line.split(',')
            layers = int(vals[0])
            name = vals[1]
            acc = float(vals[2])
            new_layers = 314 - layers
            line =  str(new_layers) + "," + name + "," + str(acc) + "\n"
            nf.write(line)


