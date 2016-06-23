# maya

## Usage (with docker)

Preparations:  
Make sure you have a prod.cfg file inside the config folder with the appropiate configs.

1. Build the docker image (may take a while):
   
    ```$ docker build -t maya .```
 
2. Run the official mysql image:

    ```$ docker run --name database -e MYSQL_ROOT_PASSWORD=my-pwd -e MYSQL_DATABSE=maya -d mysql:5.7```
    
3. Run the maya image connected to the mysql image:

    ```$ docker run --name maya_app --link database:mysql -d maya -p 80:80```
   
4. If you need to log into a running image you need to run:

    ```$ docker exec -i -t maya_app /bin/bash```