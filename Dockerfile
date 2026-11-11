# Start with a lightweight Python Linux environment
FROM python:3.14-slim

# Create a folder inside the container
WORKDIR /app

# Copy your parts list into the container
COPY requirements.txt .

# Install the tools inside the container (no .venv needed here!)
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual monitor script into the container
COPY monitor.py .

# Tell the container what command to run when it starts
CMD ["python", "monitor.py"]