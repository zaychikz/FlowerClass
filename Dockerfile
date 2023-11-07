FROM python:3.9
WORKDIR /flower
COPY ./requirements.txt /flower/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /flower/requirements.txt

COPY ./app /flower/app
COPY ./model /flower/model

ENV PYTHONPATH "${PYTHONPATH}:/flower"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]