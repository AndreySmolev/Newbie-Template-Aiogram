from src import crud


async def create_user(*,
                      user_id: int):
    user = await crud.get_user(user_id)
    if not user:
        await crud.create_user(user_id)
        return True
    return False
