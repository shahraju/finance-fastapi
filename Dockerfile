# Use a lightweight Python image 
FROM python:3.10-slim 
 
# Set working directory 
WORKDIR /app 
 
# Install dependencies 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
 
# Copy all files 
COPY . . 
 
# Expose port 7860 for Hugging Face 
EXPOSE 7860 
 
# Run FastAPI with Uvicorn 
CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "7860"] 
