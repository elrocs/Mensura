# Use Python 3.11 as the base image  
FROM python:3.11  

# Set the working directory
WORKDIR /app  
COPY . .

# Copy dependencies and install them
RUN pip install --no-cache-dir -r requirements.txt  

RUN mkdir -p /app/data

# Expose the API port  
EXPOSE 5000  

# Run the API  
CMD ["python", "main.py"]  
