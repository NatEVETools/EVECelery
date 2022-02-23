import os
import time
import warnings
from core.celery import app
from core.tasks.BaseTasks.BaseTask import BaseTask
import requests
import string
import random
from redis.exceptions import LockError
from .ProcessMailEnqueueESICalls import ProcessMailEnqueueESICalls


def get_zk_redisq_url() -> str:
    """returns the current zk redisq url"""
    try:
        queue_id = os.environ["ZKQueueID"]
    except KeyError:
        queue_id = "".join(random.choice(string.ascii_lowercase) for x in range(15))
        w = f"ZKQueueID env variable is not set. Using a temporary random queue id {queue_id}"
        warnings.warn(w)
    return f"https://redisq.zkillboard.com/listen.php?queueID={queue_id}"


@app.task(base=BaseTask)
def GetMailRedisQ() -> None:
    """
    get mail using RedisQ
    :rtype: None
    """
    redis = GetMailRedisQ.redis
    try:
        with redis.lock("Lock-GetMailRedisQ", blocking_timeout=0.5, timeout=600):
            resp = requests.get(get_zk_redisq_url(), timeout=45, verify=True)
            if resp.status_code == 200:
                data = resp.json()
                try:
                    if data.get("package") is not None:
                        id = data["package"]["killID"]  # test for id otherwise raise key error
                        ProcessMailEnqueueESICalls.apply_async(kwargs={"mail_json": data}, ignore_result=True)
                    else:
                        return
                except KeyError:
                    return
            elif resp.status_code == 429:  # error limited
                warnings.warn("GetMailRedisQ error limited. Are multiple processes from the same IP calling RedisQ?")
                time.sleep(600)
            elif 400 <= resp.status_code < 500:
                time.sleep(300)
            else:
                time.sleep(120)
    except LockError:
        return
