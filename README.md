# ML_project_predict_heart_disease
- 팀명 : 우병목
- 주제 : 심장질환 판별 머신러닝 모델 웹 구현
- 구현 웹사이트 : 
	https://sangwookwoo-ml-project-predict-heart-diseas-heartdisease-fjfpjg.streamlit.app/
- 데이터셋 : 캐글(Personal Key Indicators of Heart Disease) https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease
- 목적/효과 : 대중이 쉽게 접근 가능한 심장질환 판별 및 심장질환 발생 확률 제공
- 기술스택
	<div align=center> 
	<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white">
	<img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=Numpy&logoColor=white">
	    <br>
	<img src="https://img.shields.io/badge/matplotlib-006c66?style=for-the-badge&logo=Pandas&logoColor=white">
	<img src="https://img.shields.io/badge/Seaborn-0080ff?style=for-the-badge&logo=Seaborn&logoColor=white">
	    <br>
	<img src="https://img.shields.io/badge/sckit-learn-F7931E?style=for-the-badge&logo=sckit-learn&logoColor=white">
	<img src="https://img.shields.io/badge/lightGBM-ffd400?style=for-the-badge&logo=&logoColor=white">
	<img src="https://img.shields.io/badge/XGBoost-4aa8d8?style=for-the-badge&logo=&logoColor=white">
	<img src="https://img.shields.io/badge/CatBoost-fff44f?style=for-the-badge&logo=&logoColor=white">
	    <br>
	협업도구 :
	<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
	<img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=Canva&logoColor=white">
	<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">
	    <br>
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
	</div>
- 역할분담 
	- `민병창` : EDA, 전처리, 시각화, 머신러닝 학습, 머신러닝 모델링
	- `김경목` : EDA, 시각화, 머신러닝 학습, 머신러닝 모델링
	- `우상욱` : EDA, 전처리, 머신러닝 모델링, 웹 구현



- 웹구현 아이디어 :
	1) 사용자가 웹에 접속해서, 자신의 정보를 입력
	2) 머신러닝 모델로 심장질환이 있는지 없는지 예측
	3) PRED_PROBA 활용 심장질환에 걸렸을 확률 반환
	4) 사용자에게 심장질환 유무 및 예측 확률 반환.
	5) 개선 여부에 대해 알려줌.
	
