import streamlit as st
import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description, due_date=None):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'Pending',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False

# Initialize Streamlit app
st.set_page_config(page_title="Task Manager", page_icon="✅")
st.title("📝 Task Manager")

# Initialize TaskManager
task_manager = TaskManager()

# Sidebar for adding new tasks
with st.sidebar:
    st.header("Add New Task")
    with st.form("new_task", clear_on_submit=True):
        title = st.text_input("Task Title")
        description = st.text_area("Task Description")
        due_date = st.date_input("Due Date (Optional)")
        
        if st.form_submit_button("Add Task"):
            if title and description:
                task = task_manager.add_task(title, description, due_date.strftime("%Y-%m-%d"))
                st.success(f"Task '{title}' added successfully!")
            else:
                st.error("Please fill in both title and description!")

# Main content area
if not task_manager.tasks:
    st.info("No tasks found. Add a new task using the sidebar!")
else:
    # Filter tasks
    status_filter = st.selectbox("Filter by Status", ["All", "Pending", "Completed"])
    filtered_tasks = task_manager.tasks
    if status_filter != "All":
        filtered_tasks = [task for task in task_manager.tasks if task['status'] == status_filter]

    # Display tasks
    for task in filtered_tasks:
        with st.expander(f"Task {task['id']}: {task['title']} ({task['status']})"):
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Due Date:** {task['due_date'] or 'Not set'}")
            st.write(f"**Created:** {task['created_at']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if task['status'] == 'Pending':
                    if st.button(f"✅ Mark Complete #{task['id']}", key=f"complete_{task['id']}"):
                        task_manager.mark_completed(task['id'])
                        st.rerun()
            with col2:
                if st.button(f"🗑️ Delete #{task['id']}", key=f"delete_{task['id']}"):
                    task_manager.delete_task(task['id'])
                    st.rerun()

# Add some styling
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)