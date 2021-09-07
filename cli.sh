function test() {
    docker-compose -f test-db.yml down
    docker-compose -f test-db.yml up -d
    pytest $@
    docker-compose -f test-db.yml down
}

function shell () {
    python -m pipenv shell
}

function start() {
    docker-compose --env-file .env up -d $@
}

function restart() {
    docker-compose down
    start
}