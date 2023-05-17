import time

def pred_loop():
    while True:
        # you can implement a predict function and return the predicted value instead of 1
        pred = 1
        yield f'{pred}'
        time.sleep(0.5)