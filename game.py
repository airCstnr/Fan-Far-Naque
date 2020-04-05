import json


def singleton(className):
    """ Holds singletons of className objects """
    instances = {}
    def get_instance():
        if className not in instances:
            instances[className] = className()
        return instances[className]
    return get_instance


@singleton
class Game():

    game_started = False
    current_state = 0

    def __init__(self):
        print("Init", __class__.__name__)
        with open('order.json') as f:
            data = json.load(f)
            self.order = data['order']

