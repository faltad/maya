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

"""
In order to be able to deploy the new changes, apache needs to be restarted, after pulling the changes from git.
For that to happen, there's a cronjob running every x minutes checking for the existence of a file in /tmp/deploy.
If such a file exists, then apache is restarted and this file is deleted so that the next time the deploy runs, the process can execute correctly.
"""
def auto_build():
    try:
        subprocess.call(['git', 'pull', 'origin', 'master'], shell=True)
        subprocess.call(['/usr/bin/touch /tmp/deploy'], shell=True)
        logging.info('Build OK')
    except Exception as error:
        logging.error(str(error))

if __name__ == '__main__':
    auto_build()