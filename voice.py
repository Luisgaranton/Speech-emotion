import pandas as pd
import numpy as np

import os
import sys


import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)

speech_auido = "C:\\Users\\luisg\\speech-emotion\\dataset\\"

speech_auido_directory_list = os.listdir(speech_auido)
file_emotion = []
file_statement = []
file_path = []
for dir in speech_auido_directory_list:
    # as their are 20 different actors in our previous directory we need to extract files for each actor.
    actor = os.listdir(speech_auido + dir)
    for file in actor:
        part = file.split('.')[0]
        part = part.split('-')
        # third part in each file represents the emotion associated to that auido.
        file_emotion.append(int(part[2]))
        file_statement.append(int(part[4]))
        file_path.append(speech_auido + dir + '/' + file)

        speech_auido_df = pd.DataFrame({"Emotions":file_emotion, "Statement":file_statement, "Path":file_path})

        speech_auido_df.Emotions.replace({1:'neutral', 2:'calm', 3:'happy', 4:'sad', 5:'angry', 6:'fear', 7:'disgust', 8:'surprise'}, inplace=True)
speech_auido_df.head()