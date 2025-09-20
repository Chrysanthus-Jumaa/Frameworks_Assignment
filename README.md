# 📘 CORD-19 Metadata Explorer

An interactive Streamlit dashboard for exploring publication trends, journal distributions, and title-based word clouds from the CORD-19 metadata dataset. Built with reproducible workflows, modular design, and a focus on clarity and interactivity.

---

## 🧠 Project Overview

This dashboard provides a clean interface to analyze the CORD-19 metadata, enabling users to:

- 📈 Visualize publication trends over time  
- 📚 Identify top journals by publication count  
- 🏛️ Explore source distributions (e.g., PMC, bioRxiv)  
- 🌥️ Generate word clouds from paper titles  

All visualizations are filter-aware and can be customized by year, source, and journal.

---

## 📦 Dataset

The original CORD-19 metadata file is large and exceeds GitHub’s upload limits. Therefore, the cleaned dataset is hosted externally.

🔗 **Download the dataset from Google Drive**  
👉 [CORD-19 Metadata ZIP (Google Drive)](https://drive.google.com/file/d/1LMJYLvYogQV-JF8AWDizuFARIL-xBHBy/view?usp=sharing)

> Once downloaded, extract the contents and place `cord19_cleaned.csv` in the root directory of this project.

---

## 🚀 Getting Started

### 1. Clone the Repository
bash
git clone https://github.com/Chrysanthus-Jumaa/Frameworks_Assignment.git
cd <repo folder>

### 2. Install Dependencies  
bash

bash  
pip install -r requirements.txt

### 3. Run the App  
bash

bash  
streamlit run app.py

### 📁 File Structure  
Code

text  
cord19-metadata-explorer/  
│  
├── app.py                  # Main Streamlit dashboard  
├── cord19_cleaned.csv      # Cleaned dataset (after extraction)  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation

### 📋 Requirements  
text

Code  
streamlit  
pandas  
matplotlib  
wordcloud

You can install them manually with: bash

bash  
pip install streamlit pandas matplotlib wordcloud  
Or use the requirements.txt file provided.

### 🧪 Notes on Data Cleaning  
Extracted publish_year from publish_time using pd.to_datetime  
Removed nulls and duplicates  
Standardized journal and source names  
Exported final dataset with index=False to avoid extra columns  
Saved as cord19_cleaned.csv for use in the dashboard

### 🧠 Built With  
Streamlit — for interactive dashboards  
Pandas — for data manipulation  
Matplotlib — for custom visualizations  
WordCloud — for title-based summaries

### 👤 Author  
Chrysanthus Jumaa - Analytical, detail-oriented, and passionate about reproducible data science workflows. Built this dashboard to explore metadata-rich datasets with clarity and creativity.

### 📜 License  
This project is licensed under the MIT License — feel free to use, modify, and share.

### 🗂️ Acknowledgments  
The CORD-19 dataset by Semantic Scholar  
Streamlit community for dashboard inspiration  
Matplotlib and WordCloud contributors for visualization tools
