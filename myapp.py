import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("cord19_cleaned.csv")

df = load_data()

# ─────────────────────────────────────────────────────────────
# 🧠 Header
st.title("CORD-19 Metadata Explorer")
st.markdown("An interactive dashboard of publication trends, sources, and journal insights.")

# ─────────────────────────────────────────────────────────────
# 🧰 Sidebar Filters
st.sidebar.header("Filter Options")
selected_year = st.sidebar.selectbox("Select Year", sorted(df['publish_year'].dropna().unique()))
selected_sources = st.sidebar.multiselect("Select Source(s)", sorted(df['source_x'].dropna().unique()))
selected_journals = st.sidebar.multiselect("Select Journal(s)", sorted(df['journal'].dropna().unique()))

# Apply filters
filtered_df = df[df['publish_year'] == selected_year]
if selected_sources:
    filtered_df = filtered_df[filtered_df['source_x'].isin(selected_sources)]
if selected_journals:
    filtered_df = filtered_df[filtered_df['journal'].isin(selected_journals)]

# ─────────────────────────────────────────────────────────────
# 📊 Main Dashboard Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Publication Trends", "📚 Top Journals", "🏛️ Source Distribution", "🌥️ Word Cloud"])

# ── Tab 1: Publication Trends
with tab1:
    st.subheader("Publications Over Time")
    year_counts = df['publish_year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.plot(year_counts.index, year_counts.values, marker='o', color='teal')
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")
    ax.set_title("Publication Volume by Year")
    ax.grid(True)
    st.pyplot(fig)

# ── Tab 2: Top Journals
with tab2:
    st.subheader("Top 20 Journals")

    # Toggle between filtered and full dataset
    show_filtered = st.checkbox("Show filtered journals only", value=False)

    # Choose dataset based on toggle
    journal_data = filtered_df if show_filtered else df

    # Count and display top journals
    journal_counts = journal_data['journal'].value_counts().head(20)

    if journal_counts.empty:
        st.warning("No journal data available for the selected filters.")
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        journal_counts.plot(kind='bar', color='darkcyan', ax=ax)
        ax.set_title("Top 20 Journals by Publication Count")
        ax.set_xlabel("Journal")
        ax.set_ylabel("Number of Publications")
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y')
        st.pyplot(fig)


# ── Tab 3: Source Distribution
with tab3:
    st.subheader("Distribution by Source")

    # Toggle between filtered and full dataset
    show_filtered_sources = st.checkbox("Show filtered sources only", value=False)

    # Choose dataset based on toggle
    source_data = filtered_df if show_filtered_sources else df

    # Count and display source distribution
    source_counts = source_data['source_x'].value_counts()

    if source_counts.empty:
        st.warning("No source data available for the selected filters.")
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        source_counts.plot(kind='bar', color='indigo', ax=ax)
        ax.set_title("Distribution of Papers by Source")
        ax.set_xlabel("Source")
        ax.set_ylabel("Number of Publications")
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y')
        st.pyplot(fig)


# ── Tab 4: Word Cloud
with tab4:
    st.subheader("Word Cloud of Paper Titles")

    # Toggle between filtered and full dataset
    show_filtered_titles = st.checkbox("Use filtered titles only", value=True)

    # Choose dataset based on toggle
    title_data = filtered_df if show_filtered_titles else df

    # Combine titles into one string
    title_text = ' '.join(title_data['title'].dropna().astype(str).tolist())

    if not title_text.strip():
        st.warning("No titles available to generate a word cloud for the selected filters.")
    else:
        # Optional stopword toggle
        remove_stopwords = st.checkbox("Remove common stopwords", value=True)
        stopwords = None
        if remove_stopwords:
            from wordcloud import STOPWORDS
            stopwords = STOPWORDS

        # Generate word cloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=stopwords,
            max_words=200
        ).generate(title_text)

        st.image(wordcloud.to_array(), use_column_width=True)


# ─────────────────────────────────────────────────────────────
# 📎 Footer
st.markdown("---")
st.markdown(f"**Total Records:** {len(df)}  |  **Distinct Journals:** {df['journal'].nunique()}  |  **Sources:** {df['source_x'].nunique()}")
st.markdown("Built by **Chrysanthus** with reproducible workflows and modular design.")
