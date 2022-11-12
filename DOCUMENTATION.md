Tool introduction/explanation
- This a easy tool to produce & consume messages and persist consumed messge to database.
- MYSQL 5.7 DB is configured. Default db name - sqs & table is sqs_messages
How to build the tool and build requirements
- cd solution && docker-compose up --build

How to configure the environment (if necessary)
- NA

How to run the tool
- All 3 containers are up & running (check_python_container_1, check_localstack_1, check_db_1)
- To produce new message 
    + docker exec -it aws_sqs_app python3 /opt/generator.py
- To consume existing messages
    + docker exec -it aws_sqs_app python3 /opt/msg_consumer_app.py consume --count 40
- To fetch all messages from DB
    + docker exec -it aws_sqs_app python3 /opt/msg_consumer_app.py show
- To clean all messages from DB
    + docker exec -it aws_sqs_app python3 /opt/msg_consumer_app.py clear
    
Challenges while solving the problem
- I have elementry knowledge of AWS cloud (Mostly worked on GCP/Azure),thereforeunderstanding of Boto3 and SQS is very limited. So it was kind of challenges to implement solution while learning.
- localStack - Its a really nice tool to play around with AWS APIs and intially it took some time for me to understand what is it and how to use it. While trying It was asking AWS credentails and hence need to read article to solve that issue by adding summy AWS credentails.