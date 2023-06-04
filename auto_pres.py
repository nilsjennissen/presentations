#%% Packages
# Import libraries
import os
import glob
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing python pptx library
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

#%% Presentation
# Define the path to the powerpoint presentation
path = 'templates/template.pptx'

# Open the powerpoint presentation
prs = Presentation(path)

# Get summary details of the presentation
number_of_slides = len(prs.slides)
print('Number of slides: ', number_of_slides)

#%%
print(prs)