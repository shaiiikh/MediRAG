# MediRAG

## Medical Retrieval-Augmented Generation System

MediRAG is an advanced clinical decision support system that leverages retrieval-augmented generation to help healthcare professionals access evidence-based information quickly and efficiently.

## Overview

This system answers clinical queries by:
- Searching through trusted medical databases
- Finding relevant clinical information from the MIMIC-IV-Ext dataset
- Generating accurate, evidence-based answers with proper citations

## Features

- **Evidence-Based Responses**: All answers are grounded in medical literature
- **User-Friendly Interface**: Clean, intuitive design built with Streamlit
- **Transparent Reasoning**: Clear presentation of supporting evidence
- **Privacy-Conscious Design**: Maintains strict data privacy standards

## Technical Implementation

MediRAG combines BM25 and dense retrieval techniques with a fine-tuned LLM to provide contextually relevant answers to clinical questions. The interactive frontend allows healthcare professionals to quickly get the information they need during clinical decision-making.

## Project Structure

- `Diagnostic_kg/Diagnosis_flowchart/`: Clinical dataset for diagnosis flowcharts
- `faiss_index/`: Vector indices for semantic search
- `samples/Finished/`: Processed clinical dataset samples
- `Patient_data.py`: Processing patient PDFs/scanned documents using OCR
- `app.py`: Streamlit UI implementation
- `check.py`: Test script for Google's Gemini 2.0 Flash model
- `hf_login.py`: Hugging Face login integration
- `rag_assignment.ipynb`: Source notebook for implementation
- `rag_system.py`: Core RAG system implementation

## Installation

```
git clone https://github.com/username/MediRAG.git
cd MediRAG
pip install -r requirements.txt
```

## Usage

```
streamlit run app.py
```

## Why This Matters

In healthcare, having the right information at the right time can significantly impact patient outcomes. MediRAG aims to reduce information overload and support evidence-based practice by providing quick access to relevant clinical knowledge.

## License

See LICENSE file for details.
