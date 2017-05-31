import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '356714440:AAG_cvz5DiSgwJlpCMmmOcdtu0QtvZ17lVs'
WEBHOOK_URL = 'https://b2dc6755.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

machine = TocMachine(
    states=[
	    'startstate',
		'user',		
        
		'state1',
		'state11',
		'state12',
		'state13',
		
        'state2',
		'state21',
		'state22',
		'state23',
		
		'state3',
		'state31',
		'state32',
		'state33'
    ],
    transitions=[
	    {#start	
            'trigger': 'advance',
            'source': 'startstate',   
            'dest': 'user',
            'conditions': 'is_start_talking'
         },
		{#leave	
            'trigger': 'advance',
            'source': 'user',   
            'dest': 'startstate',
			'conditions': 'is_back'
        },		
        {#state1
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
		{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
		{
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
		{
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },#state2
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
		{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
		{
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
		{
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
		#state3
		{ 
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
		{
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
		{
            'trigger': 'advance',
            'source': 'state31',
            'dest': 'state32',
            'conditions': 'is_going_to_state32'
        },
		{
            'trigger': 'advance',
            'source': 'state32',
            'dest': 'state33',
            'conditions': 'is_going_to_state33'
        },
		#back
        {
            'trigger': 'go_back',
            'source': [
                'state13',
                'state23',
				'state33'
            ],
            'dest': 'user'
        }
    ],
    initial='startstate',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
