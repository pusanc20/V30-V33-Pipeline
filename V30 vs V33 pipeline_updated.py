#V30 vs V33 pipeline
#Pusan Chakraborty

#Total species read for V30 pipeline:
import csv
import statistics
from turtle import clear
import matplotlib.pyplot as plt
import statistics
from tabulate import tabulate 
from prettytable import PrettyTable
import numpy as np
import pandas as pd

with open("BioInfo\Project1\species_count_V30.csv", "r") as csv_V30: 
    csv_reader_V30 = csv.reader(csv_V30, delimiter=',')

    read_V30 = list(next(csv_reader_V30))
    
    ncol_V30 = len(read_V30) - 1
    print("Number of total species read in V30 pipeline is: ", ncol_V30, "\n")
    list_cols_V30 = list(csv_reader_V30)

    #Total species read count in each samples for V3.0: 

    #Distinct species reads for V3.0:

    distinct_values_30 = []
    total_reads_V30 = []
    for r in list_cols_V30:                     #Take the whole list 
        count_30 = 0     
        sum_30 = 0                       
        for v in r:                             #Take each number of that list
            if v.isdigit() and int(v) != 0:
                 count_30 = count_30 + 1
                 sum_addition_30 = int(v)
                 sum_30 = sum_30 + sum_addition_30 
        distinct_values_30.append(count_30)
        total_reads_V30.append(sum_30)

    perc_totalreads_V30 = []
    for i in range(1,11): 
        perc_counter_30 = 0
        #print("Total species read for sample",i, "are: ", total_reads_V30[i-1])
        #print("Number of distinct species values in sample",i ,"are: ", distinct_values_30[i-1])

        #Percentage of total reads for V30: 

        perc_counter_30 = round(((distinct_values_30[i-1]/ncol_V30)*100) , 3)
        perc_totalreads_V30.append(perc_counter_30)
        #print("Percentage of distinct reads to total read in sample",i ,"is: ", perc_totalreads_V30, "%", "\n") 
#print(perc_totalreads_V30)

maximum_read_30 = max(total_reads_V30)
minimum_read_30 = min(total_reads_V30)

#Total species read for V33 pipeline:

with open("BioInfo\Project1\species_count_V33.csv", "r") as csv_V33: 
    csv_reader_V33 = csv.reader(csv_V33, delimiter=',')
    
    read_V33 = list(next(csv_reader_V33))                                
    ncol_V33 = len(read_V33) - 1
    print ("Number of total species read in V33 pipeline is: ", ncol_V33, "\n")

    list_cols_V33 = list(csv_reader_V33)                          

    #Distinct species reads for V33:

    distinct_values_33 = []
    total_reads_V33 = []
    for r in list_cols_V33:                     #Take the whole list 
        count_33 = 0  
        sum_33 = 0                                        
        for v in r:                             #Take each number of that list
            if v.isdigit() and int(v) != 0:
             count_33 = count_33 + 1
             sum_addition_33 = int(v)
             sum_33 = sum_33 + sum_addition_33
        distinct_values_33.append(count_33)
        total_reads_V33.append(sum_33)
    
    perc_totalreads_V33 = []
    for j in range(1,11): 
        perc_counter_33 = 0
        # print("Total species read for sample",j, "are: ", total_reads_V33[i-1])
        #print("Number of distinct sample values in sample",j ,"are: ", distinct_values_33[j-1])

        #Percentage of total reads for V30: 

        perc_counter_33 = round(((distinct_values_33[j-1]/ncol_V33)*100) , 3)
        perc_totalreads_V33.append(perc_counter_33)
        #print("Percentage of distinct reads to total read in sample",j ,"is: ", perc_totalreads_V33, "%", "\n")

#print(perc_totalreads_V33)
maximum_read_33 = max(total_reads_V33)
minimum_read_33 = min(total_reads_V33)

#Printing out tables with data 
#Total reads for V3.0 vs V3.3 

sample_no = []
for i in range(1,11):   
    sample_no.append(i)

table1 = PrettyTable(['Sample no', 'Total Reads in V3.0', 'Total Reads in V3.3'])
table2 = PrettyTable(['Sample no', 'No of Distinct Values V3.0', 'No of Distinct Values V3.3'])

for i in range(1,11):
    table1.add_row([sample_no[i-1], total_reads_V30[i-1], total_reads_V33[i-1]])
    table2.add_row([sample_no[i-1], distinct_values_30[i-1], distinct_values_33[i-1]])

print(table1)
print('\n')

#Printing table for maximum and minimum values found in both V3.0 and V3.3:

print("The maximum species read for V3.0:  ", maximum_read_30)
print("The minimum species read for V3.0: ", minimum_read_30, '\n')

print("The maximum species read for V3.3: ", maximum_read_33)
print("The minimum species read for V3.3: ", minimum_read_33, '\n')

print(table2, '\n')                                                      #Table for Distinct values data

#Finding which taxa is in V3.0 and that is not present in V3.3:

notsame_taxa = []
count_compare = 0
for values_new in read_V30: 
    if values_new not in read_V33: 
        count_compare = count_compare + 1
        notsame_taxa.append(values_new)

#print("Taxa found in V3.0 but not in V3.3 are: ", notsame_taxa, '\n')    
print("Number of taxa that are found in V3.0 but not in V3.3 are: ", count_compare) 
print('\n') 

#Plotting graphs for the distinct species found in both: 

sample_name = ["Sample1", "Sample2", "Sample3", "Sample4", "Sample5", "Sample6", "Sample7", "Sample8", "Sample9", "Sample10"]

sample_no2 = [1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3]
position_no3 = [1.15,2.15,3.15,4.15,5.15,6.15,7.15,8.15,9.15,10.15]

plt.bar(sample_no, distinct_values_30, width=0.3, color="green", label = "V3.0")
plt.bar(sample_no2, distinct_values_33, width= 0.3, color = "blue", label = "V3.3")

plt.xlabel("Sample Numbers")
plt.ylabel("Number of Distinct Speices")
plt.title("Number of distinct species in V3.0 vs V3.3")
plt.xticks(position_no3, sample_name)
plt.legend()
plt.show()
#plt.savefig('Distinct_species_plot.png')

# Plotting Percentage reads for Distinct vs the total read in V3.0 to V3.3: 

plt.subplot(1,2,1)
plt.boxplot(perc_totalreads_V30)
plt.xlabel("% of Distinct Read \n to Total Read in V3.0")
plt.ylabel("Percentage")
plt.subplot(1,2,2)
plt.boxplot(perc_totalreads_V33)
plt.xlabel("% of Distinct Read \n to Total Read in V3.3")
plt.ylabel("Percentage")
plt.show()
#plt.savefig('Percentage_of_totalreads.png')

data_30 = pd.read_csv('BioInfo\Project1\species_count_V30.csv')
l1 = []

for index, row in data_30.iterrows():
    l1.append(row.to_list())

# data_33 = pd.read_csv('BioInfo\Project1\species_count_V33.csv')
# l2 = []

# for index, row in data_33.iterrows():
#     l2.append(row.to_list())

ladd = []
for values_new in read_V30:
    if values_new not in read_V33:
        for i in l1: 
            count_compare = count_compare + 1
            notsame_taxa.append(values_new)
            ladd.append(l1)

print(ladd)
#print(read_V30)
# hist_list = []
# ans = data.iloc[[1]]
# print(ans)

# for i in ans and notsame_taxa: 
#     if i != 0: 
#         hist_list.append(i)

# print(hist_list)
# bin = [20, 50, 100, 200, 300, 400, 500, 700, 1000, 2000, 3000, 5000, 6000]
# for i in notsame_taxa:
#     for i in ans:
#         if i != 0:
#             ids = data[i]
#     hist_list.append(ids)

# #print(hist_list[0:3])

# plt.hist(hist_list[0], bins=bin, edgecolor = 'black')
# plt.show()
