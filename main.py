from configparser import ConfigParser
import time

from pypresence import Presence

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)

client_id = config['Client']['ClientID']

if config['States']['State'] != '<Required>':
    state = config['States']['State']
else:
    state = 'Left unchanged'

if config['States']['Details'] != '<Optional>':
    details = config['States']['Details']
else:
    details = None

if config['States']['ElapsedTime'] == 'True':
    start = time.time()
else:
    start = None

if config['Images']['LargeImage'] != '<Optional>':
    large_image = config['Images']['LargeImage']
else:
    large_image = None

if config['Images']['SmallImage'] != '<Optional>':
    small_image = config['Images']['SmallImage']
else:
    small_image = None

if config['Images']['LargeTooltip'] != '<Optional>':
    large_tooltip = config['Images']['LargeTooltip']
else:
    large_tooltip = None

if config['Images']['SmallTooltip'] != '<Optional>':
    small_tooltip = config['Images']['SmallTooltip']
else:
    small_tooltip = None

rpc = Presence(client_id)

print(f'Application ID: {client_id}')
print(f'State: {state}')
print(f'Details: {details if details else "None (Optional)"}')
print(f'Elapsed Time: {"On" if start else "Off"}')
print(f'Large Image: {large_image}{" with tooltip/text" if large_tooltip else ""}')
print(f'Small Image: {small_image}{" with tooltip/text" if small_tooltip else ""}\n')

print('Connecting presence...')

try:
    rpc.connect()
    rpc.update(state=state, details=details, start=start, large_image=large_image,
           small_image=small_image, large_text=large_tooltip, small_text=small_tooltip)
    print('Presence connected!\n')
except:
    print('Presence failed to connect...')
    print('Exiting program...')

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print('Disconnecting presence...')
    print('Exiting program...')
    time.sleep(3)
