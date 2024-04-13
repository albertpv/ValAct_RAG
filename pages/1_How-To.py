import streamlit as st
import os
import json

st.set_page_config(page_title="How-to", page_icon="📖")


# Define a function to scan a directory and return a dictionary of folders and files.

# Set variables
base_path = "./data/pdf"


@st.cache_data  # Add the caching decorator
def scan_directory(base_path):
    folders_files = {}
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            files = ["All"]
            for file in os.listdir(folder_path):
                # Exclude system files like .DS_Store
                if file != ".DS_Store":
                    files.append(file)
            files[1:] = sorted(files[1:])
            folders_files[folder] = files
    return folders_files


document_list = scan_directory(base_path)
collection_list = [
    "AI_BigData",
    "ASOP_life",
    "CFT",
    "PBR",
    "VM21",
    "VM22",
    "GAAP",
    "Asset",
    "Bermuda",
    "Cayman",
    "IFRS17",
    "RiskFinance",
    "Product",
]


@st.cache_data  # Add the caching decorator
def get_json(file_path):
    # Open and load the json file
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


summary_data = get_json("summary.json")

st.title("How to use the Q&A Machine")
st.write(
    "This web app allows you to ask questions related to actuarial documents, and receive answers generated by a language model augmented with relevant information retrieved from the documents."
)
st.write(
    "The model is developed to support and augment actuaries. Harness its power but with responsibility and accountability. The process focused on transparency and verifiability."
)

st.header("Step 1: Select a Collection of Actuarial Documents")
st.write(
    "The responses you receive may differ depending on the domain your question pertains to. Therefore, it's important to select which domain your question falls under."
)
st.write("Here is a list of available document collections:")
collection = [
    "AI_BigData",
    "ASOP_life",
    "CFT",
    "PBR (VM20 falls under PBR)",
    "VM21 (set as an independent collection to differentiate from VM20)",
    "VM22 (set as an independent collection due to evolving nature)",
    "GAAP",
    "Asset",
    "Bermuda",
    "Cayman",
    "IFRS17",
    "RiskFinance (Risk and finance including capital, reinsurance topics)",
    "Product",
]
st.write("- " + "\n- ".join(collection))

st.header("Step 2: Decide Whether to Ask About a Specific Document")
st.write(
    'Within a given domain, your question may be specific to a certain document. If so, please choose that document to get the most relevant response. However, if you are unsure, you can leave the selection as "All" and the retrieval process will find relevant chunks from all documents in the collection.'
)

st.subheader("Step 2a: Preview Document Summaries")
st.write(
    "You can choose to preview a summary of each document before making your selection. The app has generated AI-powered summaries that outline the main themes of each document. These summaries are meant to help you understand what each document covers, but you should still refer to the source documents for full details."
)
st.write("**Please see the sidebar to review the summaries of each document.**")

with st.sidebar:
    collection_name = st.selectbox(
        "Select your document collection",
        collection_list,
    )

    document_name = st.selectbox(
        "Select your document",
        document_list[collection_name],
    )

if document_name != "All":
    pdf_file_path = base_path + "/" + collection_name + "/" + document_name
    # Open the file in binary mode
    with open(pdf_file_path, "rb") as pdf_file:
        # Read the PDF file's binary data
        pdf_bytes = pdf_file.read()

        # Create the download button
        st.sidebar.download_button(
            label="Download selected document",
            data=pdf_bytes,
            file_name=document_name,
            mime="application/octet-stream",
            use_container_width=True,
        )
    summary = summary_data.get(document_name)
    with st.sidebar.expander("AI generated summary of the document", expanded=True):
        if summary:
            st.write(summary.get("summary", "Summary not available."))
        else:
            st.write(f"Summary of '{document_name}' not found in the file.")


st.header("Step 3: Ask Your Question")
st.write(
    "Phrase your question concisely and clearly. Your question does not need to be long. Spell out abbreviations. For example:"
)
examples = [
    "*Explain ASOP No. 14.*",
    "*Explain Bermuda Solvency Capital Requirement* is better than *Explain BSCR*",
]
for example in examples:
    st.write("- " + example)

st.subheader("Step 3a: Adjust RAG Parameters")
st.write(
    "You can adjust the following parameters to customize the retrieval and generation process:"
)
st.write(
    "- **Top N Sources to View**: Determines how many of the top retrieved sources/chunks to display in the interface. The search algorithm retrieves 20 chunks in total."
)
st.write(
    "- **Diversity Search**: Enabling this allows the retrieved sources to be more diverse, preventing repeated information that is very close to your initial query. This can be useful for getting a broader perspective."
)
st.write(
    "- **Output similarity score**: You may output similarity score between initial query and retrieved chunks. Allowing the score output may make the retrieval process slower."
)

st.subheader("Step 3b: Clear History")
st.write(
    "The chat history can influence the retrieval and language model's responses. If you are switching to a new document collection or changing topics, please clear the history to start fresh."
)

st.header("Step 4: Review Responses")
st.write(
    "Review the language model's response as well as the retrieved document chunks that the response is based on. Always verify the response against the source material - the language model's output should not replace your own actuarial judgment and interpretation."
)

st.header("Step 5: Download and Review Documents")
st.write(
    "The ultimate goal is for you to review the relevant sections of the source documents related to your question. Use the app's responses and retrievals to narrow down where to focus, but ensure you read and interpret the official documentation yourself."
)
