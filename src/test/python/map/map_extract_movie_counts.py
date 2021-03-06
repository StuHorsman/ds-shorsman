#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
    line = line.strip()
    json_data = json.loads(line)
    
    if 'Play' in json_data['type']:
        try:
            user = json_data['user']
            
            if len(json_data['payload']['itemId']) > 0:
                movie_id = json_data['payload']['itemId']
            
            # Concatentate the key and separate by ','
            key = str(user) + ',' + movie_id
            values = 1
            
            print '%s\t%s' % (key, values)
            
        except KeyError as e:
            pass

