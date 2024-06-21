FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN python -c "from transformers import AutoModelForSequenceClassification, AutoTokenizer; \
               tokenizer = AutoTokenizer.from_pretrained('distilbert/distilbert-base-uncased-finetuned-sst-2-english'); \
               model = AutoModelForSequenceClassification.from_pretrained('distilbert/distilbert-base-uncased-finetuned-sst-2-english')"

COPY ./main.py /code/main.py

EXPOSE 8000

CMD ["fastapi", "run", "/code/main.py", "--port", "8000"]