# Author: Abdul Momen Usmani
# ID: 23685219
def main(csvfile, region):
    try:  
    # Answer 1
        with open(csvfile, 'r') as f:
            data = f.read()
        lines = data.split('\n')
    
        #keeping the header as a separate row
        header = lines[0].split(',')
        dataset = []
        #Refining the data using dictionaries and storing in dataset list declared right above
        for line in lines[1:]:
            row = line.split(',')
            if len(row) == len(header):
                dictionary = {}
                for i in range(len(header)):
                    dictionary[header[i]] = row[i]
                dataset.append(dictionary)

        # Filtered the entire datalist to include those rows with 'Net Change' that is positive
        dataWpositive_netchange = [tuples for tuples in dataset if float(tuples['Net Change']) > 0 and tuples['Regions'].lower() == region.lower()]
    
        # From the list above we try to extract the minimum and maximum of 'Population(2020)'    
        populations = [int(row['Population(2020)']) for row in dataWpositive_netchange]
    
        # Using Methods of List Comprehension to extract cells with conditions
        MinimumPopulation = next((tuples['Name'] for tuples in dataWpositive_netchange if int(tuples['Population(2020)']) == min(populations)), None)
        MaximumPopulation = next((tuples['Name'] for tuples in dataWpositive_netchange if int(tuples['Population(2020)']) == max(populations)), None)
    
    # Answer 2
    # In this step I am cleaning the dataset by removing zero and collecting those datasets related to the given region
    # dataWnonZero_Population = [tuples for tuples in dataset if int(tuples['Population(2020)']) > 0 and tuples['Regions'] == region]
        populationSum = 0;
        populationCount = 0;
        landareaSum = 0;
        landareaCount = 0;
        for rows in dataset:
            if int(rows['Population(2020)']) > 0 and rows['Regions'].lower() == region.lower():
                populationSum += int(rows['Population(2020)'])
                populationCount += 1
    # this if below is for answering correlation coffecient for Answer 3 so that I dont have to use this for loop again
            if float(rows['Land Area']) > 0 and rows['Regions'].lower() == region.lower():
                landareaSum += float(rows['Land Area'])
                landareaCount += 1
        population_mean = round(populationSum/populationCount,4)
        landarea_mean = round(landareaSum/landareaCount,4)
        stdDeviation_Numerator = sum((int(rows['Population(2020)']) - population_mean) ** 2 for rows in dataset if int(rows['Population(2020)']) > 0 and rows['Regions'].lower() == region.lower())
        population_std_deviation = round(( stdDeviation_Numerator/ (populationCount-1) ) ** 0.5,4)            
   
    # Answer 3
        countryDensity_list = [(row['Name'], round(float(row['Population(2020)'])/float(row['Land Area']), 4)) for row in dataset if row['Regions'].lower() == region.lower()]
        #Sorting according to Decreasing Population
        sortedcountryDensity_list = sorted(countryDensity_list, key=lambda row: row[1], reverse=True) 
  
    #Answer 4
    #constructing the correlation coefficient formula
        CorrNumerator1 = sum((int(rows['Population(2020)']) - population_mean) for rows in dataset if int(rows['Population(2020)']) > 0 and rows['Regions'] == region.lower())
        CorrNumerator2 = sum((float(rows['Land Area']) - landarea_mean) for rows in dataset if float(rows['Land Area']) > 0 and rows['Regions'].lower() == region.lower())         
        CorrDenominator1 = stdDeviation_Numerator
        CorrDenominator2 = sum((float(rows['Land Area']) - landarea_mean) ** 2 for rows in dataset if float(rows['Land Area']) > 0 and rows['Regions'].lower() == region.lower())
        CorrelationCoefficient = (CorrNumerator1*CorrNumerator2)/((CorrDenominator1*CorrDenominator2)**0.5)
        #CorrelationCoefficient Formula might be given wrong since I calculated using my calculator
        
        #Assigning Final Answers before returning
        MaxMin =[MaximumPopulation,MinimumPopulation]
        stdvAverage = [population_mean,population_std_deviation]
        density = sortedcountryDensity_list
        corr=CorrelationCoefficient
        return [MaxMin, stdvAverage, density, corr]
    
    except Exception as ex:
        exception_message = str(ex)
        #As Requirements say 'otherwise empty list and print an appropriate message'
        MaxMin =['Exception Details: '+exception_message]
        stdvAverage = ['Exception Details: '+exception_message]
        density = 'Exception Details: '+exception_message
        corr='Exception Details: '+exception_message
        return [MaxMin, stdvAverage, density, corr]
