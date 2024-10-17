import streamlit as st
import score_criteria as s

st.set_page_config(page_title="体测计算器")

# 体测计算器界面
st.image("sport.png")
st.subheader(":rainbow[体测计算器]")

col1, col2 = st.columns(2)

with col1:
      gender = st.selectbox('性别', ('男', '女'))
      weight = st.number_input("体重 (千克)")
      jump_rope = st.number_input('一分钟跳绳 (个)')   
      sit_up = st.number_input('仰卧起坐 (个)')
      sit_and_reach = st.number_input('坐位体前屈 (厘米)')

with col2:
      grade = st.selectbox("年级",(1, 2, 3, 4, 5, 6))
      height = st.number_input('身高 (米)')
      capacity = st.number_input('肺活量 (毫升)')
      fifty_m_run = st.number_input('50米跑 (秒)')
      if grade >= 5:
            col1, col2 = st.columns(2)
            with col1:
                  run_8r_minutes = st.number_input("50米 x 8往返跑 (分钟)")
            with col2:
                  run_8r_seconds = st.number_input("50米 x 8往返跑 (秒)")

if st.button("&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; 计算体测分数 &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;"):
    bmi_score = s.get_bmi_score(gender, grade, weight, height)
    lung_capacity_score = s.get_lung_capacity_score(gender, grade, capacity)
    jump_rope_score = s.get_jump_rope_score(gender, grade, jump_rope)
    fifty_m_run_score = s.get_50m_run_score(gender, grade, fifty_m_run)
    sit_up_score = s.get_sit_up_score(gender, grade, sit_up)
    sit_and_reach_score = s.get_sit_and_reach_score(gender, grade, sit_and_reach)
    jump_rope_bonus = s.get_jump_rope_bonus(gender, grade, jump_rope)
    if grade >= 5:
          fifty_8_r = s.get_50m_8r_run_score(gender, grade, run_8r_minutes, run_8r_seconds)
          total_score = s.get_total_score(grade, bmi_score, lung_capacity_score, fifty_m_run_score, sit_and_reach_score, sit_up_score, jump_rope_score, fifty_8_r)
    else:
          total_score = s.get_total_score(grade, bmi_score, lung_capacity_score, fifty_m_run_score, sit_and_reach_score, sit_up_score, jump_rope_score)
          
    st.markdown(f'''
      :blue-background[BMI分数: {bmi_score}] 
      &nbsp; &nbsp; &nbsp; :orange-background[肺活量分数: {lung_capacity_score}]
      &nbsp; &nbsp; &nbsp; :violet-background[跳绳分数: {jump_rope_score}] 
      &nbsp; &nbsp; &nbsp; :green-background[50米跑分数: {fifty_m_run_score}]
      &nbsp; &nbsp; &nbsp; :red-background[仰卧起坐分数: {sit_up_score}] 
      &nbsp; &nbsp; &nbsp; :grey-background[坐位体前屈分数: {sit_and_reach_score}]
      &nbsp; &nbsp; &nbsp; :rainbow-background[跳绳加分: {jump_rope_bonus}]
      &nbsp; &nbsp; &nbsp; :rainbow-background[标准分: {total_score}]
      &nbsp; &nbsp; &nbsp; :rainbow-background[总分: {total_score}+{jump_rope_bonus}] 
      ''')
