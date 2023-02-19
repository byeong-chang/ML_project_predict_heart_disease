import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings('ignore')

def fold_K(X, y, model):  # 학습모델과 x,y 값을 입력해주면 kfold를 5번 수행하여 평균치를 구해 정확도와 재현율을 출력해주고 마지막 모델을 반환해주는 함수입니다.
    kf = KFold(n_splits = 5, shuffle = True, random_state = 42)
    acc_test_score = []
    acc_train_score = []
    rec_test_score = []
    rec_train_score = []
    
    for train_index, test_index in kf.split(X): # 5번의 kfold로 분힐하여 인덱스로 사용합니다.
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index] 
        model.fit(X_train, y_train) # 입력받은 모델을 학습시킵니다.
        y_pred = model.predict(X_test) # test의 예측치를 얻어냅니다.
        y_pred_train = model.predict(X_train) # train의 예측치를 얻어냅니다.
        #구한 재현율과 정확도를 각각 리스트에 추가해줍니다.
        acc_train_score.append(accuracy_score(y_train,y_pred_train))
        acc_test_score.append(accuracy_score(y_test,y_pred))
        
        rec_train_score.append(recall_score(y_train , y_pred_train))
        rec_test_score.append(recall_score(y_test , y_pred))

    #리스트에 저장된 값을 평균화하여 출력해줍니다.
    print('정확도 : train score : {}'.format(np.array(acc_train_score).mean()))
    print('정확도 : test score : {}'.format(np.array(acc_test_score).mean()))
    print('재현율 : train score : {}'.format(np.array(rec_train_score).mean()))
    print('재현율 : test score : {}'.format(np.array(rec_test_score).mean()))
    
    return model

class model_selection: # 초기에 학습을 편하게 하기위해 제작된 class 입니다.
                        # 하지만 모든 모델에 대해 한 클래스로 적용함에 있어 불편함을 느껴 실제 학습에는 사용되지 않은 코드입니다.
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
        # SMOTE 옵션이 적용되냐 아니냐에 따라 학습시킬 때 입력되는 데이터 형태가 달라집니다.
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
    def get_predict_proba(self,val): # 웹에서 predict proba값을 쉽게 가져오기 위해 만든 함수입니다.
        return self.reg.predict_proba(val)[:,1]

#  클래스 사용법 예시
#df = pd.read_csv('C:/Chang_git/ML_project_predict_heart_disease/0.data/heart_2020_cleaned_preprocessing.csv')
#X = df.iloc[:,1:]
#y = df['HeartDisease']

#xytt = train_test_split(X,y,test_size=0.2, 
#                        random_state=42 , stratify=y)
#lr = LogisticRegression(multi_class = 'auto', solver = 'lbfgs', random_state=42)
#m1 = model_selection(lr,xytt)
#m1.get_model_apply(SMOTE = True)