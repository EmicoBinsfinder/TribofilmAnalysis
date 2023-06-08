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

# ###### Time vs Species ######
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
# ##### Number of P atoms chains #####
# Dataset500K3GPaIron_Patoms = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/4_Patoms in polyphos. vs time/500K_3GPa_Total Patoms in polyphosphates.txt', sep='\t')
#
# Time = Dataset500K3GPaIron_Patoms['time'].tolist()
# Total = Dataset500K3GPaIron_Patoms['Total_Patoms_in_chain'].tolist()
# Two = Dataset500K3GPaIron_Patoms['2'].tolist()
# Three = Dataset500K3GPaIron_Patoms['3'].tolist()
# Four = Dataset500K3GPaIron_Patoms['4'].tolist()
# Five = Dataset500K3GPaIron_Patoms['5'].tolist()
# Six = Dataset500K3GPaIron_Patoms['6'].tolist()
# Seven = Dataset500K3GPaIron_Patoms['7'].tolist()
# Eight = Dataset500K3GPaIron_Patoms['8'].tolist()
#
# TimevsPatomsPlot, TmvsPa = plt.subplots()
# #TmvsSp.set_title('Activation Energy vs Prefactor')
# TmvsPa.set_xlabel('Time (ns)')
# TmvsPa.set_ylabel('Phosphorous Atoms within Polyphosphate Chains')
# TmvsPa.plot(Time, Total, label='Total')
# TmvsPa.plot(Time, Two, label='2-Atom Chain')
# TmvsPa.plot(Time, Three, label='3-Atom Chain')
# TmvsPa.plot(Time, Four, label='4-Atom Chain')
# TmvsPa.plot(Time, Five, label='5-Atom Chain')
# TmvsPa.plot(Time, Six, label='6-Atom Chain')
# TmvsPa.plot(Time, Seven, label='7-Atom Chain')
# TmvsPa.plot(Time, Eight, label='8-Atom Chain')
# plt.grid(color='grey', linestyle='--', linewidth=0.5)
# plt.grid(which="minor", linestyle='--', linewidth=0.2)
# plt.minorticks_on()
# plt.tight_layout()
# TmvsPa.legend()
# TmvsPa.set_xlim(0, 1)
# TmvsPa.set_ylim(0, 50)
# plt.show()

##### Average Chain Lengths #####
Dataset500K2GPaIron_ChainLength = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/7_avg chain length vs time/500K_2GPa_Polyphosphate avg chain length vs time.txt', sep='\t')
Dataset500K3GPaIron_ChainLength = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/7_avg chain length vs time/500K_3GPa_Polyphosphate avg chain length vs time.txt')
Dataset500K4GPaIron_ChainLength = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/7_avg chain length vs time/500K_4GPa_Polyphosphate avg chain length vs time.txt', sep='\t')
Dataset500K5GPaIron_ChainLength = pd.read_csv('F:/PhD/TCPDecompositionExperiments/Fakhrul_raw_data_files/1_Iron/7_avg chain length vs time/500K_5GPa_Polyphosphate avg chain length vs time.txt', sep='\t')

print(Dataset500K3GPaIron_ChainLength)

NewDataset = pd.DataFrame(columns=['time', 'length'])
for i in range(len(Dataset500K2GPaIron_ChainLength)):
    Dataset500K2GPaIron_ChainLength[]