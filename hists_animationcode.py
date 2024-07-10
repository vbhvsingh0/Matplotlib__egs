%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000) + 7
x4 = np.random.uniform(14, 20, 10000)

# List of distributions and their names
dists = [x1, x2, x3, x4]
names = ['Normal', 'Gamma', 'Exponential', 'Uniform']

# Create figure and axes
fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharey = True)

    #plt.gca().set_ylabel('Frequency')
    #plt.gca().set_xlabel('Value')

def an_rand(curr)
    # If the current frame is the last frame, stop the animation
    if curr == 1000
        a.event_source.stop()

    for i in range(len(dists))
        axs[i  2, i % 2].cla()
        axs[i  2, i % 2].hist(dists[i][curr], density=True, bins=20, alpha=0.5)
        axs[i  2, i % 2].set_title(names[i],fontsize=14)
        axs[i  2, i % 2].set_ylim(0,0.5)
        fig.suptitle(f'Sampling with n = {curr} distributions', fontsize=16)
        if (i2 == 0 and i%2 == 0) or (i2 == 1 and i%2 == 0)
            axs[i  2, i % 2].set_ylabel('Frequency',fontsize=14)
        if (i2 == 1 and i%2 == 0) or (i2 == 1 and i%2 == 1)
             axs[i  2, i % 2].set_xlabel('Values',fontsize=14)
            
        # Annotate the plot
        #if i == 1
        #    axs[i  2, i % 2].annotate(f'n = {curr}', xy=(15, 0.15))

    plt.tight_layout()


# Create the animation
frames = range(100, 2001, 25)
a = animation.FuncAnimation(fig, an_rand, frames=frames, interval=100)
a.save('hists_animation.gif', writer='pillow')

# Display the plot
plt.show()
