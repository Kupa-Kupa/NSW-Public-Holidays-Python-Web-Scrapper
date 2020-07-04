import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://www.nsw.gov.au/living-nsw/school-and-public-holidays")
bsObj = BeautifulSoup(html, "lxml")
table = bsObj.findAll("table", {"class":"nsw-table"})[1] #[1] means look for the second table with class "nsw-table"
rows = table.findAll('tr')
csvFile = open('NSW_Public_Holidays_Calender_Final.csv', 'w+',newline='')
writer = csv.writer(csvFile)
try:
    writer.writerow(('Subject','Start Date','Start Time','End Date','End Time','All Day Event','Description','Location','Private'))
    for row in rows[1:]: # this is saying to iterate over each row starting with the 2nd row (i.e. skip the first row)
        csvRow = []
        for cell in row.findAll(['td'])[:-1]: # this is saying look only for normal cell data (tagged 'td') and exclude the last column's data
            csvRow.append(cell.get_text())
        csvRow.append('')
        for cell in row.findAll(['td'])[1:-1]: # exclude the first and last column's data
            csvRow.append(cell.get_text())
        csvRow.append('')
        csvRow.append('TRUE')
        csvRow.append('')
        csvRow.append('')
        csvRow.append('TRUE')
        writer.writerow(csvRow)

    for row in rows[1:]: # this is saying to iterate over each row starting with the 2nd row (i.e. skip the first row)
        csvRow = []
        for cell in row.findAll(['td'])[::2]: # this is saying ignore the second cell
            csvRow.append(cell.get_text())
        csvRow.append('')
        for cell in row.findAll(['td'])[2:]: 
            csvRow.append(cell.get_text())
        csvRow.append('')
        csvRow.append('TRUE')
        csvRow.append('')
        csvRow.append('')
        csvRow.append('TRUE')
        writer.writerow(csvRow)

finally:
    csvFile.close()



csvText = open('NSW_Public_Holidays_Calender_Final.csv', "r")
try:
    csvText = ''.join([word for word in csvText]) \
        .replace('"Easter Saturday\n			(the Saturday following Good Friday)"', "Easter Saturday") \
        .replace("2Australia Day", "Australia Day") \
        .replace("1Bank Holiday", "Bank Holiday") \
        .replace("3Additional Day", "Observed Public Holiday") \
        .replace("Monday ", "") \
        .replace("Tuesday ", "") \
        .replace("Wednesday ", "") \
        .replace("Thursday ", "") \
        .replace("Friday ", "") \
        .replace("Saturday ", "") \
        .replace("Sunday ", "") \
        .replace(" January ", "/1/") \
        .replace(" February ", "/2/") \
        .replace(" March ", "/3/") \
        .replace(" April ", "/4/") \
        .replace(" May ", "/5/") \
        .replace(" June ", "/6/") \
        .replace(" July ", "/7/") \
        .replace(" August ", "/8/") \
        .replace(" September ", "/9/") \
        .replace(" October ", "/10/") \
        .replace(" November ", "/11/") \
        .replace(" December ", "/12/")
    finalFile = open('NSW_Public_Holidays_Calender_Final.csv', "w")
    finalFile.writelines(csvText)

finally:
    finalFile.close()
