import streamlit as st
import requests

st.title("Perplexity-Inspired Answer Engine")

query = st.text_input("Enter your query:")
return_sources = st.checkbox("Return Sources", value=True)
return_follow_up = st.checkbox("Return Follow-up Questions", value=True)
embed_sources = st.checkbox("Embed Sources in LLM Response", value=False)

if st.button("Submit"):
    data = {
        "message": query,
        "returnSources": return_sources,
        "returnFollowUpQuestions": return_follow_up,
        "embedSourcesInLLMResponse": embed_sources,
        "textChunkSize": 800,
        "textChunkOverlap": 200,
        "numberOfSimilarityResults": 2,
        "numberOfPagesToScan": 4
    }
    response = requests.post("http://localhost:3005", json=data)
    result = response.json()

    st.header("Answer")
    st.write(result["answer"])

    if return_sources:
        st.header("Sources")
        for source_group in result["sources"]:
            for source in source_group:
                st.write(f"- [{source['title']}]({source['link']})")

    if return_follow_up:
        st.header("Follow-up Questions")
        for question in result["followUpQuestions"]:
            st.write(f"- {question}")