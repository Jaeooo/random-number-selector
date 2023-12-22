import streamlit as st
import random

f = open("numbers.txt", "r")
numbers = list(map(int, f.readline().split()))
f.close()

st.title("Random Number Selector")

st.write("숫자 몇 개를 랜덤으로 뽑을까요?")
n = st.text_input("숫자 개수")

if st.button("뽑기"):
    count = 0
    try:
        count = int(n)
    except:
        count = 0

    if len(numbers) < count:
        st.write("남은 개수보다 많이 뽑을 수 없습니다.")

    else:
        random.shuffle(numbers)
        st.write(numbers[:count])

        f = open("numbers.txt", "w")
        f.write(" ".join(map(str, numbers[count:])))
        f.close()

        f = open("numbers.txt", "r")
        numbers = list(map(int, f.readline().split()))
        f.close()


if st.button("숫자 초기화"):
    numbers = [str(i) for i in range(1, 71)]
    f = open("numbers.txt", "w")
    f.write(" ".join(numbers))
    f.close()

st.write("남은 숫자 개수 : ", len(numbers))
