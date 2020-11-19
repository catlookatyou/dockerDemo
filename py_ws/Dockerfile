FROM  python:3
COPY  . /
RUN  pip install --trusted-host pypi.python.org -r requirements.txt
CMD  [ "python", "./websocket.py" ]
