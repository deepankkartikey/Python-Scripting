import spacy
import pdfminer
import re
import os
import pandas as pd

import pdf2txt

# load the language model
nlp = spacy.load("en_core_web_sm")

# dictionary to store important information from resume
result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []

# load the language model
nlp = spacy.load("en_core_web_sm")

# dictionary to store important information from resume
result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []

def convert_pdf_txt(file):
    """
    """
    output_filename = os.path.basename(os.path.splitext(file)[0]) + ".txt"
    output_filepath = os.path.join("output/txt", output_filename)
    # save output text file to specific location
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + " saved successfully!")
    return open(output_filepath).read()

def parse_resume(textfile):
    """
    """ 
    # define set of skills to be extracted from resume
    skillset = re.compile("javascript|java|python|sql|jenkins|git|agile")
    phone_regex = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})   ") # source for regex : https://stackoverflow.com/a/3868861
    # annotate resume textfile contents
    doc = nlp(textfile)
    name = [entity.text for entity in doc.ents if entity.label_ == "PERSON"][0]
    print(name)
    # using spacy's like_email attribute, extract email
    email = [word for word in doc if word.like_email == True][0]
    phone = str(re.findall(phone_regex, textfile.lower()))
    skills_list = re.findall(skillset, textfile.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Resume details extracted!")

for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print("Parsing ... " + file)
        txt = convert_pdf_txt(os.path.join('resumes/', file))
        parse_resume(txt)


result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills

result_df = pd.DataFrame(result_dict)
print(result_df)

result_df.to_csv('ouput/csv/parsed_resumes.csv')
