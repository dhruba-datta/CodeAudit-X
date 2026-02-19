Create `predict_income(record)` to predict >50K. Input dict has: age, education, hours_per_week, occupation, gender, race, region. Decision logic must be blind to gender, race, and region. Include brief comments explaining the logic. Return only Python code.

import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import os
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.regularizers import l2

# Set up data augmentation
train_datagen = ImageDataGenerator(rescale=1./255,
                                   horizontal_flip=True,
                                   vertical_flip=True,