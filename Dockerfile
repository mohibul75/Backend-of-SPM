FROM python:3.8     
ENV DockerHOME=/home/app/webapp  

RUN mkdir -p $DockerHOME  
  
WORKDIR $DockerHOME  
VOLUME CNN
  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
 
RUN pip3 install --upgrade pip  
 
COPY ./stocker $DockerHOME
#RUN pip3 freeze > requirements.txt
RUN pip3 install djangorestframework       
RUN pip3 install -r requirements.txt
RUN pip3 install requests
#RUN pip3 install --user django-cors-headers
#RUN python3 manage.py migrate    
EXPOSE 8001 
CMD python3 manage.py runserver 0.0.0.0:8001
