def send_messages(messages):
    while messages:
        current_msg = messages.pop(0)
        print(current_msg)
        sent_msgs.append(current_msg)


msg_list = [
    "Hello",
    "How are you?",
    "Lovely weather we're having.",
    "Did you get the stuff? *looks around nervously*",
]

sent_msgs = []

send_messages(msg_list[:])

print(msg_list)
print(sent_msgs)
