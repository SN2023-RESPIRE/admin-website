# admin-website

## Setup

1. Clone this repo
2. Create a Pytohn venv (optional)
3. Install the packages from `requirements.txt`
4. Create a .env file
5. Create a `SECRET_KEY` entry in the .env file with a valid secret key for the website
6. Run

Extra notes:
- The secret key can be generated using any method. The method used during development was the following:
```python
import os
print(os.urandom(16).hex())  # Copy the output
```
