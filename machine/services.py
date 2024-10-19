import requests


def subscribe_to_machine(machine_id, callback_url):
    """
    Subscribes to a machine's data stream via a webhook.
    
    :param machine_id: ID of the machine to subscribe to.
    :param callback_url: Your backend URL to receive data from the machine.
    :return: Response from the server.
    """
    
    url = "https://manufcaturing-challenge-production.up.railway.app/Webhook"
    data = {
        "machine": machine_id,
        "callback_url": callback_url
    }
    print ("data",data)

    response = requests.post(url, json=data)
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    print("Response JSON:", response.json() if response.status_code == 200 else "No JSON response")

    print("response",response)
    
    if response.status_code in [200, 201]: 
        return response.json()
    else:
        raise Exception(f"Subscription failed for {machine_id}: {response.status_code} {response.text}")


def subscribe_all_machines():
    """
    Subscribes to all required machines.
    """
    machines = ['welding_robot_006', 'stamping_press_001', 'painting_robot_002','leak_test_005','cnc_milling_004','agv_003']
    
    # Replace the hardcoded Ngrok URL with the one generated when you run `ngrok http 8000`.
    callback_url = 'https://c02a-154-121-29-131.ngrok-free.app/machine/webhook/' 
            
    
    for machine in machines:
        try:
            print("machine",machine)
            response = subscribe_to_machine(machine, callback_url)
            print(f"Successfully subscribed to {machine}: {response}")
        except Exception as e:
            print(f"Error subscribing to {machine}: {e}")
