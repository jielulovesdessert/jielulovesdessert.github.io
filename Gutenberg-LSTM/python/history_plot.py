# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 00:45:59 2018

@author: Jie Lu
"""

import pandas as pd
import matplotlib.pyplot as plt
import keras
#%matplotlib inline

df = pd.DataFrame(history.history)
df[['acc', 'val_acc']].plot()
plt.ylabel("accuracy")
df[['loss', 'val_loss']].plot(linestyle='--', ax=plt.twinx())
plt.ylabel("loss")

