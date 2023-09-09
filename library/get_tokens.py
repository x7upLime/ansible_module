#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: get_tokens

short_description: Extract a list of tokens from an edpoint

version_added: "1.0.0"

description: |
  Query an endpoint expecting json output.
  The json output in the body is split in space-separated tokens.
  The tokens are parsed and returned as a list of dictionaries.


options:
    endpoint:
        description:
            - URL of the endpoint we're trying to retrieve the tokens from.
        required: true
        type: str

author:
    - Andrei Tudor Corduneanu (@x7upLime)
'''

EXAMPLES = r'''
- name: Retrieve tokens
  get_tokens:
    endpoint: https://jsonplaceholder.typicode.com/posts/2
'''

RETURN = r'''
tokens:
    description: A list of parsed tokens, in the form of dictionaries.
    returned: always
    type: list of dicts
'''

from ansible.module_utils.basic import AnsibleModule
import requests


def run_module():
    # this is the definition of the available module args.
    module_args = dict(
        endpoint=dict(type='str', required=True)
    )

    # this is the state of our module.
    # here goes anything that need be added to the response
    result = dict(
        changed=False,
        tokens=[]
    )

    # this is our interface to ansible.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # we make the request to the endpoint even if we're in
    # check mode, since we're not modifying the state of
    # the host we're running on.
    # We may choose to behave differently in the future..
    if module.check_mode:
        pass

    # we make a request to the endpoint,
    # tokenizing the body of the json response.
    tokens, err = makeRequestToEndpoint(module.params['endpoint'])
    if err != "":
        module.fail_json(err, **result)
    result['tokens'] = tokens

    # we'll never consider the state of the environment changed
    result['changed'] = False

    # successful module execution.
    # we're returning the state to ansible
    module.exit_json(**result)


def makeRequestToEndpoint(endpt: str) -> tuple[list, str]:
    try:
        r = requests.get(endpt)
    except requests.exceptions.MissingSchema:
        return ([], 'Missing schema in endpoint. Try http://{}'.format(endpt))
    except (requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.HTTPError):
        return ([], 'Unable to connect to endpoing. Check the url')
    except requests.exceptions.JSONDecodeError:
        return ([], "Unable to decode JSON.")

    else:
        jresp = r.json()
        if jresp == {}:
            return ([], "Server returned an empty response")
        else:
            tokens = str(jresp['body']).split(sep=" ")
            return ([{"field1": token} for token in tokens], "")


def main():
    run_module()


if __name__ == '__main__':
    main()
