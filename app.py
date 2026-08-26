# ============================================================
# CODEALPHA INTERNSHIP - TASK 3
# TASK AUTOMATION WITH PYTHON SCRIPTS
# File Automation Tool
# Created by: Tehmina Anwar
# ============================================================

import streamlit as st
from pathlib import Path
from collections import Counter
import zipfile
import io


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CodeAlpha Task 3 - File Automation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# FILE CATEGORIES
# ============================================================

FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg", ".tiff"
    ],

    "Documents": [
        ".doc", ".docx", ".txt", ".rtf", ".odt"
    ],

    "PDF_Files": [
        ".pdf"
    ],

    "Excel_Files": [
        ".xls", ".xlsx", ".csv"
    ],

    "PowerPoint_Files": [
        ".ppt", ".pptx"
    ],

    "Audio_Files": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg", ".m4a"
    ],

    "Video_Files": [
        ".mp4", ".avi", ".mkv",
        ".mov", ".wmv", ".flv", ".webm"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz"
    ],

    "Python_Files": [
        ".py"
    ],

    "Code_Files": [
        ".html", ".css", ".js",
        ".java", ".cpp", ".c",
        ".json", ".xml", ".sql"
    ]
}


# ============================================================
# CATEGORY ICONS
# ============================================================

CATEGORY_ICONS = {
    "Images": "🖼️",
    "Documents": "📄",
    "PDF_Files": "📕",
    "Excel_Files": "📊",
    "PowerPoint_Files": "📽️",
    "Audio_Files": "🎵",
    "Video_Files": "🎬",
    "Archives": "📦",
    "Python_Files": "🐍",
    "Code_Files": "💻",
    "Other_Files": "📁"
}


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 21px;
        margin-bottom: 5px;
    }

    .creator {
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 25px;
    }

    .info-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 20px;
    }

    .category-card {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 10px;
    }

    .footer {
        text-align: center;
        padding: 25px;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 File Automation Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'CodeAlpha Internship — Task 3'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="creator">'
    '👩‍💻 Created by: Tehmina Anwar'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🤖 File Automation")

    st.write(
        "Automatically organize files "
        "according to their extensions."
    )

    st.divider()

    st.subheader("✨ Supported Categories")

    for category in FILE_CATEGORIES:

        icon = CATEGORY_ICONS.get(
            category,
            "📁"
        )

        st.write(
            f"{icon} {category}"
        )

    st.divider()

    st.caption(
        "CodeAlpha Internship"
    )

    st.caption(
        "Task 3 — Task Automation"
    )

    st.caption(
        "Created by Tehmina Anwar"
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

st.header("🎯 About This Project")

st.markdown(
    """
    <div class="info-box">

    This Python automation tool automatically organizes
    uploaded files into separate categories based on their
    file extensions.

    Instead of manually sorting files, the application
    analyzes every file and places it into the appropriate
    category folder.

    <br>

    <b>🚀 Main Features:</b>

    <br><br>

    • Upload multiple files<br>
    • Automatic file type detection<br>
    • File statistics<br>
    • Automation preview<br>
    • Category-wise organization<br>
    • Duplicate filename handling<br>
    • Organized ZIP download<br>
    • Demo mode for testing<br>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CATEGORY FUNCTION
# ============================================================

def get_category(extension):
    """
    Detect file category using file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Other_Files"


# ============================================================
# DEMO FILE CREATOR
# ============================================================

def create_demo_files():
    """
    Create sample files for demonstration.
    """

    demo_files = [

        (
            "demo_photo.jpg",
            "Images"
        ),

        (
            "demo_image.png",
            "Images"
        ),

        (
            "demo_document.txt",
            "Documents"
        ),

        (
            "demo_resume.docx",
            "Documents"
        ),

        (
            "demo_report.pdf",
            "PDF_Files"
        ),

        (
            "demo_data.csv",
            "Excel_Files"
        ),

        (
            "demo_sheet.xlsx",
            "Excel_Files"
        ),

        (
            "demo_presentation.pptx",
            "PowerPoint_Files"
        ),

        (
            "demo_song.mp3",
            "Audio_Files"
        ),

        (
            "demo_video.mp4",
            "Video_Files"
        ),

        (
            "demo_archive.zip",
            "Archives"
        ),

        (
            "demo_code.py",
            "Python_Files"
        ),

        (
            "demo_page.html",
            "Code_Files"
        ),

        (
            "demo_unknown.xyz",
            "Other_Files"
        )
    ]

    files = []

    for filename, category in demo_files:

        content = (
            "CodeAlpha Internship - Task 3\n"
            "File Automation Demo\n\n"
            f"File Name: {filename}\n"
            f"Category: {category}\n"
        )

        files.append(
            {
                "name": filename,
                "category": category,
                "data": content.encode("utf-8")
            }
        )

    return files


# ============================================================
# UPLOAD SECTION
# ============================================================

st.header("📤 Upload Your Files")

st.write(
    "Select one or multiple files to analyze and organize."
)

uploaded_files = st.file_uploader(
    "Choose files",
    accept_multiple_files=True,
    type=None
)


# ============================================================
# DEMO MODE
# ============================================================

st.header("🧪 Demo Mode")

st.write(
    "Don't have files available? "
    "Generate sample files and test the automation."
)

demo_button = st.button(
    "🧪 Generate Demo Files",
    use_container_width=True
)


# ============================================================
# RESET BUTTON
# ============================================================

if st.button(
    "🔄 Reset Demo",
    use_container_width=True
):

    if "demo_files" in st.session_state:

        del st.session_state["demo_files"]

    st.rerun()


# ============================================================
# PREPARE FILE DATA
# ============================================================

file_data = []


# ------------------------------------------------------------
# USER UPLOADS
# ------------------------------------------------------------

if uploaded_files:

    for uploaded_file in uploaded_files:

        extension = Path(
            uploaded_file.name
        ).suffix.lower()

        file_data.append(
            {
                "name": uploaded_file.name,
                "category": get_category(extension),
                "data": uploaded_file.getvalue()
            }
        )


# ------------------------------------------------------------
# DEMO BUTTON
# ------------------------------------------------------------

elif demo_button:

    file_data = create_demo_files()

    st.session_state["demo_files"] = file_data


# ------------------------------------------------------------
# STORED DEMO
# ------------------------------------------------------------

elif "demo_files" in st.session_state:

    file_data = st.session_state["demo_files"]


# ============================================================
# PROCESS FILES
# ============================================================

if file_data:

    st.success(
        f"✅ {len(file_data)} files ready for automation!"
    )


    # ========================================================
    # STATISTICS
    # ========================================================

    statistics = Counter(
        file["category"]
        for file in file_data
    )

    st.header("📊 File Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📦 Total Files",
            len(file_data)
        )

    with col2:

        st.metric(
            "📁 Categories",
            len(statistics)
        )

    with col3:

        image_count = statistics.get(
            "Images",
            0
        )

        st.metric(
            "🖼️ Images",
            image_count
        )

    with col4:

        st.metric(
            "🤖 Status",
            "Ready"
        )


    # ========================================================
    # CATEGORY SUMMARY
    # ========================================================

    st.subheader("📈 Category Summary")

    categories = sorted(
        statistics.items()
    )

    cols = st.columns(4)

    for index, (category, count) in enumerate(
        categories
    ):

        icon = CATEGORY_ICONS.get(
            category,
            "📁"
        )

        with cols[index % 4]:

            st.metric(
                f"{icon} {category}",
                count
            )


    # ========================================================
    # PREVIEW
    # ========================================================

    st.header("🔍 Automation Preview")

    preview = []

    for file in file_data:

        icon = CATEGORY_ICONS.get(
            file["category"],
            "📁"
        )

        preview.append(
            {
                "📄 File Name": file["name"],
                "📁 Destination": (
                    f"{icon} {file['category']}"
                )
            }
        )

    st.dataframe(
        preview,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # ORGANIZED STRUCTURE
    # ========================================================

    st.header("📂 Organized Folder Structure")

    for category in sorted(statistics):

        icon = CATEGORY_ICONS.get(
            category,
            "📁"
        )

        st.subheader(
            f"{icon} {category}"
        )

        category_files = [
            file["name"]
            for file in file_data
            if file["category"] == category
        ]

        for filename in category_files:

            st.write(
                f"📄 {filename}"
            )


    # ========================================================
    # CREATE ZIP
    # ========================================================

    def create_zip(files):

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(
            zip_buffer,
            mode="w",
            compression=zipfile.ZIP_DEFLATED
        ) as zip_file:

            used_paths = set()

            for file in files:

                category = file["category"]

                original_filename = file["name"]

                filename = original_filename

                path = (
                    f"{category}/{filename}"
                )

                counter = 1

                while path in used_paths:

                    stem = Path(
                        original_filename
                    ).stem

                    suffix = Path(
                        original_filename
                    ).suffix

                    filename = (
                        f"{stem}_{counter}"
                        f"{suffix}"
                    )

                    path = (
                        f"{category}/{filename}"
                    )

                    counter += 1

                used_paths.add(path)

                zip_file.writestr(
                    path,
                    file["data"]
                )

        zip_buffer.seek(0)

        return zip_buffer


    # ========================================================
    # AUTOMATION
    # ========================================================

    st.header("🚀 Run Automation")

    st.write(
        "Click the button below to organize all files "
        "into category folders and create a ZIP package."
    )

    if st.button(
        "🚀 ORGANIZE ALL FILES",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner(
            "🤖 Organizing files..."
        ):

            zip_data = create_zip(
                file_data
            )

        st.success(
            "🎉 Automation completed successfully!"
        )

        st.balloons()

        st.download_button(
            label="📥 Download Organized ZIP",
            data=zip_data,
            file_name=(
                "Tehmina_CodeAlpha_Task3_"
                "Organized_Files.zip"
            ),
            mime="application/zip",
            use_container_width=True
        )


    # ========================================================
    # DOWNLOAD REPORT
    # ========================================================

    st.header("📋 Automation Report")

    report_lines = []

    report_lines.append(
        "CODEALPHA INTERNSHIP - TASK 3"
    )

    report_lines.append(
        "TASK AUTOMATION WITH PYTHON SCRIPTS"
    )

    report_lines.append(
        "Created by: Tehmina Anwar"
    )

    report_lines.append(
        ""
    )

    report_lines.append(
        f"Total Files: {len(file_data)}"
    )

    report_lines.append(
        f"Categories: {len(statistics)}"
    )

    report_lines.append(
        ""
    )

    report_lines.append(
        "FILE ORGANIZATION"
    )

    report_lines.append(
        "-" * 50
    )

    for file in file_data:

        report_lines.append(
            f"{file['name']} "
            f"-> {file['category']}"
        )

    report_lines.append(
        ""
    )

    report_lines.append(
        "CATEGORY SUMMARY"
    )

    report_lines.append(
        "-" * 50
    )

    for category, count in sorted(
        statistics.items()
    ):

        report_lines.append(
            f"{category}: {count}"
        )

    report = "\n".join(
        report_lines
    )

    st.download_button(
        label="📄 Download Automation Report",
        data=report,
        file_name="CodeAlpha_Task3_Report.txt",
        mime="text/plain",
        use_container_width=True
    )


# ============================================================
# EMPTY STATE / HOW IT WORKS
# ============================================================

else:

    st.info(
        "👆 Upload files OR click "
        "🧪 Generate Demo Files to start."
    )

    st.header("💡 How It Works")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("1️⃣ Upload")

        st.write(
            "Upload one or multiple files."
        )

    with col2:

        st.subheader("2️⃣ Analyze")

        st.write(
            "The application detects the file "
            "type using its extension."
        )

    with col3:

        st.subheader("3️⃣ Organize")

        st.write(
            "Files are placed into category "
            "folders inside an organized ZIP."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🤖 <strong>CodeAlpha Internship — Task 3</strong><br>

    Task Automation with Python Scripts<br><br>

    👩‍💻 Created by <strong>Tehmina Anwar</strong>

    </div>
    """,
    unsafe_allow_html=True
)
