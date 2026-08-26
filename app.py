import streamlit as st
from pathlib import Path
from collections import Counter
import zipfile
import io


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CodeAlpha Task 3",
    page_icon="🤖",
    layout="wide"
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
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a"
    ],

    "Video_Files": [
        ".mp4", ".avi", ".mkv", ".mov",
        ".wmv", ".flv", ".webm"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],

    "Python_Files": [
        ".py"
    ],

    "Code_Files": [
        ".html", ".css", ".js", ".java",
        ".cpp", ".c", ".json", ".xml", ".sql"
    ]
}


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
    }

    .creator {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🤖 File Automation Tool</div>',
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
# ABOUT
# ============================================================

st.header("🎯 About This Project")

st.write(
    """
    This Python automation tool automatically organizes files
    into separate categories based on their file extensions.

    You can upload your own files or use Demo Mode to test
    the application without having any files on your laptop.
    """
)


# ============================================================
# CATEGORY FUNCTION
# ============================================================

def get_category(extension):

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Other_Files"


# ============================================================
# DEMO FILES
# ============================================================

def create_demo_files():

    demo_files = [
        ("demo_photo.jpg", "Images"),
        ("demo_image.png", "Images"),
        ("demo_document.txt", "Documents"),
        ("demo_report.pdf", "PDF_Files"),
        ("demo_data.csv", "Excel_Files"),
        ("demo_presentation.pptx", "PowerPoint_Files"),
        ("demo_song.mp3", "Audio_Files"),
        ("demo_video.mp4", "Video_Files"),
        ("demo_archive.zip", "Archives"),
        ("demo_code.py", "Python_Files"),
        ("demo_page.html", "Code_Files"),
        ("demo_unknown.xyz", "Other_Files")
    ]

    files = []

    for filename, category in demo_files:

        files.append({
            "name": filename,
            "category": category,
            "data": (
                f"Demo file created for CodeAlpha Task 3\n"
                f"File: {filename}\n"
                f"Category: {category}\n"
            ).encode()
        })

    return files


# ============================================================
# UPLOAD FILES
# ============================================================

st.header("📤 Upload Your Files")

uploaded_files = st.file_uploader(
    "Choose files to automate",
    accept_multiple_files=True
)


# ============================================================
# DEMO BUTTON
# ============================================================

st.header("🧪 Demo Mode")

st.write(
    "Don't have files on your laptop? "
    "No problem! Generate sample files automatically."
)

demo_button = st.button(
    "🧪 Generate Demo Files",
    use_container_width=True
)


# ============================================================
# PREPARE FILE DATA
# ============================================================

file_data = []


if uploaded_files:

    for uploaded_file in uploaded_files:

        extension = Path(
            uploaded_file.name
        ).suffix.lower()

        file_data.append({
            "name": uploaded_file.name,
            "category": get_category(extension),
            "data": uploaded_file.getvalue()
        })


elif demo_button:

    file_data = create_demo_files()

    st.session_state["demo_files"] = file_data


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

    col1, col2, col3 = st.columns(3)

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
        st.metric(
            "🤖 Status",
            "Ready"
        )


    # ========================================================
    # CATEGORY STATISTICS
    # ========================================================

    st.subheader("📈 Category Summary")

    cols = st.columns(4)

    for index, (category, count) in enumerate(
        sorted(statistics.items())
    ):

        with cols[index % 4]:

            st.metric(
                category,
                count
            )


    # ========================================================
    # PREVIEW
    # ========================================================

    st.header("🔍 Automation Preview")

    preview = []

    for file in file_data:

        preview.append({
            "📄 File Name": file["name"],
            "📁 Destination": file["category"]
        })

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

        st.markdown(
            f"### 📁 {category}"
        )

        for file in file_data:

            if file["category"] == category:

                st.write(
                    f"📄 {file['name']}"
                )


    # ========================================================
    # ZIP CREATION
    # ========================================================

    def create_zip(files):

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(
            zip_buffer,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zip_file:

            used_names = set()

            for file in files:

                category = file["category"]
                filename = file["name"]

                original = filename
                counter = 1

                path = f"{category}/{filename}"

                while path in used_names:

                    stem = Path(original).stem
                    suffix = Path(original).suffix

                    filename = (
                        f"{stem}_{counter}{suffix}"
                    )

                    path = (
                        f"{category}/{filename}"
                    )

                    counter += 1

                used_names.add(path)

                zip_file.writestr(
                    path,
                    file["data"]
                )

        zip_buffer.seek(0)

        return zip_buffer


    # ========================================================
    # ORGANIZE BUTTON
    # ========================================================

    st.header("🚀 Run Automation")

    if st.button(
        "🚀 ORGANIZE ALL FILES",
        use_container_width=True,
        type="primary"
    ):

        zip_data = create_zip(file_data)

        st.success(
            "🎉 Automation completed successfully!"
        )

        st.balloons()

        st.download_button(
            label="📥 Download Organized ZIP",
            data=zip_data,
            file_name="Tehmina_CodeAlpha_Task3.zip",
            mime="application/zip",
            use_container_width=True
        )


# ============================================================
# HOW IT WORKS
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
            "Upload your own files."
        )

    with col2:

        st.subheader("2️⃣ Analyze")

        st.write(
            "The application detects file types automatically."
        )

    with col3:

        st.subheader("3️⃣ Organize")

        st.write(
            "Files are placed into category folders."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:20px">

    🤖 <strong>CodeAlpha Internship — Task 3</strong><br>

    Task Automation with Python Scripts<br><br>

    👩‍💻 Created by <strong>Tehmina Anwar</strong>

    </div>
    """,
    unsafe_allow_html=True
)