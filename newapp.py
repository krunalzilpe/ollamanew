import streamlit as st
import tempfile
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="C++ Text Retrieval", page_icon="📘")

st.title("📘 C++ Document Assistant")
st.write("Upload a text file and ask questions about it.")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Load document
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_documents = splitter.split_documents(documents)

    # Embeddings
    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Create FAISS database
    db = FAISS.from_documents(final_documents, embedding)

    st.success("Document processed successfully!")

    # User Query
    query = st.text_input("Ask a question about the uploaded document")

    if query:
        docs = db.similarity_search(query, k=3)

        st.subheader("Relevant Chunks")

        for i, doc in enumerate(docs, start=1):
            st.markdown(f"### Result {i}")
            st.write(doc.page_content)
            st.divider()