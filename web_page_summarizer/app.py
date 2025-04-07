from advisory_modules.extractor import request
from advisory_modules.html_parser import parser
from advisory_modules.generate_response import generate_response
import streamlit.components.v1 as components
import streamlit as st


st.title("Home Page")

user_input = st.text_input("Enter your website link here.")





if st.button("Fetch URL"):
    response = request(user_input)

    text,title = parser(response)
    prompt = f"""You are an AI assistant that specializes in summarizing website content. I have extracted text content from a webpage using Python's Beautiful Soup library. The content is as follows: {text}
Please provide:
1. A concise summary of the content (3-4 sentences).
2. Any key insights or main points highlighted in the content.

If the content appears too vague, incomplete, or lacks structure, mention that and suggest improvements or next steps."""
    response = generate_response(prompt)
    # st.text_area("Prompt:", prompt, height=100)
    st.subheader("Response Text")

    # Display the text in an expandable area
    with st.expander("Expand Response Text"):
        st.text_area("Response Text", prompt, height=200)

    # Button to copy text
    st.download_button(
        label="Download prompt Text",
        data=prompt,
        file_name="response.txt",
        mime="text/plain",
    )
    with st.expander("Expand Response Text"):
        st.text_area("Response Text", response, height=200)

    # Button to copy text
    st.download_button(
        label="Download Response Text",
        data=response,
        file_name="response.txt",
        mime="text/plain",
    )

    # st.text_area("Response:", response, height=100)
