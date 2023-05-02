FROM python:3

# set a directory for the app
WORKDIR /usr/FP_CS333/app

COPY . .

# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# copy all the files to the container
COPY . .

# run the command
CMD ["python3", "./finalGame.py"]
