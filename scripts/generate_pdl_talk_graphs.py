
import sys
sys.path.append("scripts")
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
assert mpl.__version__ < '2.0.0'
# mpl.style.use('classic')
import num_apps_bar
import layer_sweep
sys.path.append("scripts/scheduler")
import dynamic_scheduler
import scheduler
sys.path.append("scripts/goodness")
import accuracy_vs_layer
import false_neg_by_stride
import false_neg_by_layer
import false_pos_by_stride
sys.path.append("scripts/accuracy_vs_performance")
import accuracy_tradeoffs
sys.path.append("util")
import layer_latencies
import plot_util
sys.path.append('util/include')
import layers_info
sys.path.append('scripts/deploy')
import visualize
import fairness

import seaborn as sns
sns.set_style("whitegrid")

if __name__ == "__main__":

    # Task throughput by split point
    print "Plotting throughput by split point..."
    plot_dir = "plots/performance/throughput/inception/flow_control"
    csv_file = "output/streamer/throughput/inception/flow_control/multi-app"
    layer_sweep.plot_throughput(csv_file, plot_dir)

    # Accuracy vs layer
    fi = "output/mainstream/accuracy/flowers/inception/flowers-40-0.0001-dropout"
    fr = "output/mainstream/accuracy/flowers/resnet/flowers-40-0.0001-chokepoints"
    fm = "output/mainstream/accuracy/flowers/mobilenets/flowers-40-0.0001"

    accuracy_files = [fr]
    labels = [
              "Flowers-ResNet50"
              ]
    plot_file = "plots/accuracy/accuracy-by-layer-flowers-1.pdf"
    accuracy_vs_layer.plot_accuracy_vs_layer(accuracy_files, labels, plot_file)

    accuracy_files = [fr, fi, fm]
    labels = [
              "Flowers-ResNet50",
              "Flowers-InceptionV3",
              "Flowers-MobileNets-224",
              ]
    plot_file = "plots/accuracy/accuracy-by-layer-flowers-2.pdf"
    accuracy_vs_layer.plot_accuracy_vs_layer(accuracy_files, labels, plot_file)

    # Accuracy trade-offs
    mpl.rc('font', **{'sans-serif' : 'Arial',
                      'family' : 'sans-serif'})
    arch1 = "iv3"
    arch2 = "r50"
    arch3 = "mnets"

    latency_file1 = "output/streamer/latency/inception/basic/latency-processors-iv3.csv"
    latency_file2 = "output/streamer/latency/resnet/basic/latency-processors-r50.csv"
    latency_file3 = "output/streamer/latency/mobilenets/basic/latency.csv"

    accuracy_file1 = "output/mainstream/accuracy/flowers/inception/flowers-40-0.0001-dropout"
    accuracy_file2 = "output/mainstream/accuracy/flowers/resnet/flowers-40-0.0001-chokepoints"
    accuracy_file3 = "output/mainstream/accuracy/flowers/mobilenets/flowers-40-0.0001"

    arches = [arch1, arch2, arch3]
    latency_files = [latency_file1, latency_file2, latency_file3]
    accuracy_files = [accuracy_file1, accuracy_file2, accuracy_file3]
    labels = ["InceptionV3", "ResNet50", "MobileNets-224"]

    plot_dir = "plots/tradeoffs/flowers"

    accuracy_tradeoffs.plot_accuracy_vs_fps_partial(arches, latency_files, accuracy_files, labels, plot_dir, "2")

    arches = [arch1]
    latency_files = [latency_file1]
    accuracy_files = [accuracy_file1]
    labels = ["InceptionV3"]

    accuracy_tradeoffs.plot_accuracy_vs_fps_partial(arches, latency_files, accuracy_files, labels, plot_dir, "1")

    ms1 = "output/streamer/scheduler/v1/scheduler-v1-500-c0.1664-mainstream"
    max1 = "output/streamer/scheduler/v1/scheduler-v1-500-c0.1664-maxsharing"
    min1 = "output/streamer/scheduler/v1/scheduler-v1-500-c0.1664-nosharing"
    f1 ="scheduler-500-c0.1664-ll2"
    t1 = ""
    plot_dir = "plots/scheduler/v1/"

    ms_files = [ms1]
    max_files = [max1]
    min_files = [min1]
    f_files = [f1]
    f_files_annotated = [f + "-annotated" for f in f_files]
    titles = [t1]

    scheduler.plot_recall(ms_files, max_files, min_files, f_files, titles, plot_dir, False, 1)
    scheduler.plot_precision(ms_files, max_files, min_files, f_files, titles, plot_dir)
    scheduler.plot_f1(ms_files, max_files, min_files, f_files, titles, plot_dir)
