#!/usr/bin/env python
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Gitkit API.

Command-line application that allows insert, list, information inquiries
and deletion of Gitkit user accounts
"""

import argparse
import hashlib
import hmac
from pprint import pprint
import sys

from identitytoolkit import gitkitclient


parser = argparse.ArgumentParser(description='Manage Gitkit user accounts')

parser.add_argument('cmd',
  metavar='command',
  help='one of: get, list, insert, delete')

parser.add_argument('--id',
  nargs='?',
  help='id of the user')

parser.add_argument('--email',
  nargs='?',
  help='email of the user')

def CalcHmac(hash_key, password, salt):
  func = hmac.new(hash_key, password, hashlib.sha1)
  func.update(salt)
  return func.digest()


def main(argv):
  # Get instance of Gitkit Client
  gitkit_instance = gitkitclient.GitkitClient.FromConfigFile(
      'gitkit-server-config.json')

  # Parse command line arguments
  args = parser.parse_args()

  if args.cmd == 'insert':
    # insert account
    hash_key = 'hash-key'

    user1 = gitkitclient.GitkitUser.FromDictionary({
        'email': '1234@example.com',
        'localId': '1234',
        'salt': 'salt-1',
        'passwordHash': CalcHmac(hash_key, '1111', 'salt-1')
    })
    user2 = gitkitclient.GitkitUser.FromDictionary({
        'email': '5678@example.com',
        'localId': '5678',
        'salt': 'salt-2',
        'passwordHash': CalcHmac(hash_key, '5555', 'salt-2')
    })
    gitkit_instance.UploadUsers('HMAC_SHA1', hash_key, [user1, user2])
  elif args.cmd == 'list':
    # list accounts
    for account in gitkit_instance.GetAllUsers(2):
      pprint(vars(account))
  elif args.cmd == 'delete':
    # delete account
    if args.id != None:
      print 'Deleting user ' + args.id
      gitkit_instance.DeleteUser(args.id)
    elif args.email != None:
      print 'Deleting user '+ args.email
      account = gitkit_instance.GetUserByEmail(args.email)
      gitkit_instance.DeleteUser(account.user_id)
    else:
      print 'error: need email or id'
  elif args.cmd == 'get':
    # get user from id
    if args.id != None:
      pprint(vars(gitkit_instance.GetUserById(args.id)))
    elif args.email != None:
      pprint(vars(gitkit_instance.GetUserByEmail(args.email)))
    else:
      print 'error: need email or id'
  else:
    print 'error: unknown command'
    parser.print_help()

if __name__ == '__main__':
    main(sys.argv)
