from nicegui import ui
import os
ui.button('Click me!',on_click=lambda : ui.notify(
    'See the same tab next!',
    position='center',
    type='info',
    color='red'
))
ui.run(host='0.0.0.0',port=int(os.environ.get('PORT',8080)))