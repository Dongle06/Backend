# Backend

## Directory Structure

```
├── README.md                                          - 리드미 파일
│
│
├── Backend/                                           - 백엔드 장고 디렉토리
│   ├── docker-compose.prod.yml                        - docker-compose 개발용 파일
│   ├── docker-compose.yml                             - docker-compose 배포용 파일
│   ├── Dockerfile                                     - 백엔드 배포용 도커 파일
│   ├── Dockerfile.prod                                - 백엔드 개발용 도커 파일
│   ├── .gitignore                                     - gitignore 파일
│   ├── config/                                        
│   │    ├── nginx/                                    
│   │    │    ├── Dockerfile                           - nginx docker file
│   │    │    └── nginx.conf                           - nginx configuration
│   │    ├── scripts/                                  
│   │    │    └── deploy.sh                            - 도커 로컬 환경 세팅
│   │    └── entrypoint.sh                             
│   ├── manage.py                                      - django 명령어 인터페이스
│   ├── requirements.txt                               - 실행에 필요한 모듈들 정의
│   ├── Backend/                                              
│   │    ├── __pycache__                               
│   │    ├── __init__.py                               - 폴더가 패키지로 인식되게 함
│   │    ├── asgi.py                                   - 배포를 위한 인터페이스
│   │    ├── settings.py                               - 개발환경 세팅
│   │    ├── urls.py                                   - url 매핑
│   │    └── wsgi.py                                   - 배포를 위한 인터페이스
│   ├── accounts/                                              
│   │    ├── __pycache__                               
│   │    ├── migrations                                - 테이블 생성
│   │    ├── templates                                 - 화면 정의
│   │    ├── __init.py                                 - 폴더가 패키지로 인식되게 함
│   │    ├── admin.py                                  - 관리자가 쓸 정보 기입
│   │    ├── apps.py                                   - 응용 프로그램 구성 포함
│   │    ├── models.py                                 - user 데이터 스키마 정의
│   │    ├── serializers.py                            - 데이터 반환 형태 정의
│   │    ├── tests.py                                  - 테스트
│   │    ├── urls.py                                   - accounts views 함수 url 매핑
│   │    └── views.py                                  - 회원 정보 기능 함수 구현
│   ├── storage/                                              
│   │    ├── migrations                                - 테이블 생성
│   │    ├── __init.py                                 - 폴더가 패키지로 인식되게 함
│   │    ├── admin.py                                  - 관리자가 쓸 정보 기입
│   │    ├── apps.py                                   - 응용 프로그램 구성 포함
│   │    ├── models.py                                 - 종료 페이지 데이터 스키마 정의
│   │    ├── serializers.py                            - 데이터 반환 형태 정의
│   │    ├── tests.py                                  - 테스트
│   │    ├── urls.py                                   - storage views 함수 url 매핑 
│   │    └── views.py                                  - 불러오기 기능 함수 구현
```


### accounts
- signup, login, logout 구현 - JWT 토큰 사용
- 유저 정보 조회, 유저 정보 수정, 회원 탈퇴 구현 

### storage
- 동화 진행 중간에 종료 시  해당 페이지 및 유저 정보 저장
- 저장된 시간에 따라 정렬
- 원하는 유저의 불러오기 정보 찾기 



## API Documentation
Coming soon!
