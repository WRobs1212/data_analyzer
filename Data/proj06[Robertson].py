#Using Programming to Solve Problems CSIT-163-OL1-2026
#2/16/2026
#Project 6
#Wyatt Robertson




#allows the user to decide what file to mine in
FILE_NAME=input('What file would you like to open?\n')



import os

#opens the file, reads it all and assigns a variable to that value, then resets the file
opened = open(FILE_NAME)
pleaseWORK = opened.readlines()
opened.seek(0)
#name: get_data_list
#param: FILE_NAME <str> - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists <list>
def get_data_list(FILE_NAME):
#create and empty list to be modified later
#Iterate through the file, changing each entry so it can be put into the list

    empty = []
    for element in pleaseWORK :

        outside = opened.readline()
        inside = outside.split(',')


        list_in_list = empty.append(inside)
    return empty

#return the list to be further parsed
data_list = get_data_list(FILE_NAME)



#print(get_data_list())
#name: get_monthly_averages
#param: data_list <list> - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list <list>
def get_monthly_averages(data_list):
    #remove the header piece of data
    #create new lists for iteration and define what specifc data we're looking for
    data_list.pop(0)
    monthly_income_list = []
    monthly_volume_list = []
    specific_month_average = []
    date = data_list[0][0].split('/')
    year = date[2]
    month = date[0]
    combined = f"{month}-{year}"



    volume = data_list[0][5]
    adj_close = data_list[0][6]
    day_total = float(volume) * float(adj_close)









#Iterate on the list until there isnt any left.
#Check if the current month is the same as the future month. While it is add it to a list.
    while len(data_list) > 2 :
        if month == data_list[1][0].split('/')[0] :

            date = data_list[0][0].split('/')
            year = date[2]
            month = date[0]
            combined = f"{month}-{year}"
            volume = data_list[0][5]
            adj_close = data_list[0][6]
            day_total = float(volume) * float(adj_close)


            month_total = monthly_income_list.append(int(day_total))
            total_volume = monthly_volume_list.append(int(volume))
            data_list.pop(0)




            continue

        #If it is not, end the current entry and begin another one.
        if month != data_list[1][0].split('/')[0] :


            date = data_list[0][0].split('/')
            year = date[2]
            month = date[0]
            combined = f"{month}-{year}"
            volume = data_list[0][5]
            adj_close = data_list[0][6]
            day_total = float(volume) * float(adj_close)

            #Create a tuple of the month, year, and the calculated average for the month.

            month_total = monthly_income_list.append(int(day_total))
            total_volume = monthly_volume_list.append(int(volume))
            data_list.pop(0)
            month_average = sum(monthly_income_list) / sum(monthly_volume_list)
            Tupler = (combined , round(month_average , 2))
            month_average_list = specific_month_average.append(Tupler)




            monthly_income_list = []
            monthly_volume_list = []
            date = data_list[0][0].split('/')
            year = date[2]
            month = date[0]
            combined = f"{month}-{year}"
            continue







    return specific_month_average
monthly_average_list = get_monthly_averages(data_list)

#name: print_info
#param: monthly_average_list <list> - the list that you will process
#brief: print the top 6 and bottom 6 months for Google stock
#return: None
def print_info(monthly_average_list) :
    #Use an iterative variable to go through each entry (z)
    #Create a few empty lists to be modified later
    z = 0
    sorting_mechanism = []
    finale = []


    #iterate through one of the empty lists, adding each month's average
    for element in monthly_average_list :
        sorting_mechanism.append(monthly_average_list[z][1])
        z += 1
    sorting_mechanism.sort()
    #Sorts the new list from least to greatest
    low_baller = sorting_mechanism[0:6]
    #Take the first 6 items in the least (the smallest)
    x = 0
    a = -1
    while a < 100 :
        a += 1
        #search the normal list for the lowest values to get the associated month with them.
        if monthly_average_list[a][1] == low_baller[x] :
            finale.append(monthly_average_list[a])
            x += 1
            a = -1
            #stop when we have all 6
            if len(finale) == 6:
                break



#Same thing but in reverse. Take and find the highest value monthly averages and add them to a list.
    sorting_mechanism.reverse()
    high_roller = sorting_mechanism[0:6]
    x = 0
    a = -1
    while a < 100 :
        a += 1
        if monthly_average_list[a][1] == high_roller[x] :
            finale.append(monthly_average_list[a])
            x += 1
            a = -1
            if len(finale) == 12:
                break

#Fancy output statement with correct spacing
    output = f'6 Best Months:\n{finale[6]}\n{finale[7]}\n{finale[8]}\n{finale[9]}\n{finale[10]}\n{finale[11]}\n\n6 Worst Months:\n{finale[0]}\n{finale[1]}\n{finale[2]}\n{finale[3]}\n{finale[4]}\n{finale[5]}'
#Create a file, print in that file, close that file
    fileDescriptor = open('monthly_averages.txt','w')
    fileDescriptor.write(output)
    fileDescriptor.close()


    return
print_info(monthly_average_list)

opened.close()
#That's about it
# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the
# return in monthly_average_list

# call print_info function with the monthly_average_list from above
