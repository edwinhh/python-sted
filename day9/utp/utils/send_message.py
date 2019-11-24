import yagmail
import traceback
from config.setting import email_info, email_cc, email_to, log


def send_mail(subject, content, files=None):
    try:
        smtp = yagmail.SMTP(**email_info)
        smtp.send(subject=subject, contents=content,
                  to=email_to, cc=email_cc, attachments=files)
    except Exception as e:
        log.error("发送邮件失败+%s" % traceback.format_exc())
