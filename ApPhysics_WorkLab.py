import pandas as pd
import numpy as np

#total distance measured in mm
distance_data = np.array([515,535,555,575,625,665,695,775])

#to calculate by subtracting values of distance_data from eachother
#delta_distance = np.zeros([0,1]))

#measure kg (found by F/g = m, but convert this is N later on)
cal_mass = np.array([0,.530,.815,1.08,1.77,2.315, 2.730, 3.835])

og_dataValuesDict = {
    "Total Distance" : distance_data,
    "Calculated Mass" : cal_mass
}
og_dataValues = pd.DataFrame(og_dataValuesDict)

print(og_dataValuesDict)