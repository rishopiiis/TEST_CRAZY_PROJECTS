from haystack.nodes import FARMReader, BM25Retriever
from haystack.utils import fetch_archive_from_http
from haystack.pipelines import ExtractiveQAPipeline

# Load a pre-trained retriever and reader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
retriever = BM25Retriever()

# Load your documents into a Document Store (you can use a simple in-memory one)
from haystack.document_stores import InMemoryDocumentStore
document_store = InMemoryDocumentStore()

# Add documents (FAQ data) to the document store
document_store.write_documents(documents)

# Set up the pipeline
pipeline = ExtractiveQAPipeline(reader, retriever)
