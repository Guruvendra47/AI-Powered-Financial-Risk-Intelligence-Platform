# Retrieval-Augmented Generation (RAG) Layer

## Overview

The Retrieval-Augmented Generation (RAG) layer enables users to query financial regulations, compliance documents, and risk reports using natural language.

Instead of relying solely on Large Language Models (LLMs), the platform retrieves relevant document context from a vector database and supplies that context to the LLM before generating a response.

This approach improves accuracy, reduces hallucinations, and ensures responses are grounded in actual financial and regulatory documents.

---

# Architecture

```text
PDF Documents
(Regulations, Compliance Guides, Risk Reports)
                    │
                    ▼
load_documents.py
                    │
                    ▼
chunk_documents.py
                    │
                    ▼
create_embeddings.py
                    │
                    ▼
OpenAI Embeddings
                    │
                    ▼
ChromaDB Vector Store
                    │
                    ▼
retriever.py
                    │
                    ▼
rag_chain.py
                    │
                    ▼
OpenAI LLM
                    │
                    ▼
AI Response
```

---

# Project Structure

```text
src/
└── rag/
    │
    ├── load_documents.py
    ├── chunk_documents.py
    ├── create_embeddings.py
    ├── retriever.py
    ├── rag_chain.py
    │
    ├── tests/
    │   ├── 1_test_load_documents.py
    │   ├── 2_test_chunk_documents.py
    │   ├── 3_test_create_embeddings.py
    │   ├── 4_test_retriever.py
    │   └── 5_test_rag_chain.py
    │
    └── README.md
```

---

# Documents Used

The RAG system processes financial and compliance documentation.

Location:

```text
src/data/ai_documents/
```

---

## Compliance Documents

```text
compliance_01_third_party_risk_management_guide.pdf

compliance_02_bsa_aml_procedures.pdf

compliance_03_third_party_relationships_guidance.pdf
```

---

## Regulatory Documents

```text
regulations_01_compliance_management_systems.pdf

regulations_02_regulatory_reporting.pdf

regulations_03_review_of_regulatory_reports.pdf
```

---

## Risk Reports

```text
risk_reports_01_fdic_2024_risk_review.pdf

risk_reports_02_fdic_2025_risk_review.pdf

risk_reports_03_fdic_2026_risk_review.pdf
```

---

# Step 1: Document Loading

File:

```text
load_documents.py
```

Purpose:

Loads PDF documents into memory for processing.

Responsibilities:

```text
Read PDF files

Extract text

Prepare documents for chunking
```

---

# Step 2: Document Chunking

File:

```text
chunk_documents.py
```

Purpose:

Breaks large documents into smaller chunks.

Why?

LLMs and vector databases perform better when working with smaller text segments.

Example:

```text
100-page regulation
        │
        ▼
500 smaller chunks
```

Benefits:

```text
Improved retrieval accuracy

Faster search

Better context matching
```

---

# Step 3: Embedding Generation

File:

```text
create_embeddings.py
```

Purpose:

Converts text chunks into numerical vector representations.

Technology:

```text
OpenAI Embeddings
```

Workflow:

```text
Text Chunk
      │
      ▼
Embedding Model
      │
      ▼
Vector Representation
```

---

# Step 4: Vector Storage

Technology:

```text
ChromaDB
```

Purpose:

Stores embeddings for semantic search.

Capabilities:

```text
Vector Search

Similarity Matching

Context Retrieval
```

---

# Step 5: Retrieval

File:

```text
retriever.py
```

Purpose:

Finds the most relevant document chunks based on a user query.

Example Query:

```text
What are the requirements for third-party risk management?
```

Retriever Output:

```text
Top Matching Chunks

Compliance Guidance

Risk Management Sections
```

---

# Step 6: RAG Chain

File:

```text
rag_chain.py
```

Purpose:

Combines retrieved document context with the user query.

Workflow:

```text
User Question
        │
        ▼
Retriever
        │
        ▼
Relevant Context
        │
        ▼
OpenAI LLM
        │
        ▼
Final Response
```

---

# Example Query

User Question:

```text
What controls should banks implement for third-party vendors?
```

Retrieved Context:

```text
Third-party risk management guidance

Vendor due diligence requirements

Monitoring recommendations
```

Generated Response:

```text
Banks should implement vendor due diligence,
risk assessments, ongoing monitoring,
and compliance reviews for third-party providers.
```

---

# OpenAI Integration

Used For:

```text
Embedding Generation

Question Answering

Contextual Response Generation
```

Required Environment Variable:

```text
OPENAI_API_KEY
```

---

# ChromaDB Integration

Purpose:

Stores vector embeddings and supports semantic search.

Benefits:

```text
Fast Retrieval

Semantic Similarity Search

Scalable Vector Storage
```

---

# Testing

Location:

```text
src/rag/tests
```

Files:

```text
1_test_load_documents.py

2_test_chunk_documents.py

3_test_create_embeddings.py

4_test_retriever.py

5_test_rag_chain.py
```

Testing Areas:

```text
Document Loading

Chunking

Embedding Creation

Retriever Accuracy

RAG Pipeline Execution
```

---

# End-to-End Workflow

```text
Load Documents
        │
        ▼
Chunk Documents
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
User Query
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
OpenAI LLM
        │
        ▼
Answer Generated
```

---

# Business Value

The RAG layer enables financial analysts, compliance teams, and risk managers to query regulatory documents using natural language.

Benefits:

* Faster research
* Reduced manual document review
* Improved compliance analysis
* More accurate AI responses
* Context-aware financial risk insights
* Reduced hallucinations from LLMs

---

# Skills Demonstrated

```text
Retrieval-Augmented Generation (RAG)

LangChain

ChromaDB

Vector Databases

Embeddings

Semantic Search

OpenAI API

Prompt Engineering

Document Processing

Financial Compliance Analytics

Python

Generative AI
```

