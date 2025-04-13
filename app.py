import streamlit as st
import rag_system as RS
import time

def main():
    # Page config for better appearance
    st.set_page_config(
        page_title="MediRAG - Clinical Question Answering",
        page_icon="🩺",
        layout="wide"
    )

    # Custom CSS for better styling with dark/light mode support
    st.markdown("""
    <style>
    .main-header {
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 0;
        color: var(--text-color, #2c3e50);
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        color: var(--text-color, #7f8c8d);
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        width: 100%;
    }
    .response-box {
        background-color: rgba(248, 249, 250, 0.1);
        border-radius: 10px;
        padding: 20px;
        border-left: 5px solid #3498db;
    }
    .footnote {
        text-align: center;
        font-size: 0.8rem;
        color: var(--text-color, #95a5a6);
        margin-top: 3rem;
    }
    /* Ensure text is visible in both light and dark modes */
    p, h1, h2, h3, h4, h5, h6, li, span {
        color: var(--text-color, black);
    }
    /* Detect and adapt to dark mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --text-color: white;
        }
    }
    @media (prefers-color-scheme: light) {
        :root {
            --text-color: black;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Application header with medical emojis
    st.markdown("<h1 class='main-header'>🩺 MediRAG 💊</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Advanced Clinical Knowledge Assistant</p>", unsafe_allow_html=True)

    # Create two columns for better layout
    col1, col2 = st.columns([1, 3])

    # Sidebar with information
    with col1:
        # Use a visible icon instead of image to avoid display issues
        st.markdown("# 🏥")
        st.markdown("### How it works")
        st.markdown("""
        MediRAG uses advanced retrieval-augmented generation (RAG) technology to:
        
        1. 🔍 Search through trusted medical databases
        2. 📚 Find relevant clinical information
        3. 🧪 Generate accurate, evidence-based answers
        """)
        
        with st.expander("⚠️ Medical Disclaimer"):
            st.write("""
            This tool is designed to provide information based on medical literature. 
            It should not replace professional medical advice. Always consult with a 
            qualified healthcare provider for diagnosis and treatment.
            """)
            
        with st.expander("💉 Search Tips"):
            st.write("""
            - Be specific with your clinical questions
            - Include relevant patient details when appropriate
            - Specify if you need treatment options, diagnostic criteria, etc.
            - Try reformulating your question if the answer isn't helpful
            """)

    # Main content area
    with col2:
        st.markdown("### 👨‍⚕️ Ask Your Clinical Question")
        
        # Text input for user query with placeholder
        query = st.text_area(
            "Enter your clinical question:",
            placeholder="Example: What are the latest treatment guidelines for community-acquired pneumonia in elderly patients?",
            height=100
        )
        
        # Search button
        if st.button("🔬 Search Medical Knowledge Base"):
            if query:
                # Progress indication
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulated search process with visual feedback
                stages = [
                    "🧬 Analyzing query...",
                    "🔍 Searching medical databases...",
                    "📋 Retrieving relevant documents...",
                    "🧠 Generating evidence-based response..."
                ]
                
                for i, stage in enumerate(stages):
                    status_text.text(stage)
                    progress_bar.progress((i+1)/len(stages))
                    time.sleep(0.5)  # Simulated delay for visual effect
                
                # Get the actual response from the RAG system
                response = RS.answer_clinical_query(query)
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Display the answer in a nicely formatted box
                st.markdown("### 💡 Clinical Answer")
                st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
                
                # Add references section
                st.markdown("### 📚 References")
                st.info("MediRAG bases its answers on current medical literature and clinical guidelines. Specific references for this query are listed below when available.")
                # Example references - replace with actual references if your system provides them
                st.markdown("1. *Reference information would be displayed here if available from your RAG system*")
                
                # Add feedback mechanism
                col_feedback1, col_feedback2 = st.columns(2)
                with col_feedback1:
                    st.button("👍 This was helpful")
                with col_feedback2:
                    st.button("👎 Needs improvement")
            else:
                st.error("⚠️ Please enter a clinical question to proceed.")
    
    # Footer with ashcodes credit
    st.markdown("<p class='footnote'>MediRAG is designed to assist medical professionals with evidence-based information. Developed by ashcodes. Last updated: April 2025</p>", unsafe_allow_html=True)

    # Add theme detection and adjustment to runtime
    st.markdown("""
    <script>
    function detectColorScheme() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
        }
    }
    detectColorScheme();
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', detectColorScheme);
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()