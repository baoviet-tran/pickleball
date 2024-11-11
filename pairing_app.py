import random
import streamlit as st

# Danh sách 6 người
people = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6']

# Tiêu đề cho ứng dụng
st.title('Chia ngẫu nhiên 6 người thành 3 cặp')

# Nút nhấn để chia cặp
if st.button('Chia cặp'):
    random.shuffle(people)  # Trộn ngẫu nhiên danh sách
    pairs = [(people[i], people[i+1]) for i in range(0, len(people), 2)]  # Tạo cặp

    # Hiển thị kết quả
    st.write("Kết quả chia cặp:")
    for pair in pairs:
        st.write(f"Cặp: {pair[0]} và {pair[1]}")
