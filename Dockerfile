# 1. Start with an official lightweight Python base image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all your project files into the container
COPY . .

# 4. Install the application's dependencies
RUN python -m pip install -r requirements.txt

# 5. Define the command that will run when the container starts
#    This now correctly points to your client.py file.
CMD ["python", "-m", "app.client"]