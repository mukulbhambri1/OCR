import pdfplumber
import operator
import re
invoice = r"H 59248260.pdf"
from PyPDF2 import PdfFileReader
pdf = PdfFileReader(open(invoice,'rb'))
count = pdf.getNumPages()
print(count)
text=''
with pdfplumber.open(invoice) as pdf:
    for i in range(0,count):
        page = pdf.pages[i]
        text = text+page.extract_text()
        if i<count-1:
            text = text + "\n"
        else:
            continue
print(text)
temp_bill = ''
for row in text.split('\n'):
    if "Carl-Zeiss-Strasse" in row:
        temp_bill = "Eagle"
        break
    if "CMA" in row and "CGM" in row:
        temp_bill = "CMA"
        break
    if "jurisdiction" in row and "clause" in row:
        temp_bill = "Maersk"
        break
print(temp_bill)
bill="Bill Number: "
flag = 0
if temp_bill == "CMA":
    billno = re.search("[A-Z]{3}\d{7}",text)
elif temp_bill == "Maersk":
    billno = re.search("\d{9}",text)
elif temp_bill == "Eagle":
    billno = re.search("[A-Z]{7}\d{6}",text)
bill = bill + billno.group() + "\n"
print(bill)
flag = 0
det = "Shipper Address:" + "\n"
for row in text.split('\n'):
    if "Shipper" in row or "SHIPPER" in row:
        flag = 4
    elif  flag != 0:
        if "Export references Svc Contract" in row:
            continue
        det = det + row
        det = det + "\n"
        print(row)
        flag = flag - 1
        if flag == 0:
            break
det = det.replace("VOYAGE NUMBER",'')
det = det.replace(" SHIPPER",'SHIPPER ADDRESS:')
det = det.replace(" SHIPPER ADDRESS:",'')
det = det.replace(" WAYBILL NUMBER",'')
det = det.replace(" WAYBILL",'')
det = det.replace("NON NEGOTIABLE",'')
det = det.replace(" ***COPY NOT NEGOTIABLE*** EXPRESS RELEASE",'')
det = det.replace("Export references",'')
det = det.replace("Svc Contract",'')
det = det.replace(" F/Agent's Ref.",'')
det = det.replace("Consignee (If 'Order' state Notify Party and Address)",'')
det = det.replace(" \n",'')
det = re.sub(r'\s{1}\d{1}[A-Z]{2}\d{1}[A-Z]{2}\d{1}[A-Z]{2}', '', det)
det = re.sub(r'\s{1}[A-Z]{3}-{1}[A-Z]{3}-{1}\d{4}-{1}\d{4}', '', det)
det = re.sub(r'\s{1}\d{9}', '', det)
print(det)
new_det = det
new_det = new_det + "\n"
new_det = new_det.split('\n')
bill = [bill]
list1 = []
list1 = list1 + bill
list1 = list1 + new_det
mark = 0
for row in text.split('\n'):
    if "This contract is subject to the terms, conditions and exceptions, including the law & jurisdiction clause" in row:
        mark = 2
        print(mark)
mark2 = 0
for row in text.split('\n'):
    if "NON-NEGOTIABLE" in row:
        mark2 = 1

import pdfplumber
import pandas as pd
import pdfplumber
import tabula
temp = ''
for row in text.split('\n'):
    if "Carl-Zeiss-Strasse" in row:
        from PyPDF2 import PdfFileReader
        pdf = PdfFileReader(open(invoice,'rb'))
        count = pdf.getNumPages()
        if count == 3:
            temp = 'Eagle1'
        if count == 4 :
            temp = 'Eagle2'
    if "CMA" in row and "CGM" in row:
        temp = 'CMA'
    if "jurisdiction" in row and "clause" in row:
        from PyPDF2 import PdfFileReader
        pdf = PdfFileReader(open(invoice,'rb'))
        count = pdf.getNumPages()
        if count == 1:
            temp = 'Maersk1'
        if count == 2 :
            temp = 'Maersk2'
print(temp)
if temp == 'CMA':
    df = tabula.io.read_pdf_with_template(invoice,r"....json",guess = False, multiple_tables = True, stream=True)
    print(df)
if temp == 'Eagle1':
    df = tabula.io.read_pdf_with_template(invoice,r".....json",guess = False, multiple_tables = True, stream=True)
    print(df)
if temp == 'Eagle2':
    df = tabula.io.read_pdf_with_template(invoice,r".....json",guess = False, multiple_tables = True, stream=True)
    print(df)
if temp == 'Maersk1':
    df = tabula.io.read_pdf_with_template(invoice,r"......json",guess = False, multiple_tables = False, stream=True)
    print(df)
if temp == 'Maersk2':
    df = tabula.read_pdf_with_template(invoice,r"......json",guess = False, multiple_tables = True, stream=True)
    print(df)
length = len(df)
print(length)
import pandas as pd
df = [df]
listreal8 = pd.DataFrame(df)
pq=listreal8.to_string()
print(pq)
str9 = pq
if temp == 'CMA':
    string123 = "MARKS "
elif temp =="Maersk1" or temp =="Maersk2":
    string123 = ""
else:
    string123 = ""
line_items = []
for line in str9.split('\n'):
    try:
        s_no, *container1 = line.split()
        if "MARKS" in line.split():
            string123 = ""
        container1 = ' '.join(container1)
        print(container1)
        string123 = string123 + container1
        string123 = string123 + "\n"
    except ValueError:
        break
final_result_new = final_result_new.replace(np.nan, '')
final_result_new
final_result_new.to_excel('invoices_new.xlsx')
