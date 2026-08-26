<div align="center">

# 🤖 FILE AUTOMATION

### ⚡ Smart File Organization with Python

**CodeAlpha Internship — Task 3**

<p>
  <b>Task Automation with Python Scripts</b>
</p>

<p>
  👩‍💻 <b>Created by Tehmina Anwar</b>
</p>

<br>

<a href="https://codealphatask3fileautomation-vltnvnzsnolsdxwyeztu3a.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Click%20Here-success?style=for-the-badge" alt="Live Demo">
</a>

<a href="https://github.com/Tehminaanwar543">
  <img src="https://img.shields.io/badge/GitHub-Tehminaanwar543-black?style=for-the-badge&logo=github" alt="GitHub">
</a>

</div>

---

## 🌟 Project Overview

**FILE AUTOMATION** is a smart Python-based automation tool that organizes files automatically according to their file extensions.

Instead of manually sorting hundreds of files, users can simply upload multiple files and let the application detect, categorize, and organize them automatically.

The application provides a clean and interactive **Streamlit dashboard** with file statistics, automation preview, category summaries, demo mode, and downloadable ZIP packages.

---

## 🚀 Live Application

<div align="center">

### 🎯 Try It Now

<a href="https://codealphatask3fileautomation-vltnvnzsnolsdxwyeztu3a.streamlit.app/">

<img src="https://img.shields.io/badge/OPEN%20FILE%20AUTOMATION-🚀%20LIVE%20APP-blue?style=for-the-badge" alt="Live Application">

</a>

</div>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 📤 File Upload

Upload one or multiple files at once.

### 🤖 Auto Detection

Automatically detects file types using extensions.

### 📂 Smart Organization

Files are automatically assigned to the correct category.

### 📊 File Statistics

View total files, categories, and category-wise counts.

</td>

<td width="50%">

### 🔍 Automation Preview

Preview where every file will be organized.

### 🧪 Demo Mode

Generate sample files without uploading your own files.

### 📦 ZIP Generation

Download all organized files as a ZIP package.

### 📋 Automation Report

Generate and download a detailed text report.

</td>
</tr>
</table>

---

## 🗂️ Supported File Types

| 📁 Category        | 🔗 Extensions                               |
| ------------------ | ------------------------------------------- |
| 🖼️ **Images**     | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG, TIFF   |
| 📄 **Documents**   | DOC, DOCX, TXT, RTF, ODT                    |
| 📕 **PDF Files**   | PDF                                         |
| 📊 **Excel Files** | XLS, XLSX, CSV                              |
| 📽️ **PowerPoint** | PPT, PPTX                                   |
| 🎵 **Audio**       | MP3, WAV, AAC, FLAC, OGG, M4A               |
| 🎬 **Video**       | MP4, AVI, MKV, MOV, WMV, FLV, WEBM          |
| 📦 **Archives**    | ZIP, RAR, 7Z, TAR, GZ                       |
| 🐍 **Python**      | PY                                          |
| 💻 **Code**        | HTML, CSS, JS, JAVA, CPP, C, JSON, XML, SQL |
| 📁 **Other**       | Unknown file extensions                     |

---

## 🔄 How It Works

```text
          📤 UPLOAD FILES
                 │
                 ▼
        🔍 DETECT FILE TYPE
                 │
                 ▼
       🤖 ANALYZE EXTENSION
                 │
                 ▼
        📂 SELECT CATEGORY
                 │
                 ▼
        📊 SHOW PREVIEW
                 │
                 ▼
        🚀 RUN AUTOMATION
                 │
                 ▼
        📦 CREATE ZIP FILE
                 │
                 ▼
          📥 DOWNLOAD
```

---

## 🧪 Demo Mode

Don't have files available?

No problem! 😎

The application includes a built-in **Demo Mode** that creates sample files from different categories.

Click:

**🧪 Generate Demo Files**

The application will generate sample files such as:

```text
demo_photo.jpg
demo_image.png
demo_document.txt
demo_resume.docx
demo_report.pdf
demo_data.csv
demo_sheet.xlsx
demo_presentation.pptx
demo_song.mp3
demo_video.mp4
demo_archive.zip
demo_code.py
demo_page.html
demo_unknown.xyz
```

These files can then be analyzed and organized automatically.

---

## 📊 Dashboard

The application provides useful statistics after files are uploaded.

### 📦 Total Files

Shows the total number of uploaded files.

### 📁 Categories

Shows how many different file categories were detected.

### 🖼️ Images

Displays the total number of image files.

### 🤖 Automation Status

Shows whether files are ready to be organized.

---

## 🔍 Automation Preview

Before organizing the files, the application displays a preview like:

```text
┌────────────────────────┬──────────────────────┐
│ 📄 File Name           │ 📁 Destination       │
├────────────────────────┼──────────────────────┤
│ photo.jpg              │ 🖼️ Images            │
│ resume.docx            │ 📄 Documents         │
│ report.pdf             │ 📕 PDF_Files         │
│ data.xlsx              │ 📊 Excel_Files       │
│ song.mp3               │ 🎵 Audio_Files       │
│ video.mp4              │ 🎬 Video_Files       │
│ script.py              │ 🐍 Python_Files      │
└────────────────────────┴──────────────────────┘
```

---

## 📂 Organized Folder Structure

After automation, files are placed into category-based folders:

```text
📦 Organized_Files
│
├── 🖼️ Images
│   ├── photo.jpg
│   └── image.png
│
├── 📄 Documents
│   ├── resume.docx
│   └── notes.txt
│
├── 📕 PDF_Files
│   └── report.pdf
│
├── 📊 Excel_Files
│   └── data.xlsx
│
├── 📽️ PowerPoint_Files
│   └── presentation.pptx
│
├── 🎵 Audio_Files
│   └── song.mp3
│
├── 🎬 Video_Files
│   └── video.mp4
│
├── 📦 Archives
│   └── backup.zip
│
├── 🐍 Python_Files
│   └── script.py
│
├── 💻 Code_Files
│   └── index.html
│
└── 📁 Other_Files
    └── unknown.xyz
```

---

## 🛡️ Duplicate File Protection

The application intelligently handles duplicate filenames.

For example:

```text
Documents/

resume.docx
resume_1.docx
resume_2.docx
```

This prevents files from being overwritten when creating the organized ZIP package.

---

## 📋 Automation Report

After processing, users can download a detailed report containing:

```text
CODEALPHA INTERNSHIP - TASK 3
TASK AUTOMATION WITH PYTHON SCRIPTS

Created by: Tehmina Anwar

Total Files: 14
Categories: 10

FILE ORGANIZATION
----------------------------------------

photo.jpg -> Images
resume.docx -> Documents
report.pdf -> PDF_Files
data.xlsx -> Excel_Files
song.mp3 -> Audio_Files
script.py -> Python_Files

CATEGORY SUMMARY
----------------------------------------

Images: 2
Documents: 2
PDF_Files: 1
Excel_Files: 2
```

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/Pathlib-Python-blue?style=for-the-badge">

<img src="https://img.shields.io/badge/Zipfile-Python-orange?style=for-the-badge">

</div>

---

## 📦 Python Libraries

This project uses:

```text
streamlit
pathlib
collections
zipfile
io
```

Most file-processing functionality is powered by Python's built-in libraries.

---

## 📁 Project Structure

```text
📦 CodeAlpha_Task3_File_Automation
│
├── 📄 app.py
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Tehminaanwar543/CodeAlpha_Task3_File_Automation.git
```

### 2️⃣ Open Project

```bash
cd CodeAlpha_Task3_File_Automation
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit

```bash
streamlit run app.py
```

---

## 📄 requirements.txt

```text
streamlit
```

---

## 🎯 CodeAlpha Internship

This project was developed as part of the:

<div align="center">

### 💻 CodeAlpha Python Programming Internship

**Task 3 — Task Automation with Python Scripts**

</div>

The project demonstrates how Python can automate repetitive file-management tasks and provide users with a simple graphical interface through Streamlit.

---

## 👩‍💻 Developer

<div align="center">

# Tehmina Anwar

### AI/ML Engineer | Python Developer | Generative AI Enthusiast

Building intelligent applications using:

**Python • Machine Learning • Deep Learning • Generative AI • LLMs • NLP • Computer Vision • Streamlit**

</div>

---

## 🌐 Connect With Me

<div align="center">

<a href="https://github.com/Tehminaanwar543">
<img src="https://img.shields.io/badge/GitHub-Tehminaanwar543-181717?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/in/tehmina-anwar-77b8a8414">
<img src="https://img.shields.io/badge/LinkedIn-Tehmina%20Anwar-0A66C2?style=for-the-badge&logo=linkedin">
</a>

<a href="https://tehmina-portfolio-five.vercel.app/">
<img src="https://img.shields.io/badge/Portfolio-Visit%20Website-purple?style=for-the-badge&logo=vercel">
</a>

</div>

---

## ⭐ Project Highlights

<div align="center">

| Feature                 | Status |
| ----------------------- | ------ |
| 📤 Multiple File Upload | ✅      |
| 🤖 Automatic Detection  | ✅      |
| 📂 Smart Categorization | ✅      |
| 📊 File Statistics      | ✅      |
| 🔍 Automation Preview   | ✅      |
| 🧪 Demo Mode            | ✅      |
| 📦 ZIP Generation       | ✅      |
| 🛡️ Duplicate Handling  | ✅      |
| 📋 Report Generation    | ✅      |
| 🚀 Streamlit Deployment | ✅      |

</div>

---

<div align="center">

### 🤖 Automate. Organize. Simplify.

**Made with ❤️ using Python & Streamlit**

### ⭐ If you like this project, don't forget to star the repository!

</div>
