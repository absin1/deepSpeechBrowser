

import asyncio
import datetime
import random
import websockets
import ssl
import webrtcvad
vad = webrtcvad.Vad()
vad.set_mode(1)
sample_rate = 16000
async def time(websocket, path):
    frame = await websocket.recv()
    await websocket.send('Contains speech: %s' % (vad.is_speech(frame, sample_rate)))
    #while True:
    #    now = datetime.datetime.utcnow().isoformat() + 'Z'
    #   await websocket.send(now)
    #    await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

def startWebsocket():
    print('Started websocket')
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if(__name__=='__main__'):
    startWebsocket()