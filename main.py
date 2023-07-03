"""
Date: 7th June 2023
Script to plot data sent by Fakhrul Bhuiyan from Merced Uni
"""

import pandas
import numpy
import matplotlib
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import csv

SMALL_SIZE = 13
MEDIUM_SIZE = 16
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of Athe tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title

# ###### Time vs Species Iron ######
#
# Dataset500K3GPaIron = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/1_Time vs species/500K_3GPa.txt', sep='\t')
# Dataset500K3GPaIron = Dataset500K3GPaIron.iloc[48:]
#
# Time = Dataset500K3GPaIron['Time(ps)'].tolist()
# Time  = [x - 0.095 for x in Time]
# TCP = Dataset500K3GPaIron['Mono'].tolist()
# Oligomer = Dataset500K3GPaIron['Oligo'].tolist()
# Cresol = Dataset500K3GPaIron['Cresol'].tolist()
# Toluene = Dataset500K3GPaIron['Toluene'].tolist()
#
# TimevsSpeciesPlot, TmvsSp = plt.subplots()
# #TmvsSp.set_title('Activation Energy vs Prefactor')
# TmvsSp.set_xlabel('Time (ns)')
# TmvsSp.set_ylabel('Number of Molecules')
# #TmvsSp.plot(Time, TCP, label='TCP')
# TmvsSp.plot(Time, Oligomer, label='Oligomer', color='black')
# TmvsSp.plot(Time, Cresol, label='Cresol', color='blue')
# TmvsSp.plot(Time, Toluene, label='Toluene', color='red')
# plt.grid(color='grey', linestyle='--', linewidth=0.5)
# plt.grid(which="minor", linestyle='--', linewidth=0.2)
# plt.minorticks_on()
# plt.tight_layout()
# TmvsSp.legend()
# TmvsSp.set_xlim(0, 1)
# TmvsSp.set_ylim(0, 50)
# plt.savefig('C:/Users/eeo21/Desktop/TCP Surface Chemistries Paper/SubFigures/Oligomer_Iron.png')
# plt.show()
#
# ###### Time vs Species  Iron Oxide ######
#
# Dataset500K3GPaIron = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/2_Iron oxide/1_Time vs species/500K_3GPa_Time vs chemical species plot data.txt', sep='\t')
# Dataset500K3GPaIron = Dataset500K3GPaIron.iloc[48:]
#
# Time = Dataset500K3GPaIron['Time(ps)'].tolist()
# Time  = [x - 0.095 for x in Time]
# TCP = Dataset500K3GPaIron['Mono'].tolist()
# Oligomer = Dataset500K3GPaIron['Oligo'].tolist()
# Cresol = Dataset500K3GPaIron['Cresol'].tolist()
# Toluene = Dataset500K3GPaIron['Toluene'].tolist()
#
# TimevsSpeciesPlot, TmvsSp = plt.subplots()
# #TmvsSp.set_title('Activation Energy vs Prefactor')
# TmvsSp.set_xlabel('Time (ns)')
# TmvsSp.set_ylabel('Number of Molecules')
# #TmvsSp.plot(Time, TCP, label='TCP')
# TmvsSp.plot(Time, Oligomer, label='Oligomer', color='black')
# TmvsSp.plot(Time, Cresol, label='Cresol', color='blue')
# TmvsSp.plot(Time, Toluene, label='Toluene', color='red')
# plt.grid(color='grey', linestyle='--', linewidth=0.5)
# plt.grid(which="minor", linestyle='--', linewidth=0.2)
# plt.minorticks_on()
# plt.tight_layout()
# TmvsSp.legend()
# TmvsSp.set_xlim(0, 1)
# TmvsSp.set_ylim(0, 50)
# plt.savefig('C:/Users/eeo21/Desktop/TCP Surface Chemistries Paper/SubFigures/Oligomer_IronOxide.png')
# plt.show()
#
# ###### Time vs Species Iron Carbide######
#
# Dataset500K3GPaIron = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/3_Iron carbide/1_Time vs species/500K_3GPa_Time vs chemical species plot data.txt', sep='\t')
# Dataset500K3GPaIron = Dataset500K3GPaIron.iloc[48:]
#
# Time = Dataset500K3GPaIron['Time(ps)'].tolist()
# Time  = [x - 0.095 for x in Time]
# TCP = Dataset500K3GPaIron['Mono'].tolist()
# Oligomer = Dataset500K3GPaIron['Oligo'].tolist()
# Cresol = Dataset500K3GPaIron['Cresol'].tolist()
# Toluene = Dataset500K3GPaIron['Toluene'].tolist()
#
# TimevsSpeciesPlot, TmvsSp = plt.subplots()
# #TmvsSp.set_title('Activation Energy vs Prefactor')
# TmvsSp.set_xlabel('Time (ns)')
# TmvsSp.set_ylabel('Number of Molecules')
# #TmvsSp.plot(Time, TCP, label='TCP')
# TmvsSp.plot(Time, Oligomer, label='Oligomer', color='black')
# TmvsSp.plot(Time, Cresol, label='Cresol', color='blue')
# TmvsSp.plot(Time, Toluene, label='Toluene', color='red')
# plt.grid(color='grey', linestyle='--', linewidth=0.5)
# plt.grid(which="minor", linestyle='--', linewidth=0.2)
# plt.minorticks_on()
# plt.tight_layout()
# TmvsSp.legend()
# TmvsSp.set_xlim(0, 1)
# TmvsSp.set_ylim(0, 50)
# plt.savefig('C:/Users/eeo21/Desktop/TCP Surface Chemistries Paper/SubFigures/Oligomer_IronCarbide.png')
# plt.show()
#
##### Number of P atoms chains #####

Surfaces = ['1_Iron', '2_Iron oxide', '3_Iron carbide']

Dataset500K3GPaIron_Patoms = pd.read_csv(f'F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/4_Patoms in polyphos. vs time/500K_3GPa_Total Patoms in polyphosphates.txt', sep='\t')

Time = Dataset500K3GPaIron_Patoms['time'].tolist()
Total = Dataset500K3GPaIron_Patoms['Total_Patoms_in_chain'].tolist()
Two = Dataset500K3GPaIron_Patoms['2'].tolist()
Three = Dataset500K3GPaIron_Patoms['3'].tolist()
Four = Dataset500K3GPaIron_Patoms['4'].tolist()
Five = Dataset500K3GPaIron_Patoms['5'].tolist()
Six = Dataset500K3GPaIron_Patoms['6'].tolist()
Seven = Dataset500K3GPaIron_Patoms['7'].tolist()
Eight = Dataset500K3GPaIron_Patoms['8'].tolist()

TimevsPatomsPlot, TmvsPa = plt.subplots()
#TmvsSp.set_title('Activation Energy vs Prefactor')
TmvsPa.set_xlabel('Time (ns)')
TmvsPa.set_ylabel('P atoms in Polyphosphate Chains')
TmvsPa.plot(Time, Total, label='Total')
TmvsPa.plot(Time, Two, label='2 Atoms', linestyle='--')
TmvsPa.plot(Time, Three, label='3 Atoms', linestyle='--')
TmvsPa.plot(Time, Four, label='4 Atoms', linestyle='--')
TmvsPa.plot(Time, Five, label='5 Atoms', linestyle='--')
TmvsPa.plot(Time, Six, label='6 Atoms', linestyle='--')
TmvsPa.plot(Time, Seven, label='7 Atoms', linestyle='--')
TmvsPa.plot(Time, Eight, label='8 Atoms', linestyle='--')
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.grid(which="minor", linestyle='--', linewidth=0.2)
plt.minorticks_on()
plt.tight_layout()
TmvsPa.legend(ncol=3, fontsize=12, loc='upper center')
TmvsPa.set_xlim(0, 1)
TmvsPa.set_ylim(0, 60)
plt.show()


#### Iron Oxide
Dataset500K3GPaIron_Patoms = pd.read_csv(f'F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/4_Patoms in polyphos. vs time/500K_3GPa_Total Patoms in polyphosphates.txt', sep='\t')

Time = Dataset500K3GPaIron_Patoms['time'].tolist()
Total = Dataset500K3GPaIron_Patoms['Total_Patoms_in_chain'].tolist()
Two = Dataset500K3GPaIron_Patoms['2'].tolist()
Three = Dataset500K3GPaIron_Patoms['3'].tolist()
Four = Dataset500K3GPaIron_Patoms['4'].tolist()
Five = Dataset500K3GPaIron_Patoms['5'].tolist()
Six = Dataset500K3GPaIron_Patoms['6'].tolist()
Seven = Dataset500K3GPaIron_Patoms['7'].tolist()
Eight = Dataset500K3GPaIron_Patoms['8'].tolist()

TimevsPatomsPlot, TmvsPa = plt.subplots()
#TmvsSp.set_title('Activation Energy vs Prefactor')
TmvsPa.set_xlabel('Time (ns)')
TmvsPa.set_ylabel('P atoms in Polyphosphate Chains')
TmvsPa.plot(Time, Total, label='Total')
TmvsPa.plot(Time, Two, label='2 Atoms', linestyle='--')
TmvsPa.plot(Time, Three, label='3 Atoms', linestyle='--')
TmvsPa.plot(Time, Four, label='4 Atoms', linestyle='--')
TmvsPa.plot(Time, Five, label='5 Atoms', linestyle='--')
TmvsPa.plot(Time, Six, label='6 Atoms', linestyle='--')
TmvsPa.plot(Time, Seven, label='7 Atoms', linestyle='--')
TmvsPa.plot(Time, Eight, label='8 Atoms', linestyle='--')
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.grid(which="minor", linestyle='--', linewidth=0.2)
plt.minorticks_on()
plt.tight_layout()
TmvsPa.legend(ncol=3, fontsize=12, loc='upper center')
TmvsPa.set_xlim(0, 1)
TmvsPa.set_ylim(0, 60)
plt.show()

#### Iron Carbide
Dataset500K3GPaIron_Patoms = pd.read_csv(f'F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/3_Iron carbide/4_Patoms in polyphos. vs time/500K_3GPa_Total Patoms in polyphosphates.txt', sep='\t')

Time = Dataset500K3GPaIron_Patoms['time'].tolist()
Total = Dataset500K3GPaIron_Patoms['Total_Patoms_in_chain'].tolist()
Two = Dataset500K3GPaIron_Patoms['2'].tolist()
Three = Dataset500K3GPaIron_Patoms['3'].tolist()
Four = Dataset500K3GPaIron_Patoms['4'].tolist()
Five = Dataset500K3GPaIron_Patoms['5'].tolist()
Six = Dataset500K3GPaIron_Patoms['6'].tolist()
Seven = Dataset500K3GPaIron_Patoms['7'].tolist()
Eight = Dataset500K3GPaIron_Patoms['8'].tolist()

TimevsPatomsPlot, TmvsPa = plt.subplots()
#TmvsSp.set_title('Activation Energy vs Prefactor')
TmvsPa.set_xlabel('Time (ns)')
TmvsPa.set_ylabel('P atoms in Polyphosphate Chains')
TmvsPa.plot(Time, Total, label='Total')
TmvsPa.plot(Time, Two, label='2 Atoms', linestyle='--')
TmvsPa.plot(Time, Three, label='3 Atoms', linestyle='--')
TmvsPa.plot(Time, Four, label='4 Atoms', linestyle='--')
TmvsPa.plot(Time, Five, label='5 Atoms', linestyle='--')
TmvsPa.plot(Time, Six, label='6 Atoms', linestyle='--')
TmvsPa.plot(Time, Seven, label='7 Atoms', linestyle='--')
TmvsPa.plot(Time, Eight, label='8 Atoms', linestyle='--')
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.grid(which="minor", linestyle='--', linewidth=0.2)
plt.minorticks_on()
plt.tight_layout()
TmvsPa.legend(ncol=3, fontsize=12, loc='upper center')
TmvsPa.set_xlim(0, 1)
TmvsPa.set_ylim(0, 60)
plt.show()


# ##### Average Chain Length Iron #####
#
# Pressures = ['2GPa', '3GPa', '4GPa', '5GPa']
#
# NewDataset = pd.DataFrame(columns=['Time 2GPa', 'Length 2GPa', 'Time 3GPa', 'Length 3GPa', 'Time 4GPa', 'Length 4GPa', 'Time 5GPa', 'Length 5GPa'])
#
# for P in Pressures:
#     DatasetIron_ChainLength = pd.read_csv(f'F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/7_avg chain length vs time/500K_{P}_Polyphosphate avg chain length vs time.txt', sep='\t')
#     for i in range(len(DatasetIron_ChainLength)):
#         x = DatasetIron_ChainLength.iloc[i]
#         item = x[0].split(' ')
#         item[0] = (float(item[0]) / 1000) - 0.102
#         if item[1] == '':
#             continue
#         else:
#             print(item)
#             NewDataset.loc[i, f'Time {P}'] = float(item[0])
#             NewDataset.loc[i, f'Length {P}'] = float(item[1])
#
# NewDataset = NewDataset.dropna()
#
# Time = NewDataset['Time 2GPa'].tolist()
# TwoGPa = NewDataset['Length 2GPa'].tolist()
# ThreeGPa = NewDataset['Length 3GPa'].tolist()
# FourGPa = NewDataset['Length 4GPa'].tolist()
# FiveGPa = NewDataset['Length 5GPa'].tolist()
#
# ChainLengthPlot, Chainplt = plt.subplots()
# #TmvsSp.set_title('Activation Energy vs Prefactor')
# Chainplt.plot(Time, TwoGPa, label='2GPa')
# Chainplt.plot(Time, ThreeGPa, label='3GPa')
# Chainplt.plot(Time, FourGPa, label='4GPa')
# Chainplt.plot(Time, FiveGPa, label='5GPa')
# Chainplt.set_xlabel('Time (ns)')
# Chainplt.set_ylabel('Average Chain Length (Angstrom)')
# plt.grid(color='grey', linestyle='--', linewidth=0.5)
# plt.grid(which="minor", linestyle='--', linewidth=0.2)
# plt.minorticks_on()
# plt.tight_layout()
# Chainplt.legend()
# Chainplt.set_xlim(0, 1)
# Chainplt.set_ylim(10, 20)
# plt.show()
