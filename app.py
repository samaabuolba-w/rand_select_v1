import time

import streamlit as st

from rand_select_v1.selector import random_selection

FLASH_SECONDS = 3
FLASH_INTERVAL = 0.1

st.title("Random Selector")

st.session_state.setdefault("names", [])
st.session_state.setdefault("questions", [])
st.session_state.setdefault("used_names", set())
st.session_state.setdefault("last_pick", None)

with st.form("add_name_form", clear_on_submit=True):
    new_name = st.text_input("Name")
    if st.form_submit_button("Add name") and new_name.strip():
        st.session_state.names.append(new_name.strip())

st.write("Current names:", st.session_state.names)

with st.form("add_question_form", clear_on_submit=True):
    new_question = st.text_input("Question")
    if st.form_submit_button("Add question") and new_question.strip():
        st.session_state.questions.append(new_question.strip())

st.write("Current questions:", st.session_state.questions)

no_repeats = st.checkbox("No repeats")

names = st.session_state.names
questions = st.session_state.questions
used_names = st.session_state.used_names

exhausted = bool(no_repeats and names and set(names) <= used_names)
can_draw = bool(names) and bool(questions) and not exhausted

if exhausted:
    st.warning("All names are selected!")

if st.button("Draw", disabled=not can_draw):
    effective_used = used_names if no_repeats else set()
    placeholder = st.empty()

    end_time = time.time() + FLASH_SECONDS
    while time.time() < end_time:
        flash_name, flash_question = random_selection(
            names, questions, used_names=effective_used
        )
        placeholder.markdown(f"### {flash_name} — {flash_question}")
        time.sleep(FLASH_INTERVAL)

    name, question = random_selection(names, questions, used_names=effective_used)
    if no_repeats:
        st.session_state.used_names.add(name)
    st.session_state.last_pick = (name, question)
    placeholder.empty()

if st.session_state.last_pick:
    name, question = st.session_state.last_pick
    st.success(f"{name}, please answer: {question}")
