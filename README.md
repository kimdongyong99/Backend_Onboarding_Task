#  Backend_Onboarding_Task


#  개발 기간 
2025.03.15~2025.03.16

#  프로젝트 개요
Backend_Onboarding_Task는 Django를 활용하여 RESTful API를 개발하고, 배포 과정에서 필요한 모든 설정을 학습하기 위해 설계된 프로젝트입니다.

#  개발 환경
|Programming Language| python 3.10|
|:----------------:|:----------------:|
| Web Framework | Django 4.2|
| Database | SQLite|
| IDE | PyCharm|
| Version Control | Git, Github |
| Backend | Python, Django |
| Database | Django ORM, SQLite |
| HTTP Server | Gunicorn |
| Reverse Proxy | Nginx |

#  주요 기능
*회원가입 (Signup)*

사용자 정보를 받아 계정을 생성합니다.
비밀번호는 안전하게 해싱하여 저장합니다.

*로그인 (Login)*

사용자가 입력한 자격 증명을 통해 인증을 수행하고, JWT 토큰을 발급합니다.

*토큰 갱신 (Token Refresh)*

Refresh Token을 사용해 새로운 Access Token을 발급받을 수 있습니다.

*Swagger UI 통합*

API 명세서를 자동으로 생성하여 사용자 및 개발자가 쉽게 API를 테스트할 수 있도록 합니다.

#  기술적 의사결정
Django REST Framework :

Django REST Framework는 강력한 Serializer와 뷰셋을 통해 API 개발을 효율적으로 할 수 있어 선택하였습니다.

Swagger (drf-yasg) :

API 문서를 자동으로 생성하고 UI를 통해 테스트할 수 있어 개발 및 유지보수에 유리합니다.

Gunicorn & Nginx :

배포 과정에서 Gunicorn은 WSGI 서버로, Nginx는 정적 파일 제공과 보안 강화를 위해 사용하였습니다.

#  기능 테스트
*sign up:*
![image](https://github.com/user-attachments/assets/f8e7147f-1c03-41c7-bd32-d1c6b035c64e)

*log in:*
![image](https://github.com/user-attachments/assets/6c39937b-c9de-4ebf-8e8b-18d07508adb2)

*Refresh Token:*
![image](https://github.com/user-attachments/assets/ed07c628-fc93-4e95-b2c5-aec2180227e3)






#  배포 URL
http://43.201.27.232:8000/

