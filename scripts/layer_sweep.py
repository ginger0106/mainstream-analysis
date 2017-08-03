import pprint as pp
import sys
import matplotlib
import numpy as np

matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()

# CSV file needs to be of format
# layer1,camera_fps,transformer_fps,base_fps,task_fps
# layer2,camera_fps,transformer_fps,base_fps,task_fps

def op_to_layer(op_full):
    tensor_name = (op_full.split(":"))[0]
    layer = tensor_name.split("/")[0]
    return layer

def get_layers(csv_file):
    layers = []
    with open(csv_file) as f:
        for line in f:
            vals = line.split(',')
            op_full = vals[0]
            layer = op_to_layer(op_full)
            if layer not in layers:
                layers.append(layer)
    return layers

def get_num_NNs(csv_file):
    num_NNs = []
    with open(csv_file) as f:
        for line in f:
            vals = line.split(',')
            num_NN = int(vals[1])
            if num_NN not in num_NNs:
                num_NNs.append(num_NN)
    return num_NNs

def get_data(csv_file, experiment_name):
    data = {}
    with open(csv_file) as f:
        for line in f:
            vals = line.split(',')
            op_full = vals[0]
            layer = op_to_layer(op_full)
            num_NN = int(vals[1])
            base = float(vals[2])
            tasks = [float(i) for i in vals[3:]]
            task_avg = np.average(tasks)
            if num_NN not in data.keys():
                data[num_NN] = {}
            if layer not in data[num_NN].keys():
                data[num_NN][layer] = {"base": [], "task":[]}

            if experiment_name == "throughput":
                if len(tasks) == 0:
                    task_avg = base
                if base == 0:
                    base = task_avg

            data[num_NN][layer]["base"].append(base)
            data[num_NN][layer]["task"].append(task_avg)
    return data

def plot_throughput(csv_file, plot_dir):
    num_NNs = get_num_NNs(csv_file)
    data = get_data(csv_file, "throughput")
    layers = get_layers(csv_file)

    for i in range(2):              # Hack to get dimensions to match between 1st and 2nd graph
        for num_NN in num_NNs:
            xs = range(len(layers))

            base_fps = [np.average(data[num_NN][layer]["base"]) for layer in layers]
            base_errors = [np.std(data[num_NN][layer]["base"]) for layer in layers]
            task_fps = [np.average(data[num_NN][layer]["task"]) for layer in layers]
            task_errors = [np.std(data[num_NN][layer]["task"]) for layer in layers]
            plt.errorbar(xs, base_fps, yerr=base_errors, label="Base-"+str(num_NN))
            plt.errorbar(xs, task_fps, yerr=task_errors, label="Task-"+str(num_NN))

            # Format plot
            plt.xticks(xs, layers, rotation="vertical")
            plt.tick_params(axis='y', which='major', labelsize=28)
            plt.tick_params(axis='y', which='minor', labelsize=20)
            plt.ylabel("Throughput (FPS)", fontsize=28)
            plt.legend(loc=0, fontsize=15)
            plt.title(str(num_NN)+" split NN", fontsize=30)
            plt.tight_layout()
            plot_file = plot_dir + "/layer-sweep-throughput-"+str(num_NN)+"-NN.pdf"
            plt.savefig(plot_file)
            plt.clf()
    print plot_file

def plot_processor_latency(processors_file, plot_dir):
    layers = get_layers(processors_file)
    num_NNs = get_num_NNs(processors_file)
    data = get_data(processors_file, "latency-processors")
    width = 0.4
    for i in range(2):              # Hack to get dimensions to match between 1st and 2nd graph
        for num_NN in num_NNs:
            xs = range(len(layers))

            base_ms = [np.average(data[num_NN][layer]["base"]) for layer in layers]
            task_ms = [np.average(data[num_NN][layer]["task"]) for layer in layers]

            plt.bar(xs, base_ms, width, color = "seagreen", label="Base")
            plt.bar(xs, task_ms, width, bottom=base_ms, color = "dodgerblue", label="Task")

            plt.ylim(0,750)
            plt.xticks(xs, layers, rotation="vertical")
            plt.tick_params(axis='y', which='major', labelsize=28)
            plt.tick_params(axis='y', which='minor', labelsize=20)
            plt.legend(loc=0, fontsize=15, ncol=2)
            plt.ylabel("Processor Latency (ms)", fontsize=20)
            plt.title(str(num_NN) + " NNs", fontsize=30)
            plt.tight_layout()
            plot_file = plot_dir + "/layer-sweep-latency-" + str(num_NN) + "-NN.pdf"
            plt.savefig(plot_file)
            plt.clf()
    print plot_file


if __name__ == "__main__":
    cmd = sys.argv[1]
    plot_dir = sys.argv[2]
    csv_file = sys.argv[3]
    if cmd == "throughput":
        plot_throughput(csv_file, plot_dir)
    elif cmd == "latency":
        plot_processor_latency(csv_file, plot_dir)
    else:
        print "cmd must be in {throughput, latency}"

