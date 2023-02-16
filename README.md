# ML_project_predict_heart_disease
- 팀명 : 우병목
- 주제 : 심장질환 판별 머신러닝 모델 웹 구현
- 데이터셋 : 캐글(Personal Key Indicators of Heart Disease) https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

- 목적/효과 : 대중이 쉽게 접근 가능한 심장질환 판별 및 심장질환 발생 확률 제공
- 기술스택(라이브러리)
	- 데이터 가공 : pandas, numpy
	- 데이터 시각화 : matplotlib, seaborn
	- 머신러닝 : sklearn, lightgbm, xgboost, catboost 등
	- 웹구현 : streamlit
- 역할분담 
	- 민병창 : 범주형 변수 전환/오버샘플링(SMOTE)
	- 김경목 :	 데이터 시각화
	- 우상욱 : 웹 구현
	- 머신러닝 : 팀원 전부 참여
	- 발표 : 사다리타기
- 협업도구
	- GIT, NOTION

- 웹구현 아이디어 :
	1) 사용자가 웹에 접속해서, 자신의 정보를 입력
	2) 머신러닝 모델로 심장질환이 있는지 없는지 예측
	3) PRED_PROBA 활용 심장질환에 걸렸을 확률 반환
	4) 사용자에게 심장질환 유무 및 예측 확률 반환.
