# 딥러닝 모델을 사용하는 서버 구현 (FastAPI)
1. 현재 서버가 가지고 있는 분류 모델 리스트를 가져오는 API
2. 분류 모델을 선택하여 악성코드 분류를 실행하는 API

# 딥러닝 모델 요약
전체 구조는 VGG-16을 전이학습함
   - 맨 뒤에 FC 계층(분류계층)을 단일층으로 변경
   - 파라미터가 많이 줄어들어서 학습이 빨라지는데, val_accuracy 수치는 거의 차이가 없었음. 그래서 이러한 구조를 택함.
   - Conv 계층은 학습중단 (프리징), FC 계층만 학습가능하도록 설정
   - 결과는 총 25가지 클래스에 대한 분류 결과 (각각의 클래스에 속할 확률)
  
# 학습 및 분류 데이터
Malimg 데이터셋
   - 25가지로 분류된 악성코드 이미지들 (학술적으로 사용되는 데이터셋)
   - 새로운 파일을 분류할 때는 224 x 224 x 3의 이미지로 만드는 전처리를 이용하여 모델의 INPUT_SHAPE에 맞춤
   - 참고: https://vision.ece.ucsb.edu/sites/default/files/publications/nataraj_vizsec_2011_paper.pdf (전처리 방법과 데이터셋 모두 이 논문의 방식을 사용함)

# fastapi 셋팅
1. Tensorflow, Fastapi, Numpy 설치
2. Tensorflow로 구현한 분류 모델은 모델세이브해서 서버에 올림 (model_path 변수에 저장)
