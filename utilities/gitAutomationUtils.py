import os
import configparser
import xlsxwriter
import datetime

ini_file = os.path.abspath(os.path.dirname(".\\..\configurations\."))
config = configparser.RawConfigParser()
config.read(ini_file + "\\config.ini")
updated_repo_path = config.get('common info', 'updated_repo_path')
testCases_path = config.get('common info', 'testCases_path')
testData_path = config.get('common info', 'testData_path')
git_branch = config.get('common info', 'git_branch')


class TestExecutionAutomation:
    @staticmethod
    def setup():
        print("******************** TEST EXECUTION STARTED ********************")

    @staticmethod
    def teardown():
        print("******************** TEST EXECUTION COMPLETED ********************")

    @staticmethod
    def git_command(git_repo_command):
        print("******************** GIT COMMAND EXECUTION STARTED ********************")
        os.chdir(updated_repo_path)
        repo_path = os.getcwd()
        print(repo_path)
        os.system(command=git_repo_command)
        print("******************** GIT COMMAND EXECUTION COMPLETED ********************")

    @staticmethod
    def files_update():
        files = []
        os.chdir(updated_repo_path)
        folders = os.listdir()
        if "testCases" in folders:
            os.chdir(testCases_path)
            print("-I- Current Directory Selected is :{}".format(os.getcwd()))
            files = os.listdir()
            if len(files) != 0:
                print("******************** ALL FILES LOADED SUCCESSFULLY ********************")
        else:
            print("-I- Couldn't find any directory called 'TestCases'")
        return files

    @staticmethod
    def test_case_execution(file_name):
        os.chdir(updated_repo_path)
        folders = os.listdir()
        if "testCases" in folders:
            os.chdir(testCases_path)
            if file_name in os.listdir():
                os.system(command=file_name)
            else:
                print("The file is not available in this directory")
        else:
            print("-I- Couldn't find any directory called 'TestCases'")

    @staticmethod
    def generate_result_files(res):
        os.chdir(testData_path)
        results_list = os.listdir()
        curr_date = str(datetime.date.today())
        workbook = xlsxwriter.Workbook("Results_" + curr_date + ".xlsx")
        worksheet = workbook.add_worksheet("Test_case_results")
        worksheet.set_column(0, 0, 50)
        bold = workbook.add_format({'bold': True})
        worksheet.write(0, 0, "Test case Name", bold)
        worksheet.write(0, 1, "Result", bold)
        row = 1
        col = 0
        for i, j in res:
            worksheet.write(row, col, i)
            worksheet.write(row, col + 1, j)
            row += 1
        workbook.close()
