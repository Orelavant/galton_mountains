"""
Mountain Demonstration with matplotlib: Creating a 'mountain' using a
Galton board: https://en.wikipedia.org/wiki/Bean_machine. Formula
and inspiration: https://www.mathsisfun.com/data/quincunx-explained.html
Author: Jacob Valero
Date: 09/15/21
"""
import matplotlib.pyplot as plt
import math as math
import numpy as np
import random as rand


def main():
    # "Run" Galton board with randomization
    # Random Modifiers and whether to save fig / show it
    total_bins = rand.randrange(10, 21)
    balls = rand.randrange(0, 101)
    start = rand.randrange(3, 6)
    end = rand.randrange(6, 8)
    n_samples = rand.randrange(10, 21)
    probabilities = np.linspace(start, end, n_samples)
    save = False
    show = True

    # Get samples
    total_arr = []
    for i in range(len(probabilities)):
        balls_bin_arr = galton_board(balls, total_bins, probabilities[i]/10)
        total_arr.append(balls_bin_arr)

    # Plot the results to create various 'mountains'
    for balls_bin_arr in total_arr:
        plt.plot(range(total_bins), balls_bin_arr, color='black')
        plt.fill_between(range(total_bins), balls_bin_arr)
    plt.xlabel("Bins")
    plt.xticks(range(total_bins))
    plt.ylabel("Number of Balls")
    plt.title("Galton Mountain")
    if save:
        plt.savefig('figures/' + str(rand.randrange(0, 999)) + "example")
    if show:
        plt.show()


def bin_prob(bin_k, total_bins, l_r_prob):
    """
    bin_k (int): one bin
    total_bins (int): total number of bins
    l_r_prob (float): probability of ball going left or right on a
    galton board peg between 0 and 1
    :return: The probability that a ball will fall into that bin
    """
    # total bins choose bin_k
    n_c_k = math.factorial(total_bins) / (math.factorial(bin_k) *
                                          math.factorial(total_bins - bin_k))

    # Binomial Distribution formula
    return n_c_k * l_r_prob**bin_k * (1-l_r_prob)**(total_bins-bin_k)


def galton_board(balls, total_bins, l_r_prob):
    """
    balls (int): number of balls to use
    total_bins (int): total number of bins
    l_r_prob (float): probability of ball going left or right on a
    galton board peg between 0 and 1
    :return: array of the number of balls that landed in each bin
    """
    # Calculate the probability for each bin
    bin_prob_arr = []
    for bin_k in range(total_bins):
        bin_prob_arr.append(bin_prob(bin_k, total_bins, l_r_prob))

    # Calculate the number of balls that will probably land in each bin
    balls_bin_arr = []
    for i in range(total_bins):
        n_balls = round(balls * bin_prob_arr[i])
        balls_bin_arr.append(n_balls)

    return balls_bin_arr


if __name__ == "__main__" :
    main()