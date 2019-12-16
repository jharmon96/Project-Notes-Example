import csv
import time
import settings
import standard_functions
from selenium import webdriver
from pathlib import Path


def run():

    read_import()

    pass


# return key of project
def read_import():

    input_file = csv.DictReader(open(settings.notes_file, encoding="utf-8-sig"))
    projects_file = csv.DictReader(open(settings.projects_file, encoding="utf-8-sig"))

    project_key =""

    for row in input_file:
        input_project_org_code = str(row["project_org_code"])
        input_project_code = str(row["project_code"])
        input_note_title = str(row["note_title"])
        input_note_description = str(row["note_description"])
        input_note_type = str(row["note_type"])
        input_note_status = str(row["note_status"])
        input_due_date = str(row["due_date"])
        input_file_path = str(row["file_path"])
        input_udf_08 = str(row["csm_engagement"])

        print(input_project_org_code)
        print(input_project_code)

        for row in projects_file:
            db_project_org_code = str(row["proj_org_code"])
            db_project_code = str(row["proj_code"])
            db_project_key = str(row["proj_key"])

            print("1")

            if input_project_code == db_project_code and input_project_org_code == db_project_org_code:
                project_key = db_project_key

                URL = settings.URL + "/action/projects/note?projectkey=" + project_key
                settings.driver.get(URL)

                settings.driver.find_element_by_link_text("Project Note").click()
                settings.driver.find_element_by_name("title").send_keys(input_note_title)
                settings.driver.find_element_by_name("notetext").send_keys(input_note_description)
                settings.driver.find_element_by_name("notetypekey").send_keys(input_note_type)
                settings.driver.find_element_by_name("notestatuskey").send_keys(input_note_status)
                #settings.driver.find_element_by_name("actiondate").send_keys(input_due_date)
                settings.driver.find_element_by_name("attachment").send_keys(input_file_path)
                settings.driver.find_element_by_name("udf_8").send_keys(input_udf_08)
                settings.driver.find_element_by_name("button_save").click()

                #time.sleep(10)


