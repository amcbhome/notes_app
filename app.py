import streamlit as st
from pathlib import Path

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Notes Vault",
    page_icon="📓",
    layout="wide"
)

st.title("📓 Notes Vault")
st.caption("Markdown-based notes and reusable code snippets")

# -----------------------------
# Notes directory
# -----------------------------
NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load notes
# -----------------------------
notes = sorted(NOTES_DIR.glob("*.md"))

if not notes:
    st.info("No notes found. Add Markdown files to the `notes/` directory.")
    st.stop()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Notes")

selected_note = st.sidebar.radio(
    "Select a note",
    notes,
    format_func=lambda p: p.stem.replace("_", " ").title()
)

search = st.sidebar.text_input("Search in note")

# -----------------------------
# Read note
# -----------------------------
content = selected_note.read_text(encoding="utf-8")

# -----------------------------
# Search filter (simple + fast)
# -----------------------------
if search:
    if search.lower() not in content.lower():
        st.warning(f"No matches for **{search}** in this note.")
    else:
        st.success(f"Matches found for **{search}**")

# -----------------------------
# Render Markdown
# -----------------------------
st.markdown(content)

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(
    "Notes are written in Markdown. "
    "Code blocks are copy-paste ready. "
    "Managed with Streamlit + GitHub."
)
