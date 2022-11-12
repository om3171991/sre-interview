import boto3
import sys
import mysql.connector

def conn_db():
    try:
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="BAoMDUdhcmFudGlh",
            database="sqs"
        )
        return mydb

    except Exception as err:
        print(Exception, err)
        print("Can't connect to DB")
        sys.exit()


def consume_message(db,db_cursor,q_name,maxNumberOfMessages):
    insert_sql = "INSERT INTO sqs_messages (sqs_message_id, sqs_message) VALUES (%s, %s)"
    sqs = boto3.resource('sqs',region_name="ap-southeast-1",endpoint_url="http://localstack:4566")
    queue = sqs.get_queue_by_name(QueueName=q_name)
    messages = queue.receive_messages(MaxNumberOfMessages=int(maxNumberOfMessages), WaitTimeSeconds=1)
    print("lenght => " + str(len(messages))) 
    for message in messages:
        if check_msg_id(db_cursor,message.message_id):
            print(message.message_id + "is already present in DB, hence removing from Queue")
        else:
            print(message.message_id + "-->" + message.body)
            val = (message.message_id,message.body)
            db_cursor.execute(insert_sql, val)
            db.commit()
        message.delete()

def check_msg_id(db_cursor,msg_id):
    check_sql = "select * from sqs_messages where sqs_message_id = " + msg_id
    db_cursor.execute(check_sql)
    results = db_cursor.fetchall()
    if(len(results) > 0):
        return True
    else:
        return False

def show_messages(db_cursor):
    show_sql = "select * from sqs_messages"
    try:
        db_cursor.execute(show_sql)
        results = db_cursor.fetchall()
        if(len(results) > 0):
            for row in results:
                print(row)                
        else:
            print("No messages are consumed yet")
    except Exception as err:
        print(Exception, err)
        print("Error in displaying messages")

def clear_messages(db_cursor):
    clear_message = "truncate table sqs_messages"
    try:
        db_cursor.execute(clear_message)
        print("All messages have been cleared from DB")
        return True
    except:
        print("Error in deleting messages")
        return False


if len(sys.argv) == 1:
    print("Action is required")
else:    
    db_conn = conn_db()
    db_cursor = db_conn.cursor()
    action = sys.argv[1]
    if action == "consume":
        if len(sys.argv) == 4 and sys.argv[2] == "--count":
            maxNumberOfMessages = sys.argv[3]
        else:    
            print("Selected action is consume & its requires queue_name & maxNumberOfMessages")
        consume_message(db_conn,db_cursor,"test-queue",maxNumberOfMessages)

    elif action == "clear":
        clear_messages(db_cursor)
    
    elif action == "show":
        show_messages(db_cursor)
    else:
        print("Invalid choice") 
