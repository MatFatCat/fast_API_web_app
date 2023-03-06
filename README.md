# fast_API_web_app

to ran the program first you need to run docker
on your machine in another terminal window directly
in this project with following command:
    docker-compose -f docker-compose.dev.yaml up
Then in another terminal window run this:
    export EE_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"
and then:
    python3 main.py