import streamlit as st
#import os
from agent_backend import generate_blog
from db import init_db, save_blog, get_all_blogs, get_blog_by_filename

init_db()

if "selected_blog" not in st.session_state:
    st.session_state["selected_blog"] = None


st.title("AI Technical Blog Writer")

# Sidebar
st.sidebar.title("Saved Blogs")
files = get_all_blogs()
selected_blog = None

if files:
    for filename in files:
        if st.sidebar.button(filename, use_container_width=True):
            st.session_state["selected_blog"] = filename
else:
    st.sidebar.info("No blogs yet.")

# Tabs
tab1, tab2 = st.tabs(["📝 Generate Blog", "📖 View Blog"])


# Generate blog tab
with tab1:
    st.header("Generate New Blog")
    topic = st.text_input("Enter Blog Topic")

    if st.button("Generate Blog"):
        if topic.strip() == "":
            st.warning("Please enter a topic")
        else:
            status = st.empty()
            status.write("Generation in process...")
            
            with st.spinner("Generating blog... (Check back after 2-3 minutes)"):
                blog = generate_blog(topic)
    
            save_blog(blog["title"], blog["filename"], blog["markdown"])
            
            st.success(f"Blog saved in database as {blog['filename']}")
            st.rerun()
        

# View blog tab
with tab2:
    st.header("View Blog")
    selected = st.session_state.get("selected_blog")
    
    if selected:
        content = get_blog_by_filename(selected)
        if content:
            st.download_button(
                label="Download as .md",
                data=content,
                file_name=selected,
                mime="text/markdown"
            )
            st.markdown(content)
        else:
            st.error("Blog not found")
    else:
        st.info("Select a blog from the sidebar")
      