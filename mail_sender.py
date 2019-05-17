import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email.message import EmailMessage  #파이썬 메일 전송 모듈
from email.headerregistry import Address #파이썬 주소 리스트 모듈
from email.utils import make_msgid

############################## 메일 서버 로그인 블록 ###############################
smtp_sigong = smtplib.SMTP('SMTP_ADDRESS, 25)   # SMTP.xxx.com, port
smtp_sigong.ehlo()
smtp_sigong.login('E-MAIL','PASSWORD')  #E-MAIL = xxx@xxx.com
############################메일 형식 규정 블록#####################################
msg = EmailMessage()
msg['Subject'] = 'Hi nice to meet you'  # 제목
msg['From']='xxxx@xxx.xx'  # 보내는 사람
#받는 사람 목록
msg['To'] = (Address("TOM", "tom", "xxx.com"),
             Address("SAM", "sams", "xxx.com"))

# 기본 텍스트 메시지
msg.set_content("""\
Hello Every one
[1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718
""")

# html 버전.
asparagus_cid = make_msgid()
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Hey there</p>
    <p>
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
            click!
        </a>
    </p>
    <img src="cid:{asparagus_cid}" />
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

with open("roasted-asparagus.jpg", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                     cid=asparagus_cid)
############################# 첨부 파일 블록 ######################################
file ='./ex25_import.txt'       #파일 첨부 예제
fp = open(file, 'rb')
file_data = fp.read()
msg.add_attachment(file_data,maintype='text',subtype='plain',filename="ex25_import.txt")
############################## 메일 전송 #########################################
smtp_sigong.send_message(msg)
print('done!')
############################## 메일 전송 종료 #####################################
smtp_sigong.quit()
################################################################################
