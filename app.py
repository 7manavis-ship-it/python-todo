import json
import os
import streamlit as st

TODO_FILE = "todo.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

st.title("📝 나의 심플 할 일 관리 프로그램")

todos = load_todos()

new_task = st.text_input("➕ 새로운 할 일을 입력하세요:")
if st.button("추가하기"):
    if new_task:
        todos.append({"task": new_task, "done": False})
        save_todos(todos)
        st.success(f"'{new_task}' 추가 완료!")
        st.rerun()

st.subheader("📋 할 일 목록")
if not todos:
    st.info("등록된 할 일이 없습니다.")
else:
    for idx, todo in enumerate(todos):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            is_done = st.checkbox(todo["task"], value=todo["done"], key=f"todo_{idx}")
            if is_done != todo["done"]:
                todos[idx]["done"] = is_done
                save_todos(todos)
        with col2:
            if st.button("삭제", key=f"del_{idx}"):
                todos.pop(idx)
                save_todos(todos)
                st.rerun()