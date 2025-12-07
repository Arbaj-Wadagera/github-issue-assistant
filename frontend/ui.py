import streamlit as st
import requests

# Constants
API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Seedling Issue Assistant", layout="centered")

# Header
st.title("🌱 AI-Powered GitHub Issue Assistant")
st.markdown("Prioritize and summarize GitHub issues instantly.")

# Input Form
with st.form("issue_form"):
    col1, col2 = st.columns([3, 1])
    with col1:
        repo_url = st.text_input("GitHub Repo URL", value="https://github.com/facebook/react")
    with col2:
        issue_num = st.number_input("Issue #", min_value=1, value=1)
    
    submitted = st.form_submit_button("Analyze Issue")

if submitted:
    if not repo_url:
        st.error("Please provide a valid Repository URL.")
    else:
        # Prepare Payload
        payload = {
            "repo_url": repo_url,
            "issue_number": issue_num
        }

        with st.spinner("Fetching data and analyzing..."):
            try:
                # Call the Backend API
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # --- DISPLAY RESULTS ---
                    st.divider()
                    st.subheader(f"Analysis Results")
                    
                    # Summary Box
                    st.info(f"**Summary:** {data['summary']}")
                    
                    # Metrics Row
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Type", data['type'].title())
                    m2.metric("Priority", f"{data['priority_score']}/5")
                    m3.metric("Impact", "High" if data['priority_score'] > 3 else "Low")

                    # Detailed Justification
                    st.markdown("### 📝 Priority Justification")
                    st.write(data['priority_justification'])

                    # Potential Impact (Conditional Display)
                    if data.get('potential_impact'):
                        st.markdown("### ⚠️ Potential User Impact")
                        st.warning(data['potential_impact'])

                    # Tags
                    st.markdown("### 🏷️ Suggested Labels")
                    # Display labels as small pills/chips
                    labels_html = " ".join(
                        [f"<span style='background-color:#e0f2f1; color:#00695c; padding:4px 8px; border-radius:4px; margin-right:5px;'>{label}</span>" 
                         for label in data['suggested_labels']]
                    )
                    st.markdown(labels_html, unsafe_allow_html=True)

                    # JSON Expander (For debugging/transparency)
                    with st.expander("View Raw JSON Output"):
                        st.json(data)

                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the Backend API. Is it running?")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")