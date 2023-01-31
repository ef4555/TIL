# 문자메세지
# 메세지 서비스를 구축한다. 모델링을 구축해보자.
# 상속을 해서 만들자
# 공통 속성은 무엇일까
# sms 
# 1. 수신자, 발신자, 내용

class Sms:
    def __init__(self, receiver, sender, content):
        self.receiver = receiver
        self.sender = sender
        self.content = content
    
    def __str__(self):
        return f'SMS : 수신자{self.receiver}, 발신자{self.sender}, 내용{self.content}'

    def send(self):
        return f'SMS가 발송되었습니다.'


class Lms(Sms): # 자식 클래스 
    def __init__(self, receiver, sender, content):
        super().__init__(receiver, sender, content)

    def __str__(self): # 재정의
        return f'LMS : 수신자{self.receiver}, 발신자{self.sender}, 내용{self.content}'
    
    def send(self):
        return f'LMS가 발송되었습니다.'

m1 = Sms('01012345678', '9999999', '메세지 입니다.')
print(m1.send())

m2 = Lms('01012345678', '9999999', '장문메세지 입니다.')
print(m2.send())