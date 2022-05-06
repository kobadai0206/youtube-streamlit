import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'


left_colimn, right_column = st.beta_columns(2)
button = left_colimn.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ')
expander3.write('問い合わせ3の回答')