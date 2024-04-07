# 딥러닝 모델을 사용하는 서버 구현 (FastAPI)
1. 현재 서버가 가지고 있는 모델 리스트를 가져오는 API
2. 모델을 선택하여 악성코드 분류를 실행하는 API

# 모델 구조
1. VGG16 전이학습
2. 파일을 224 x 224 x 3의 이미지로 만드는 전처리
3. 분류계층은 데이터셋의 클래스인 25개의 단일층 (DROPOUT을 0.7정도 넣으니 오버피팅이 많이 줄어서 넣어줌)
4. 모델의 학습은 Malimg 데이터셋을 사용하였다. (실제 악성코드를 수집하여 하진 않고 학술용 데이터셋을 사용)
   https://vision.ece.ucsb.edu/sites/default/files/publications/nataraj_vizsec_2011_paper.pdf

# fastapi 셋팅
1. 텐서플로우, fastapi, numpy 설치
2. 텐서플로우 모델은 모델세이브해서 올림 (model_path 변수에 저장)

# 결과값
1. 각각의 클래스에 확률(소숫점 4자리까지)을 더해서 리스트로 만듬
2. 총 25가지 클래스
