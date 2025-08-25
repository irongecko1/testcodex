import asyncio
from typing import Optional
import httpx
from nicegui import events, ui

api = httpx.AsyncClient()

async def search(e: events.ValueChangeEventArguments) -> None:
    '''Search for cocktails as you type.'''
    response = await api.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={e.value}')
    results.clear()
    with results:  # enter the context of the the results row
        for drink in response.json()['drinks'] or []:  # iterate over the response data of the api
            with ui.image(drink['strDrinkThumb']).classes('w-64'):
                ui.label(drink['strDrink']).classes('absolute-bottom text-subtitle2 text-center')

search_field = ui.input(on_change=search).props('outlined rounded').classes('w-96')
results = ui.row()

ui.run()