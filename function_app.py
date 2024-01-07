import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.schedule(schedule="0 00 22 * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger3(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
    params = {
        "trigger" : "true"
    }
    response = requests.get('https://bloodserviceschedule.azurewebsites.net/',params=params)
    logging.info(f'Response: {response.text}')
    logging.info('Python timer trigger function executed.')