from config import Config

import hmac
import hashlib

import subprocess
import logging
import os


def verify_hash(data, signature):
    deploy_key = Config.get_deploy_key().encode(encoding='UTF-8')
    mac = hmac.new(deploy_key, msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest('sha1=' + mac.hexdigest(), signature)

def auto_build():
    try:
        subprocess.call(['git', 'pull', 'origin', 'master'], shell=True)
        subprocess.call(['/usr/bin/touch /tmp/deploy'], shell=True)
        logging.info('Build OK')
    except Exception as error:
        logging.error(str(error))

if __name__ == '__main__':
    auto_build()