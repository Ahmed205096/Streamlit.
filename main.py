import streamlit as st


st.markdown('''

<style>
            
input,label{
    direction : RTL;
}
            
.st-emotion-cache-10trblm{
        text-align : center;
}
            
</style>

''' , unsafe_allow_html=True)

st.header('تسجيل الدخول')


login_form = st.form('Login Form')

with login_form:
    st.text_input(label='ادخل اسم المستخدم' , placeholder='اسم المستخدم')
    st.text_input(label='ادخل كلمة المرور' , placeholder='كلمة المرور' , type='password')

    st.form_submit_button(label='دخول',use_container_width=True)