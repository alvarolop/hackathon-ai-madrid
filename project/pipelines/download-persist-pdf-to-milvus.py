from kfp import dsl

def get_file_name_from_url(url):
    from urllib.parse import urlparse
    # Parse the URL to extract the path
    parsed_url = urlparse(url)
    # Extract the file name from the path
    file_name = parsed_url.path.split('/')[-1]
    return file_name

def get_metadata_from_filename(filename):
    metadata = filename.split("-")
    return {
        "product_name": metadata[0],
        "version": metadata[2],
        "section": metadata[3],
        "language": metadata[4]
    }

@dsl.component(packages_to_install=['pymilvus'],
               pip_index_urls=['http://pypi.org/simple'])
def create_milvus_client(milvus_endpoint, user, password):
    return MilvusClient(milvus_endpoint, user=user, password=password)


@dsl.component(packages_to_install=['pymilvus'],
               pip_index_urls=['http://pypi.org/simple'])
def create_milvus_collection(client, collection_name = "openshift_ai_documentation"):
    # Delete collection if the collection exists
    if client.has_collection(collection_name=collection_name):
        print("going to delete ", collection_name)
        client.drop_collection(collection_name=collection_name)
    # Create collection
    print("Creating Collection ", collection_name)
    client.create_collection(
        collection_name=collection_name,
        dimension=768,  # The vectors we will use in this demo has 768 dimensions
    )

@dsl.component(packages_to_install=['urlparse', 'docling'],
               pip_index_urls=['http://pypi.org/simple'])
def download_pdf(URL):
    from docling.document_converter import DocumentConverter

    chunker = HybridChunker(tokenizer="BAAI/bge-small-en-v1.5")
    converter = DocumentConverter()
    ## Retrieve metadata from one file
    metadata = get_metadata_from_filename(get_file_name_from_url(URL))
    print(f"Handling file with metadata: {metadata}")
    ## Parse document from source chunk it
    converted_source_file = converter.convert(URL)
    return converted_source_file.document, metadata

@dsl.component(packages_to_install=['pymilvus', 'docling', 'pymilvus[model]'],
               pip_index_urls=['http://pypi.org/simple'])
def create_vectors(document):
    from docling.chunking import HybridChunker
    import docling.model

    embedding_fn = model.DefaultEmbeddingFunction()

    chunk_iter = chunker.chunk(document)
    ## Create chunk_list with the parts of the document
    chunk_list = list(chunk_iter)
    chunk_vectors = embedding_fn.encode_documents([chunk.text for chunk in chunk_list])
    vectors = []
    for i, chunk in enumerate(chunk_list):
        vectors.append({
            # to avoid overriding the same id, hash the product_name
            "id": int(str(file_index * 100) + str(i)),
            "product_name": metadata.get("product_name", "null"),
            "version": metadata.get("version", "null"),
            "section": metadata.get("section", "null"),
            "language": metadata.get("language", "null"),
            "vector": chunk_vectors[i] ,
            "text": chunk.text,
        })
    return vectors

@dsl.component
def persist_vectors_on_milvus(name: str) -> str:
    pass


@dsl.pipeline
def download_persist_pdf_to_milvus_pipeline(document_url):
    client = create_milvus_client("http://vectordb-milvus.milvus.svc.cluster.local:19530", "root", "Milvus")
    create_milvus_collection(client)

    #full_url = "https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/2.16/pdf/monitoring_data_science_models/Red_Hat_OpenShift_AI_Self-Managed-2.16-Monitoring_data_science_models-en-US.pdf"
    #base_url="https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/2.16/pdf/"
    #document_url = base_url + "monitoring_data_science_models/Red_Hat_OpenShift_AI_Self-Managed-2.16-Monitoring_data_science_models-en-US.pdf"

    # add for loop to support multiple PDFs
    document, metadata = download_pdf(document_url)
    vectors = create_vectors(document, metadata)

    #

if __name__ == "__main__":
    from kfp import compiler
    compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')