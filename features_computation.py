'''
This script extracts and computes the mean, standard deviation, variance and adds them as new columns.
'''

import csv
import  statistics as st

'''
This function takes reads the data, make the relevant computations and write to a new script.
@:param infile The file containing the data
@:param outfie The file to write to
@:desiredCols The columns in the data to use in computation
'''
def computeFeatures(infile, outfile, desiredCols):
    #open and close files using with_open synthax
    with open(outfile, 'wt', newline= '', encoding='utf-8') as outputfile, open(infile, 'rt', encoding='utf-8') as inputfile:
        oldData = csv.reader(inputfile)
        headers = []
        allColHeaders = oldData.__next__()
        headers.extend(allColHeaders)
        newCols = ["BallsMean", "BallsStd", "BallsVariance"]
        headers.extend(newCols)
        outputSCVFile = csv.writer(outputfile)

        #write column headers to make sense of output data
        outputSCVFile.writerow(headers)

        for row in oldData:
            unProcessedData = []
            for header in desiredCols:
                colIndex = allColHeaders.index(header)
                colVal = row[colIndex]
                unProcessedData.append(int(colVal))

	    #now addind mean, standard deviation ans variance
            row.insert(len(row), st.mean(unProcessedData))
            row.insert(len(row), st.stdev(unProcessedData))
            row.insert(len(row), st.variance(unProcessedData))

            # write to new row to file
            outputSCVFile.writerow(row)

            #end of function

targetCols = ["Ball1","Ball2","Ball3","Ball4","Ball5"]

computeFeatures("data/CleanedData.csv", "data/dataWithAddedFeatures.csv", targetCols)


