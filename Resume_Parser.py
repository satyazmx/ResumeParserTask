import pandas as pd
import docx
import PyPDF2
import re
import os
from pyresparser import ResumeParser
path = "D:/TASKS/RESUME_PARSING/same-resume-year-wise-master/"
class SearchPattern():
    def __init__(self, src):
        self.src = src

    def find_emailid(self):
        pattern = re.findall("[a-zA-Z0-9_\.\*\-\+]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}", self.src)
        return pattern

    def find_githubid(self):
        pattern = re.findall("[github]+\.[com]+\/[a-zA-Z0-9]+", self.src)
        return pattern

    def find_linkedinid(self):
        pattern = re.findall("/linkedin\.[com]+\/[a-zA-Z0-9_\.\*\-\+]+", self.src)
        return pattern

    def find_skills(file):
        data = ResumeParser(file).get_extracted_data()
        print(data)

for root_folder, sub_folders, files in os.walk(path):
    email_id = []
    git_id = []
    linkedin_id = []
    skills_list = []
    df = pd.DataFrame({'resume_name': files})
    df.set_index('resume_name', inplace=True)
    for file in files:
        df = pd.DataFrame({'resume_name': files})
        df.set_index('resume_name', inplace=True)
        if file.split(".")[1] == "pdf":
            f = open("D:/TASKS/RESUME_PARSING/same-resume-year-wise-master/"+file, 'rb')
            read_pdf = PyPDF2.PdfFileReader(f)
            n = read_pdf.numPages
            for i in range(n):
                page_obj = read_pdf.getPage(i)
                text = page_obj.extractText()
                search_obj = SearchPattern(text)
                skills = search_obj.find_skills(file)
                skills_list.append(skills)
                email = search_obj.find_emailid()
                email_id.extend(email)
                github = search_obj.find_githubid()
                git_id.extend(github)
                linkedin = search_obj.find_linkedinid()
                linkedin_id.extend(linkedin)
        elif file.split(".")[1] == "docx":
            doc = docx.Document("D:/TASKS/RESUME_PARSING/same-resume-year-wise-master/"+file)
            for p in doc.paragraphs:
                text = p.text
                search_obj = SearchPattern(text)
                email = search_obj.find_emailid()
                email_id.extend(email)
                skills = search_obj.find_skills(file)
                skills_list.append(skills)
                github = search_obj.find_githubid()
                git_id.extend(github)
                linkedin = search_obj.find_linkedinid()
                linkedin_id.extend(linkedin)
    data = {'email_id':email_id, 'github_id':git_id, 'linkedin_id':linkedin_id,'skills':skills_list}
    df = pd.DataFrame(data)







