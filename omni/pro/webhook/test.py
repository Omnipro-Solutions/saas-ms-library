from omni.pro.decorators import custom_decorator


@custom_decorator
def test_weebhook(ex=False):
    if ex:
        raise Exception("Webhook is not working")
    return {"status": "success", "message": "Webhook is working fine"}
