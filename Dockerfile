# Stage 1: Build stage
FROM python:3.10-slim AS builder

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/python /usr/local/bin/python
COPY --from=builder /usr/local/bin/pip /usr/local/bin/pip

# Copy the requirements file again
COPY requirements.txt .

# Copy the bot.py file from the host to the container
COPY bot.py .

# Create the logs directory
RUN mkdir -p /usr/src/app/logs

# Command to run the bot
CMD ["python", "bot.py"]
