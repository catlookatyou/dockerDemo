import asyncio
import websockets
import json

print('helloworld')

async def hello():
    async with websockets.connect('ws://35.236.138.54:3001/ws/python') as websocket:
        json_response = await websocket.recv()
        iotdata = json.loads(json_response)
        print(iotdata)
        #if iotdata['command'] == 'open':
        #    print(f"got command from {iotdata['line_user_id']} : turn the light on! AND replyToken-> {iotdata['replyToken']}")
        #elif iotdata['command'] == 'close':
        #    print(f"got command from {iotdata['line_user_id']} : turn the light off! AND replyToken-> {iotdata['replyToken']}")
        #elif iotdata['command'] == 'Hello2':
        #    print('hello world')
        # print(f"< {greeting}")
        # if greeting == "show":
        #     print(f"get recv {greeting}")

while True:
    asyncio.get_event_loop().run_until_complete(hello())