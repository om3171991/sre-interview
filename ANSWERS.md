Q1: Please explain what is the advantage of using SQS in this solution.
A1: 
- Dont need to invest on setup, maintence & reliability of delivery of messages.
- Easy integration with other AWS services else need to maintain a library.
- Scalable in different peaks. 

Q2: Compare SQS to a message broker you have used before. What are the differences? [RabbitMQ/Kafka]
A2:
- RabbitMQ/Kafka is more appropiate where Organisation has product distributed across multiClouds like banking or multi teants apps.
- Kafka is alot faster then SQS/Pubsub.
- For very big payloads, SQS uses s3 bucket which will another cost expense.

Q3: If we run multiple instances of this tool, what prevents a message from processed twice?
A3: 
- message_id column in mysql db is a primary key and hence if we try to add same message_id again it will raise and concern.
- From code also, we are first checking if message_id is present or not and if not present then only insert.

Q4: In very rough terms, can you suggest an alternative solution aside from using SQS from your previous experience using different technologies?
