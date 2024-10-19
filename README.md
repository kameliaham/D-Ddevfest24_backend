Add machines : 
<!-- python manage.py loaddata machines.json -->


subscribe webhook 
<!-- from machine.services  import *
subscribe_all_machines() -->

run project with daphne -b 127.0.0.1 -p 8000 backend.asgi:application

create redis-server on docker 
docker run -d --name redis-server -p 6379:6379 redis
docker start redis-server 


install ngrok 
ngrok http 8000
get HTTP  and replace it subscribe_all_machines()

