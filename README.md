# fast_API_web_app

to ran the program first you need to run docker
on your machine in another terminal window directly
in this project with following command:
    docker-compose -f docker-compose.dev.yaml up
Then in another terminal window run this:
    export EE_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"
and then:
    python3 main.py

to start a local postgresql server you need type in
terminal: brew services start postgresql@14
and then check the status: brew services list
to stop the server:  brew services stop postgresql@14
To see on wich port postgresql is running type:
sudo lsof -i -P -n | grep LISTEN | grep postgres

connect to postgresql through CLI: psql -h 127.0.0.1 -p 5432 -d postgres