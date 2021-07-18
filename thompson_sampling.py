# Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
import random

ads_selected = []
numbers_of_rewards_1 = [0] * 10
numbers_of_rewards_0 = [0] * 10
total_reward = 0
for n in range(0, 10000):
    ad = 0
    max_random = 0
    for i in range(0, 10):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i   #selecting ad with highest probability of success....chooses ad whic has more alpha beta ratio.if the ad we choose is correct and selected by user reward will be 1 and will get added to number of rewards_1
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward

# Visualising the results - Histogram
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
#in code we dont know about the answer so we predict which ad user will select by looking at alpha beta value and then cross check with excel sheet if we r correct we get reward=1 else 0