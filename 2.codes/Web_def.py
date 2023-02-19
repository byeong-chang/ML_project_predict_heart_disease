import streamlit as st
import time
import numpy as np
import pandas as pd

def yes_or_no_q(question): # yes or No 로 입력된 결과를 1과 0으로 리턴해줍니다.
    '''질문에 대한 답을 리턴해줍니다.'''
    answer = st.radio(question, ['네', '아니요'])
    if answer == '네':
        return 1
    elif answer == '아니요':
        return 0
    
def question(placeholder): # 웹에서 사용자에게 입력받는 부분입니다.
    
    # 초기 설정
    base_df = pd.DataFrame(columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke',
                                    'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex',
                                    'PhysicalActivity', 'SleepTime', 'Asthma', 'KidneyDisease',
                                    'SkinCancer', 'AgeCategory_1824', 'AgeCategory_2529',
                                    'AgeCategory_3034', 'AgeCategory_3539', 'AgeCategory_4044',
                                    'AgeCategory_4549', 'AgeCategory_5054', 'AgeCategory_5559',
                                    'AgeCategory_6064', 'AgeCategory_6569', 'AgeCategory_7074',
                                    'AgeCategory_7579', 'AgeCategory_80orolder',
                                    'Race_AmericanIndianAlaskanNative', 'Race_Asian', 'Race_Black',
                                    'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
                                    'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
                                    'GenHealth_Verygood', 'Diabetic_No', 'Diabetic_Noborderlinediabetes',
                                    'Diabetic_Yes', 'Diabetic_Yesduringpregnancy'])
    
    base_df.loc[0, ['AgeCategory_1824', 'AgeCategory_2529',
                    'AgeCategory_3034', 'AgeCategory_3539', 'AgeCategory_4044',
                    'AgeCategory_4549', 'AgeCategory_5054', 'AgeCategory_5559',
                    'AgeCategory_6064', 'AgeCategory_6569', 'AgeCategory_7074',
                    'AgeCategory_7579', 'AgeCategory_80orolder',
                    'Race_AmericanIndianAlaskanNative', 'Race_Asian', 'Race_Black',
                    'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
                    'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
                    'GenHealth_Verygood', 'Diabetic_No', 'Diabetic_Noborderlinediabetes',
                    'Diabetic_Yes', 'Diabetic_Yesduringpregnancy']] = 0
    
    with placeholder.form("my_form"):
        # 몸무게
        weight = st.number_input('몸무게를 입력해주세요(단위 : kg)')
        # 키
        height = st.number_input(label = '키를 입력해주세요(단위 : cm)')
        # 나이(범주화 필요)
        AgeCategory = st.number_input('당신의 나이는 몇 살입니까(만 나이)?')
        if AgeCategory <= 24:
            base_df.loc[0, 'AgeCategory_1824'] = 1
        elif AgeCategory <= 29:
            base_df.loc[0, 'AgeCategory_2529'] = 1
        elif AgeCategory <= 34:
            base_df.loc[0, 'AgeCategory_3034'] = 1           
        elif AgeCategory <= 39:
            base_df.loc[0, 'AgeCategory_3539'] = 1    
        elif AgeCategory <= 44:
            base_df.loc[0, 'AgeCategory_4044'] = 1   
        elif AgeCategory <= 49:
            base_df.loc[0, 'AgeCategory_4549'] = 1
        elif AgeCategory <= 54:
            base_df.loc[0, 'AgeCategory_5054'] = 1
        elif AgeCategory <= 59:
            base_df.loc[0, 'AgeCategory_5559'] = 1
        elif AgeCategory <= 64:
            base_df.loc[0, 'AgeCategory_6064'] = 1
        elif AgeCategory <= 69:
            base_df.loc[0, 'AgeCategory_6569'] = 1
        elif AgeCategory <= 74:
            base_df.loc[0, 'AgeCategory_7074'] = 1
        elif AgeCategory <= 79:
            base_df.loc[0, 'AgeCategory_7579'] = 1
        else:
            base_df.loc[0, 'AgeCategory_80orolder'] = 1

        # 신체 부상
        PhysicalHealth = int(st.number_input('지난 30일 동안 질병과 부상을 포함해 아픈 일수는 며칠입니까?'))
        base_df.loc[0, 'PhysicalHealth'] = PhysicalHealth
        # 정신건강
        MentalHealth = int(st.number_input('지난 30일 동안 정신 건강이 좋지 않았던 횟수(일수)는 며칠입니까?'))
        base_df.loc[0, 'MentalHealth'] = MentalHealth
        # 수면 시간
        SleepTime = st.number_input('최근 한달 간 평균 수면시간을 입력해주세요(단위 : 시간)')
        base_df.loc[0, 'SleepTime'] = SleepTime
        # 인종
        Race = st.selectbox('당신의 인종은 무엇입니까?', ['아시안', '백인', '히스패닉', '흑인', '기타', '알래스카/미국 원주민'])
        if Race == '아시안':
            base_df.loc[0, 'Race_Asian'] = 1
        elif Race == '백인':
            base_df.loc[0, 'Race_White'] = 1
        elif Race == '히스패닉':
            base_df.loc[0, 'Race_Hispanic'] = 1
        elif Race == '흑인':
            base_df.loc[0, 'Race_Black'] = 1
        elif Race == '기타':
            base_df.loc[0, 'Race_Other'] = 1
        elif Race == '알래스카/미국 원주민':
            base_df.loc[0, 'Race_AmericanIndianAlaskanNative'] = 1
            
        
        # 당뇨
        Diabetic = st.selectbox('당뇨병인 적이 한번이라도 있습니까?', ['네', '아니요', '애매하다', '임신 중에만 당뇨병이였다(여성만 해당)'])
        if Diabetic == '네':
            base_df.loc[0, 'Diabetic_Yes'] = 1
        elif Diabetic == '아니요':
            base_df.loc[0, 'Diabetic_No'] = 1
        elif Diabetic == '애매하다':
            base_df.loc[0, 'Diabetic_Noborderlinediabetes'] = 1
        elif Diabetic == '임신 중에만 당뇨병이였다(여성만 해당)':
            base_df.loc[0, 'Diabetic_Yesduring pregnancy'] = 1
            
        # 건강
        GenHealth = st.selectbox('본인이 느끼기에 당신의 건강 정도는?', ['훌륭하다', '아주 좋다' , '좋다' , '그저 그렇다' , '나쁘다'])
        if GenHealth == '훌륭하다':
            base_df.loc[0, 'GenHealth_Excellent'] = 1
        elif GenHealth == '아주 좋다':
            base_df.loc[0, 'GenHealth_Verygood'] = 1
        elif GenHealth == '좋다':
            base_df.loc[0, 'GenHealth_Good'] = 1
        elif GenHealth == '그저 그렇다':
            base_df.loc[0, 'GenHealth_Fair'] = 1
        elif GenHealth == '나쁘다':
            base_df.loc[0, 'GenHealth_Poor'] = 1        
            
        # 흡연 여부
        Smoking = yes_or_no_q('당신은 평생 동안 적어도 100개 이상의 담배를 피우셨습니까?')
        base_df.loc[0, 'Smoking'] = Smoking
        # 술
        AlcoholDrinking = yes_or_no_q('당신은 과음자입니까?(남성은 주에 14잔 이상 , 여성은 주에 7잔 이상')
        base_df.loc[0, 'AlcoholDrinking'] = AlcoholDrinking
        # 뇌졸중
        Stroke = yes_or_no_q('당신은 뇌졸중 경험이 있습니까?')
        base_df.loc[0, 'Stroke'] = Stroke
        # 운동능력
        DiffWalking = yes_or_no_q('계단을 오를 때 힘들다고 느끼십니까?')
        base_df.loc[0, 'DiffWalking'] = DiffWalking
        # 육체활동
        PhysicalActivity = yes_or_no_q('운동을 하십니까?')
        base_df.loc[0, 'PhysicalActivity'] = PhysicalActivity
        # 천식
        Asthma = yes_or_no_q('천식에 걸린 적이 있습니까?')
        base_df.loc[0, 'Asthma'] = Asthma
        # 신장 질환
        KidneyDisease = yes_or_no_q('신장 질환이 있습니까?')
        base_df.loc[0, 'KidneyDisease'] = KidneyDisease
        # 피부암
        SkinCancer = yes_or_no_q('피부암에 걸린 적이 있습니까?')
        base_df.loc[0, 'SkinCancer'] = SkinCancer
        # 성별
        Sex = st.radio('당신의 성별은 무엇입니까?', ['남자', '여자'])
        if Sex == '남자':
            Sex = 1
        else :
            Sex = 0
        base_df.loc[0, 'Sex'] = Sex
        # BMI
        if height > 0:
            # BMI 계산 및 
            BMI = round(weight / ((height/100) ** 2) , 2)
        else:
            BMI = 0
        base_df.loc[0, 'BMI'] = BMI
            
        time.sleep(4)
        submitted = st.form_submit_button("AI 예측")
        
        # base_df 조정(다른 컬럼 조정)
        base_df = base_df.append(base_df.loc[[0,0,0,0,0]]).reset_index(drop = True)
        
        # 당신이 담배를 피우지 않았다면
        if base_df.at[0, 'Smoking'] == 1:
            base_df.at[1, 'Smoking'] = 0

        # 당신이 과음을 하지 않는다면
        if base_df.at[0, 'AlcoholDrinking'] == 1:
            base_df.at[2, 'AlcoholDrinking'] = 0

        # 잠이 부족한 당신이 수면을 취한다면
        if base_df.at[0, 'SleepTime'] <= 6:
            base_df.at[3, 'SleepTime'] = 9

        # 당신이 정상 범주의 BMI 지수를 가질 경우
        if (base_df.at[0, 'BMI'] < 18.5) or (base_df.at[0, 'BMI'] > 25):
            base_df.at[4, 'BMI'] = 22
            
        # 당신이 운동을 한다면
        if base_df.at[0, 'PhysicalActivity'] == 0:
            base_df.at[5, 'PhysicalActivity'] = 1
        
        return base_df, submitted


def bmi_visualization(BMI): # BMI지수를 계산하여 웹상에서 시각화해주는 자료입니다.
    
    outside_expander_area = st.container()
    state = st.session_state
    with outside_expander_area:
        guage = st.empty()
    bmi_thresholds = [13, 18.5, 25, 30, 43]
    level_labels = ['심각한 저체중', '저체중','정상','과체중','비만', '심각한 비만']

    if BMI <= bmi_thresholds[0]:
        level = level_labels[0]
    elif BMI <= bmi_thresholds[1]:
        level = level_labels[1]
    elif BMI <= bmi_thresholds[2]:
        level = level_labels[2]
    elif BMI <= bmi_thresholds[3]:
        level = level_labels[3]
    elif BMI <= bmi_thresholds[4]:
        level = level_labels[4]
    else:
        level = level_labels[5]

    bmi_gauge_lower = 13 # 0 degrees
    bmi_gauge_upper = 43 # 180 degrees

    bmi_guage_range = (bmi_gauge_upper - bmi_gauge_lower)
    BMI_adjusted = BMI if (BMI >= bmi_gauge_lower and BMI <= bmi_gauge_upper) else (
        bmi_gauge_lower if BMI < bmi_gauge_lower else bmi_gauge_upper
    )
    dial_rotation = round(((BMI_adjusted - bmi_gauge_lower) / bmi_guage_range) * 180.0, 1)

    html = f"""
    <html><body>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300px" height="163px" viewBox="0 0 300 163">
    <g transform="translate(18,18)" style="font-family:arial,helvetica,sans-serif;font-size: 12px;">
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7"></polygon>
            </marker>
            <path id="curvetxt1" d="M-4 140 A140 140, 0, 0, 1, 284 140" style="fill: none;"></path>
            <path id="curvetxt2" d="M33 43.6 A140 140, 0, 0, 1, 280 140" style="fill: #none;"></path>
            <path id="curvetxt3" d="M95 3 A140 140, 0, 0, 1, 284 140" style="fill: #none;"></path>
            <path id="curvetxt4" d="M235.4 33 A140 140, 0, 0, 1, 284 140" style="fill: #none;"></path>
        </defs>
        <path d="M0 140 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#bc2020"></path>
        <path d="M6.9 96.7 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#d38888"></path>
        <path d="M12.1 83.1 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#ffe400"></path>
        <path d="M22.6 63.8 A140 140, 0, 0, 1, 96.7 6.9 L140 140 Z" fill="#008137"></path>
        <path d="M96.7 6.9 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#ffe400"></path>
        <path d="M169.1 3.1 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#d38888"></path>
        <path d="M233.7 36 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#bc2020"></path>
        <path d="M273.1 96.7 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#8a0101"></path>
        <path d="M45 140 A90 90, 0, 0, 1, 230 140 Z" fill="#fff"></path>
        <circle cx="140" cy="140" r="5" fill="#666"></circle>

        <g style="paint-order: stroke;stroke: #fff;stroke-width: 2px;">
            <text x="25" y="111" transform="rotate(-72, 25, 111)">16</text>
            <text x="30" y="96" transform="rotate(-66, 30, 96)">17</text>
            <text x="35" y="83" transform="rotate(-57, 35, 83)">18.5</text>
            <text x="97" y="29" transform="rotate(-18, 97, 29)">25</text>
            <text x="157" y="20" transform="rotate(12, 157, 20)">30</text>
            <text x="214" y="45" transform="rotate(42, 214, 45)">35</text>
            <text x="252" y="95" transform="rotate(72, 252, 95)">40</text>
        </g>

        <g style="font-size: 14px;">
            <text><textPath xlink:href="#curvetxt1">저체중</textPath></text>
            <text><textPath xlink:href="#curvetxt2">정상</textPath></text>
            <text><textPath xlink:href="#curvetxt3">과체중</textPath></text>
            <text><textPath xlink:href="#curvetxt4">비만</textPath></text>
        </g>
        
        <line x1="140" y1="140" x2="65" y2="140" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)">
            <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 140 140" to="{dial_rotation} 140 140" dur="1s" fill="freeze" repeatCount="1"></animateTransform>
        </line>
        
        
    </g>
    </svg>
    </body></html>
    """
    # 저기 맨밑에 끼우면 됨
    # <text x="65" y="120" style="font-size: 28px;font-weight:bold;color:#000;">BMI = {BMI}</text>

    with outside_expander_area:
        import streamlit.components.v1 as components

        with guage:
            components.html(html.replace('\n',''))

        st.markdown(f"<h1 style='text-align: center; font-size: 18px'>BMI 지수 상 {level}입니다({BMI})</h1>", unsafe_allow_html=True)
        # st.caption(f'Rotation: {dial_rotation} degrees')