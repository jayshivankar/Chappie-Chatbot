from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()

inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract necessary information from the Dialogflow WebhookRequest
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    # session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'order-add - context:ongoing order': add_to_order,
        # 'order-remove - context:ongoing order': remove_from_order,
        # 'order-complete - context:ongoing-order': complete_order,
        'track-order - context:ongoing-tracking': track_order
    }
    return intent_handler_dict[intent](parameters)

def add_to_order(parameters: dict):
    food_items = parameters["food-item-names"]
    quantities = parameters["number"]

    if len(food_items) != len(quantities):
        fulfillment_text = "Sorry I didn't understand.Can you please specify the quantity."
    else:
        fulfillment_text = f"Recieved {food_items} and {quantities} "

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def track_order(parameters: dict):
    order_id = int(parameters['order_id'])
    order_status = db_helper.get_order_status(order_id)

    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


