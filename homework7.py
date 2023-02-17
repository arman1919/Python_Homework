#  Ստեղծել contacts.txt ֆայլ, ավելացնել հետևյալ
#  (First_Name Last_Name, Title, Extension, Email)
#  տեքստը՝ օգտագվելով Python-ի ֆայլային ֆունկցիոնալից։
#  Ստորև ուղարկում եմ pdf ֆայլ (Business_Proposal.pdf),
#  որի պարունակությունը կարդալով պետք է դուրս բերել AUTHORS:
#  դաշտը իր ենթատողերով և ավելացնել contacts.txt ֆայլում։
#  Վերջնական պատկերը պետք է լինի հետևյալը
#
#  First_Name Last_Name, Title, Extension, EmailAUTHORS:
#  Amy Baker, Finance Chair, x345, abaker@ourcompany.com
#  Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
#  Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com
#
# import fitz
#
# file1 = open("contacts.txt","w")
#
# file1.write("First_Name Last_Name, Title, Extension, Email")
#
# pdf_document = "./source/Business_Proposal.pdf "
# doc = fitz.open(pdf_document)
#
# page = doc.load_page(1)
#
# page_text = page.get_text("text")
#
# lines = page_text.split("\n")
#
# page_text = "\n" +"\n".join(lines[1:])
#
# file1.write(page_text)
#
# file1.close()
#
# file1 = open("contacts.txt","r")
#
# print(file1.read())

# Pdf ֆայլից (US_Declaration.pdf) դուրս բերել նահանգների և
# մարդկանց անունները և համապատասխանաբար պահել բառարանի մեջ (dict)։
# Georgia:
# Button Gwinnett, Lyman Hall, George Walton
# dict key -> Georgia:
# dict value -> [Button Gwinnett, Lyman Hall, George Walton]

import fitz

pdf_document = "./source/US_Declaration.pdf"

doc = fitz.open(pdf_document)
count = doc.page_count

text = ''
for i in range(3,count):

    page = doc.load_page(i)
    text += page.get_text()



lines = text.split("[Column 1]\n")

text = "\n".join(lines[1:])


text = text.replace("[Column 2]", "").replace("[Column 3]", "").replace("[Column 4]", "").replace("[Column 5]", "").replace("[Column 6]", "")



people_dict = {}
state_name = ''
for line in text.split('\n'):
    line = line.strip()
    if line.endswith(':'):
        state_name = line[:-1]
        people_dict[state_name] = []
    elif line != '':
        people_dict[state_name].append(line)

print(people_dict)
