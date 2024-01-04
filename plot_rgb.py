import matplotlib.pyplot as plt


def plot(height, width, colors, h, w):
    x = width
    y = height
    colors = colors

    aspect_ratio = w / h
    w = 6
    h = w / aspect_ratio

    # Plotting
    fig, ax1 = plt.subplots(figsize=(w, h))
    fig2, ax2 = plt.subplots(figsize=(w, h))
    fig3, ax3 = plt.subplots(figsize=(w, h))

    # Scatter plot with color mapped to values
    for i in range(len(x)):  # width horizontal
        for j in range(len(y)):  # height vertical
            for k in range(3):
                if colors[j][i][k] > 0.15:
                    if k == 0:
                        ax1.plot(x[i], y[j], marker='o', markersize=1, color=(colors[j][i][k], 0, 0), linestyle='none')
                    elif k == 1:
                        ax2.plot(x[i], y[j], marker='o', markersize=1, color=(0, colors[j][i][k], 0), linestyle='none')
                    else:
                        ax3.plot(x[i], y[j], marker='o', markersize=1, color=(0, 0, colors[j][i][k]), linestyle='none')

    for i in range(3):
        if i == 0:
            ax1.set_title('Red plot')
            ax1.set_xlabel('Width')
            ax1.set_ylabel('Height')
        elif i == 1:
            ax2.set_title('Green plot')
            ax2.set_xlabel('Width')
            ax2.set_ylabel('Height')
        else:
            ax3.set_title('Blue plot')
            ax3.set_xlabel('Width')
            ax3.set_ylabel('Height')

    plt.show()
