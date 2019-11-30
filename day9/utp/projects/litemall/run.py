import unittest
import datetime,time
import os
import BeautifulReport as bf
from projects.litemall.const import case_path,report_path
from config.setting import email_template
from utils.send_message import send_mail,send_foxmail
def run():
    test_suite = unittest.defaultTestLoader.discover(case_path,'test_address.py')
    report = bf.BeautifulReport(test_suite)
    title = 'litemall_测试报告'
    filename = title + '_'  +datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.html'
    report.report(description=title,
                  filename=filename,
                  report_dir=report_path)
    email_content = email_template.format(pass_count=report.success_count,
                                          fail_count=report.failure_count,
                                          all_count=report.success_count+report.failure_count)
    

    report_abs_path = os.path.join(report_path,filename)
    #print(report_abs_path)
    #send_foxmail(title, email_content, report_abs_path)

run()