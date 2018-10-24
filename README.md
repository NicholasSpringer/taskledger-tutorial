# Taskledger

## Running the website
* `docker-compose -f sawtooth-default.yaml up`
This command brings up the docker containers and prepares the transaction
processor for use. The docker containers being referred to are 
    + `todo-tp` The transaction processor
    + `sawtooth-shell-default`
    + `sawtooth-settings-tp-default`   
    + `sawtooth-rest-api-default`
    + `sawtooth-validator-default`
    + More can be found about the conatiners on this here: https://sawtooth.hyperledger.org/docs/core/releases/1.0.5/app_developers_guide/docker.html#connecting-to-the-rest-api

* `./startup` specifies the interpret and other host machine stuff. Runs main()
* `sudo python3 webapp.py` Runs the web application if you'd like to view or 
  change the state of the blockchain. Available on port 80 of the host machine.

The REST API is exposed to port 8008 and makes it easy to see the state of the
application, view the blocks, or the batches.
Ex.
<YOUR-IP>:8008/state
