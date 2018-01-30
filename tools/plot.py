import matplotlib.pyplot as plt


def plot(data, path, legend='', xlabel='', ylabel=''):
    if len(data[[0]]) == 0:
        return
    plt.rc('font', family='Times New Roman', size=8)
    plt.rc('lines', linewidth=0.4)
    fig, ax = plt.subplots(figsize=(2.756, 1.703))
    fig.subplots_adjust(right=0.96, top=1, bottom=0.16, left=0.16)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.8)
    ax.spines['left'].set_linewidth(0.8)
    ax.tick_params(direction='in')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    line_style_list = ['-', '-.', ':', '--']
    color_list = ['r', 'b', 'm', 'g']
    x_axis = range(len(data[[0]]))
    for i in range(len(data.columns)):
        ax.plot(x_axis, data[[i]], color=color_list[i], linestyle=line_style_list[i], label=legend)
    ax.legend()
    interval = (len(data[[0]]) - 1) / 4
    xtick_list = x_axis[0::interval]
    xtick_label_list = data.index[0::interval]
    ax.set_xticks(xtick_list)
    ax.set_xticklabels(map(lambda x: x[:7], xtick_label_list))
    plt.savefig(path, dpi=200)
    plt.close()
