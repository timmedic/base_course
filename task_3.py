import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def Butterfly(t):
    x = np.sin(t) * (np.pow(np.e, np.cos(t)) - 2 * np.cos(4 * t) + np.pow(np.sin(t/12)))
    y = np.cos(t) * (np.pow(np.e, np.cos(t)) - 2 * np.cos(4 * t) + np.pow(np.sin(t/12)))
    return x, y

x, y = [], []

def Update(i):
    