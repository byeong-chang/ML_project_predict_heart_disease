import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings('ignore')

class model_selection:
    def __init__(self, model, *xytt):
        # 입력할 모델과 train_test_split의 return 값
        # (4개=x_train,x_test,y_train,y_test)를 xytt로 받아와서 각자 분할해준다.
        self.X_train = xytt[0][0]
        self.X_test = xytt[0][1]
        self.y_train = xytt[0][2]
        self.y_test = xytt[0][3]
        self.model = model
        self.X_train_over = None
        self.y_train_over = None
        self.reg = None
        
    #점수 출력부 함수
    def get_clf_eval(self,y_test, pred=None, pred_proba=None):
        confusion = confusion_matrix(y_test, pred)
        accuracy = accuracy_score(y_test , pred)
        precision = precision_score(y_test , pred)
        recall = recall_score(y_test , pred)
        f1 = f1_score(y_test,pred)
        # ROC-AUC 추가 
        roc_auc = roc_auc_score(y_test, pred_proba)
        print('오차 행렬')
        print(confusion)
        # ROC-AUC print 추가
        print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},\
        F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
        
    #값이 편향적일때 오버샘플링 해주는 함수
    def get_SMOTE(self):
        # SMOTE train 함수
        smote = SMOTE()
        return smote.fit_resample(self.X_train,self.y_train)
    
    # 모델 학습, 예측 , 출력을 실행해주는 함수
    def get_model_apply(self,SMOTE = False):
        if SMOTE == False:
            self.reg = self.model.fit(self.X_train,self.y_train)
        else:
            self.X_train_over , self.y_train_over = self.get_SMOTE()
            self.model.fit(self.X_train_over,self.y_train_over
                                      ,early_stopping_rounds = 30 , eval_metric = 'auc')
            print(self.model.best_score_)
            return self.model
        y_pred = self.reg.predict(self.X_test)
        y_pred_proba = self.reg.predict_proba(self.X_test)[:,1]
        self.get_clf_eval(self.y_test,y_pred,y_pred_proba)  
        # 우리는 심장병에 걸릴 확률을 원하기 때문에 proba 값을 return
    def get_predict_proba(self,val):
        return self.reg.predict_proba(val)[:,1]

# 사용법 예시
#df = pd.read_csv('C:/Chang_git/ML_project_predict_heart_disease/0.data/heart_2020_cleaned_preprocessing.csv')
#X = df.iloc[:,1:]
#y = df['HeartDisease']

#xytt = train_test_split(X,y,test_size=0.2, 
#                        random_state=42 , stratify=y)
#lr = LogisticRegression(multi_class = 'auto', solver = 'lbfgs', random_state=42)
#m1 = model_selection(lr,xytt)
#m1.get_model_apply(SMOTE = True)