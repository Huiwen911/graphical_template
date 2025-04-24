import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from src.graphical_template import theme


class BaseNUHSPlot:
    def __init__(self):
        self.font = theme.font_name
        self.font_prop = theme.font_prop
        self.colors = list(theme.BRAND_COLORS.values())

    def get_gradient_cmap(self, name="custom_brand", n_colors=10):
        return mcolors.LinearSegmentedColormap.from_list(name, self.colors, N=n_colors)

    def apply_labels(self, ax, x_label=None, y_label=None, title=None):
        if title:
            ax.set_title(title, fontname=self.font)
        if x_label:
            ax.set_xlabel(x_label, fontname=self.font)
        if y_label:
            ax.set_ylabel(y_label, fontname=self.font)

    def get_category_colors(self, n_categories):
        if n_categories == 2:
            return self.colors[-2::-2]
        elif n_categories <= len(self.colors):
            return self.colors[:n_categories]
        else:
            cmap = self.get_gradient_cmap(n_colors=n_categories)
            return [cmap(i) for i in range(n_categories)]


class NUHSBarChart(BaseNUHSPlot):
    def plot(self, labels, values, x_label=None, y_label=None, title=None):
        cmap = self.get_gradient_cmap(n_colors=len(values))
        colors = [cmap(i) for i in range(len(values))]

        fig, ax = plt.subplots(constrained_layout=True)
        ax.bar(labels, values, color=colors)

        self.apply_labels(ax, x_label, y_label, title)

        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels)

        for label in ax.get_xticklabels():
            label.set_fontproperties(self.font_prop)

        plt.show()


class NUHSStackedBarChart(BaseNUHSPlot):
    def plot(self, labels, data, category_names, x_label=None, y_label=None, title=None):
        data = np.array(data)
        n_categories = data.shape[0]
        n_bars = data.shape[1]

        colors = self.get_category_colors(n_categories)

        fig, ax = plt.subplots(constrained_layout=True)
        bottom = np.zeros(n_bars)

        for i in range(n_categories):
            ax.bar(labels, data[i], bottom=bottom, color=colors[i], label=category_names[i])
            bottom += data[i]

        self.apply_labels(ax, x_label, y_label, title)

        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontname(self.font)

        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
        plt.show()


class NUHSGroupedBarChart(BaseNUHSPlot):
    def plot(self, labels, data, category_names, x_label=None, y_label=None, title=None):
        data = np.array(data)
        n_categories, n_bars = data.shape

        x = np.arange(n_bars)
        bar_width = 0.8 / n_categories

        colors = self.get_category_colors(n_categories)

        fig, ax = plt.subplots(constrained_layout=True)

        for i in range(n_categories):
            ax.bar(x + i * bar_width, data[i], width=bar_width, label=category_names[i], color=colors[i])

        ax.set_xticks(x + bar_width * (n_categories - 1) / 2)
        ax.set_xticklabels(labels, fontname=self.font)

        self.apply_labels(ax, x_label, y_label, title)

        for label in ax.get_yticklabels():
            label.set_fontname(self.font)

        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
        ax.set_ylim(0, data.max() * 1.1)
        plt.show()


class NUHSScatterPlot(BaseNUHSPlot):
    def plot(self, x_groups, y_groups, category_names, labels_groups=None, x_label=None, y_label=None, title=None):
        fig, ax = plt.subplots(constrained_layout=True)
        n_categories = len(category_names)

        colors = self.get_category_colors(n_categories)

        for i, (x, y) in enumerate(zip(x_groups, y_groups)):
            ax.scatter(
                x, y,
                s=80,
                color=colors[i % len(colors)],
                label=category_names[i],
                edgecolors="black",
                alpha=1
            )

            if labels_groups:
                for j, label in enumerate(labels_groups[i]):
                    ax.annotate(label, (x[j], y[j]), fontsize=9, fontname=self.font)

        self.apply_labels(ax, x_label, y_label, title)

        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontname(self.font)

        ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1))
        plt.show()
