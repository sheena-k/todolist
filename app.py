import streamlit as st
import backend as main 

st.set_page_config(layout="centered")

st.title("Simple To-Do List App!")


st.markdown('<div class="subheading-container"><h3 class="subheading">Create and Manage Your Tasks...</h3></div>', unsafe_allow_html=True)

# Input for adding new tasks

new_task = st.text_input("Add a new task:")

if st.button("Add Task"):
    if new_task:
        main.add_task(new_task)
        st.success("Task added successfully")

st.header("Your Tasks")

# Displaying tasks
tasks = main.get_task()
if tasks:
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        with col1:
            st.checkbox(task["task"],
                        value=task["completed"],
                        key=f"task_checkbox_{i}",
                        on_change=main.mark_complete, args=(i,)) # Pass the index as an argument
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                main.delete_task(i)
                st.rerun()
else:
    st.info("No tasks yet in the List!")
