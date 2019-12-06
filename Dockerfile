FROM python:3
RUN git clone https://github.com/caranova/nrcodechallenge.git
WORKDIR /nrcodechallenge
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "nrchallenge.py" ]