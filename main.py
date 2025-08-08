import streamlit as st
from backend import add_reel, search_tool  # Import backend functions

# Title of the web app
st.title("AI Tool Finder")

# Add a reel to the database (Optional)
st.subheader("Add a New Reel")
link = st.text_input("Instagram Reel Link")
tag = st.text_input("Tag (e.g., Linkedin Post Automation)")
tool_name = st.text_input("AI Tool Name (e.g., ABC.ai)")

if st.button("Add Reel"):
    if link and tag and tool_name:
        add_reel(link, tag, tool_name)  # Use the appropriate backend function (SQLite or CSV)
        st.success(f"Reel with tag '{tag}' added successfully!")

# Chat interface
st.subheader("Ask for an AI Tool")

user_message = st.text_input("Type a tag (e.g., Linkedin):")

if st.button("Get Tool"):
    if user_message:
        response = search_tool(user_message)  # Use the updated backend function
        st.write(response)
    else:
        st.write("Please enter a tag.")
