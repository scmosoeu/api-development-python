from fastapi import FastAPI

app = FastAPI()


@app.get('/{commodity}')
def get_commodity(commodity: str) -> dict:
    """
    Get information of the specified commodity 
    for the day

    Args:
    commodity (str): The commodity name to display
        latest sales for

    Returns:
    dict
    """

    return {'commodity': commodity}