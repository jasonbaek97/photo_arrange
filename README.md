Jason Nas Photo file Arrage

목적
 - NAS 폴더에 너무 두서없이 모아놓은 이미지들 일괄 정리 목적

주요 기능
 - 작업 디렉토리에 있는 이미지파일의 메타정보(exif)와 파일생성일을 판단하여 년/월 폴더로 자동 정리
 - ubuntu, windows, mac os 구분없이 작동
 - 이미지 중복인 경우 이름변경(파일명 앞에 dup_ 추가)하여 이동

분류 방법
1. 작업 디렉토리의 Photo 파일들을 연/월 순으로 정리
2. Image 정보를 기준 으로 생성(촬열) 날짜별로 폴더 구성
   - 년(yyyy) > 월(mm) 생성하여 폴더 이관
   - 이미지 메타정보(exif)가 없으면, 파일생성일자 기준으로 정리
   
   
3. Diretory 구조
   - Photo > yyyy > mm
   - Photo > error : 분류 에러 대상
   
 
4. 사용법 
    - 작업하려고 하는 폴더(디렉토리)에 정리할 이미지 파일을 모조리 모아 놓는다
    - python photoarrange.py 실행
    - 파일 문제가 있는경우 error 로그 콘솔에 찍어주고, error 폴더로 

5. 설치 필요한 패키지
    - pillow 
    - 그외 3.9 기본 패키지
 

