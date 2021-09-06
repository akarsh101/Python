# Reading an excel file using Python
import xlrd
i=1
n=1
# Give the location of the file
loc = ("E:\Downloads\Telegram Desktop\Wipro.xls")
 
workbook = xlrd.open_workbook(loc)
sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for row in range(sheet.nrows):
    x= sheet.cell_value(row,2)#counting of second row containging the Event which is TalentNxt or OnCampus
    x2= sheet.cell_value(row,0)#counting of 0th row the mail ids with klh.edu.in or gmail.com
    string2="klh.edu.in"
    c=str(x)
    A="Elite TalentNxt"
    B="Elite OnCampus"
    string=x2.split('@')
    mail=string[1:]
    listToStr = ' '.join([str(elem) for elem in mail])
    if c==A and listToStr == "klh.edu.in":
        i=i+1
    if c==B and listToStr == "klh.edu.in":
        n=n+1
print("Total no of students who got selected for TalentNxt from KL Hyderabad campus are:",i)
print("Total no of students who got selected for OnCampus from KL Hyderabad campus are:",n)
print("Total no of students from KLH are:",i+n)        
