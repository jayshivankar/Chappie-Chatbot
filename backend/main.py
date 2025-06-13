from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

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

    if intent == "track-order - context:ongoing-tracking":
        return track_order(parameters)

    return JSONResponse(content={
        "fulfillmentText": f"Intent '{intent}' not handled explicitly."
    })


def track_order(parameters: dict):
    order_id = parameters.get('order_id')
    return JSONResponse(content={
        "fulfillmentText": f"Tracking order with ID: {order_id}"
    })


