import os
import xlsxwriter
import datetime


def generate_result_files(res):
    os.chdir("C:\My_Project_Repo\\nopecommerce\\testData")
    results_list = os.listdir()
    curr_date = str(datetime.date.today())
    workbook = xlsxwriter.Workbook("Results_" + curr_date + ".xlsx")
    worksheet = workbook.add_worksheet("Test_case_results")
    worksheet.set_column(0, 0, 50)
    worksheet.write(0, 0, "Test case Name", format= bold)
    worksheet.write(0, 1, "Result")
    row = 1
    col = 0
    for i, j in res:
        print(i)
        print(j)
        worksheet.write(row, col, i)
        worksheet.write(row, col + 1, j)
        row += 1
    workbook.close()


res = [("TestExecutionAutomation", "PASSED")]
generate_result_files(res)
