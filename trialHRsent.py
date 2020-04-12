pat = {}


def add_keys():
    pat["heart_rate"] = []
    pat["status"] = []
    pat["timestamp"] = []
    return pat


def add_HR(pat2):
    pat["heart_rate"].append(100)
    pat["heart_rate"].append(200)
    pat["heart_rate"].append(200)
    return pat


pat2 = add_keys()
pat3 = add_HR(pat2)
print("the dictionary is {}".format(pat2))
print("the filled dictionary is {}".format(pat3))
