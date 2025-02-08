# Use Python 3.11 as the base image  
FROM python:3.11  

# Set the working directory  
WORKDIR /app  

# Copy dependencies and install them  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the application code  
COPY src/ app/src/

# Expose the API port  
EXPOSE 5000  

# Run the API  
CMD ["python", "src/main.py"]  
