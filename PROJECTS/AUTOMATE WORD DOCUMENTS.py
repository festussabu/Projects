from docxtpl import DocxTemplate
from  datetime import datetime
import pandas as pd



doc = DocxTemplate("en-template-manager-info.docx")

my_name = "Festus"
my_phone = '956-298-2082'
my_email = 'festus.hoopa@gamil.com'
my_address = "Amballoor P.O"
today_date =datetime.today().strftime("%d %b, %Y")


my_context = {"my_name" : my_name, "my_phone" : my_phone, "my_email" : my_email, "my_address" : my_address,
           "today_date" : today_date}


data_frame = pd.read_csv("Untitled 1.csv")



for index, row in data_frame.iterrows():
    context = {"hiring_manager_name": row["name"],
               "address": row["address"],
               "phone_number": row["phone_number"],
               "email": row["email"],
               "job_position": row["job"],
               "company_name" : row["company"]}


    context.update(my_context)


    doc.render(context)
    doc.save(f"generate_doc {index}.docx")


