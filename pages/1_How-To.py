import streamlit as st
from common.config import (
    # base_path,
    # document_list,
    # collection_list,
    collection,
    # setup_doc_selector,
    # display_summary,
    # download_pdf_button,
)


def main():
    st.set_page_config(page_title="How-to", page_icon="📖")

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

    # (
    #     collection_name,
    #     document_name,
    # ) = setup_doc_selector()
    # download_pdf_button(base_path, collection_name, document_name)
    # display_summary(document_name)

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

    st.header("Step 5: Review Source Documents")
    st.write(
        "The ultimate goal is for you to review the relevant sections of the source documents related to your question. Use the app's responses and retrievals to narrow down where to focus, but ensure you read and interpret the official documentation yourself."
    )


if __name__ == "__main__":
    main()
