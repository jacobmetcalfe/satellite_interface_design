import csv

sat_nums = []
sat_launches = []
sat_desigs = []
sat_funcs = []
sat_statuses = []
sat_remarks = []

with open('Satellites.csv') as satFile:
    reader = csv.reader(satFile)
    for row in reader:
        sat_nums.append(row[0])
        sat_launches.append(row[1])
        sat_desigs.append(row[2])
        sat_funcs.append(row[3])
        sat_statuses.append(row[4])
        sat_remarks.append(row[5] + ' ' + row[6])
print('----------------------------------------------------------------------------')
typeOfSearch = input('\t\t\t\t  What do you want to search by?\n'
                     '[SATELLITE NUMBER][LAUNCH DATE][OTHER DESIGNATIONS][FUNCTION][STATUS]\n' +
                     '----------------------------------------------------------------------------\n')

search_topics = ['SATELLITE NUMBER', 'LAUNCH DATE', 'OTHER DESIGNATIONS', 'FUNCTION', 'STATUS']
if typeOfSearch.lower() == search_topics:
    print(typeOfSearch)

search = input(str('Sat Capability: '))
statusIndexes = [status for status in range(len(sat_statuses)) if sat_statuses[status].lower() == search.lower()]
for index in statusIndexes:
    print(sat_nums[index] + ': ' + sat_desigs[index] + ', ' + sat_remarks[index])
exit(0)
