from typing import Optional, List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class QA(BaseModel):
    id: int
    name: str
    country: str

app = FastAPI()

qa_data = {}

@app.post("/qa", response_model=QA)
def create_qa(qa_item: QA):
    qa_data[qa_item.id] = qa_item
    return qa_item

@app.get("/qa/{qa_id}", response_model=QA)
def read_qa(qa_id: int):
    qa_item = qa_data.get(qa_id)
    if not qa_item:
        raise HTTPException(status_code=404, detail="QA not found")  # Return a 404 response with an error message
    return qa_item

@app.put("/qa/{qa_id}", response_model=QA)
def update_qa(qa_id: int, qa_update: QA):
    if qa_id not in qa_data:
           return {"error": "QA not found"}
    
    updated_qa = qa_data[qa_id]
    updated_qa.name = qa_update.name
    updated_qa.country = qa_update.country
    return updated_qa

@app.delete("/qa/{qa_id}", response_model=QA)
def delete_qa(qa_id: int):
    if qa_id not in qa_data:
        return {"error": "QA not found"}
    
    deleted_qa = qa_data.pop(qa_id)
    return deleted_qa


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
