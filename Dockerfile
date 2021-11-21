FROM python:3
COPY requirements.txt /tmp/requirements.txt
# set a directory for the app
WORKDIR C:\Users\omer\bot_mesibot

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./mesibot.py"]