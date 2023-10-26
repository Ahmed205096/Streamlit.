import streamlit as st , pandas as pd



st.markdown('''
<style>
input,label{
    direction:RTL;
}
            
.st-emotion-cache-10trblm{
     text-align:center;       
}
</style>
''',unsafe_allow_html=True)


st.title('')
st.title('تسجيل الدخول')


def auth(user , passw):


    is_user(user , passw)


def is_user(global_user , global_pass):
    df = pd.read_excel('pass.xlsx')



    if len(df[(df['user'].astype(str) == str(global_user))& (df['pass'].astype(str) == str(global_pass))]) > 0:
        st.write('OK')
    else:
        st.write('NO')
    





with st.form('Form1'):
    user = st.text_input('ادخل اسم المستخدم', placeholder='اسم المستخدم')
    password = st.text_input('ادخل كلمة المرور',placeholder='كلمة المرور')

    st.form_submit_button('دخول',use_container_width=True,on_click=auth(user , password))
