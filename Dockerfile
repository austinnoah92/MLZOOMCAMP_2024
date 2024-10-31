FROM python:3.11.5-slim

# Install pipenv
RUN pip install pipenv

# Create the expected directory structure
RUN mkdir -p /workspaces/MLZOOMCAMP_2024

# Set the working directory to match the application's expected path
WORKDIR /workspaces/MLZOOMCAMP_2024

# Copy necessary files into the working directory
COPY ["Pipfile", "Pipfile.lock", "model1.bin", "dv.bin", "predict.py", "./"]

# Install dependencies
RUN pipenv install --system --deploy

# Expose port 5000
EXPOSE 5000

# Bind Gunicorn to 0.0.0.0 to allow external access
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "predict:app"]
