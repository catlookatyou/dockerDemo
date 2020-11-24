## 安裝docker

docker desktop

wsl (ubuntu)

**切換成wsl2，讓docker可以運行**

https://marcus116.blogspot.com/2019/01/docker-docker-for-windows.html

https://stackoverflow.com/questions/49679818/docker-could-not-read-ca-certificate

https://docs.docker.com/docker-for-windows/wsl/

## docker run 執行python檔 (py_ws)

1. 建立py、requirements.txt

2. 建立Dockerfile
  
### shell

1. 建立image:  docker build -t i_name .

2. 查看image:  docker images

3. 執行image:  docker run i_name (-it or -itd)

4. 查看container:  docker ps -a

 ***
 
停止container: docker stop c_id

刪除container: docker rm c_id

停止/刪除所有container

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

刪除image: docker rmi i_id

**若要刪掉image，要先刪除container**

進入container: docker exec -it c_id /bin/bash
  
## docker-compose (py_web)

### 建立web service

1. app.py(flask、redis)、requirements.txt

2. Dockerfile、build製作image(web)

3. 撰寫docker-compose.yml

**services中可啟動images(製作好的web、另外抓的redis):**

**ports、volumes (本機):(容器) => 本機檔案可掛載至容器內，本地修改檔案時會連動至container**

**開啟服務(啟動yml中的container): docker-compose up -d**

4. 關閉服務: docker-compose stop (停止)/ down (刪除container) 

5. 查看紀錄: docker-compose logs -f

**若只有單一檔案則可製作成image，再變成服務，但若是很多檔案，則image用底層的環境就好，不然每次更動都須重新build一次image**

進入container: docker-compose exec svc_name bash

## build laravel env (lara)

### dockerfile

安裝composer、node、phpzip等套件，build一個laravel環境image

### docker-compose

- 服務:app(自製的環境)、db、redis、nginx:

1. app中掛載根目錄所有檔案，可建立laravel專案; working_dir改為/var/www

2. db中的enviroment可設定資料庫預設密碼、建立資料庫等等

3. nginx中掛載根目錄所有檔案，以及本機./nginx/conf.d，內有先寫好的conf檔，用來指定laravel的預設路徑: root /var/www/project/public

- docker-compose up -d

1. 進入app，compose開專案，設定.env(host連至服務名db、redis)

2. 測試migrate、redis-cli -h redis -p 6379

3. 可進入其他容器查看

  
  




