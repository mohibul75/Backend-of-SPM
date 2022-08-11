FROM python:3.8     
ENV DockerHOME=/home/app/webapp  

RUN mkdir -p $DockerHOME  
  
WORKDIR $DockerHOME  
  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
 
RUN pip3 install --upgrade pip  
 
COPY ./stocker $DockerHOME
RUN pip3 freeze > requirements.txt
RUN pip3 install djangorestframework       
RUN pip3 install -r requirements.txt
#RUN python3 manage.py migrate    
EXPOSE 8000  
CMD python3 manage.py runserver 0.0.0.0:8000  
