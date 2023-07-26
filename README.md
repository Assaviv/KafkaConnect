# KafkaConnect
POC of kafka connect with mongodb

### How to use:
- Run to following command in the terminal
```
docker compose -p mongo-kafka up  --force-recreate
```
- Check the data from mongodb container
```
docker exec -it mongo1 /bin/bash
mongosh "mongodb://mongo1"
use Tutorial2
db.pets.find()
```
- See the connector status
```
docker exec -it py-service /bin/bash
status
```
### Configurations:
> Configure mongodb connector under simplesink.json
