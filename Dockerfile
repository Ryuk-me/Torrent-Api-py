FROM python:3.8
ADD requirements.txt requirements.txt
ADD main.py main.py
RUN pip install -r requirements.txt
COPY . .
CMD ["python" ,"main.py"]