from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.vector_store import add_documents_to_vectorstore, clear_vectorstore
from app.services.parser import parse_file
from app.services.embeddings import get_embedding

router = APIRouter()

@router.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)): 
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    # Clear old data before processing new batch
    clear_vectorstore()
    
    all_documents = []

    for file in files:
        content = await file.read()
        try:
            # Use your flexible parser that handles CSV, Excel, and PDF
            df = parse_file(file.filename, content)
            
            # Convert dataframe rows to strings
            for _, row in df.iterrows():
                doc_text = f"Source: {file.filename} | " + " | ".join(
                    [f"{col}: {row[col]}" for col in df.columns if row[col] is not None]
                )
                all_documents.append(doc_text)
        except Exception as e:
            print(f"Error processing {file.filename}: {e}")
            continue # Skip failed files but continue with others

    if not all_documents:
        raise HTTPException(status_code=400, detail="No readable data found in files")

    # Batch process embeddings
    embeddings = [get_embedding(doc) for doc in all_documents]
    add_documents_to_vectorstore(all_documents, embeddings)

    return {"message": f"Successfully processed {len(files)} files", "docs": len(all_documents)}