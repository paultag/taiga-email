#!/usr/bin/env python3

from taiga import TaigaAPI

import email.parser
import sys
import os

body = email.parser.Parser().parsestr(sys.stdin.read())
text = body.get_payload() if not body.is_multipart() else body.get_payload(i=0)

api = TaigaAPI(host=os.environ.get('TAIGA_HOST', 'http://z.ero.cool/'))
api.auth(
    username=os.environ.get('TAIGA_USER', 'email'),
    password=os.environ.get('TAIGA_PASS', None)
)
project = api.projects.get(os.environ.get('TAIGA_PROJECT', '2'))

project.add_user_story(
    body['Subject'],
    description="""\
From: {fro}
Message-Id: {messageid}

{text}
""".format(fro=body['From'],
           messageid=body['Message-Id'],
           text=text))
