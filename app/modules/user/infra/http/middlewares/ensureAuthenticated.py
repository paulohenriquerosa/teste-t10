from fastapi import Request


async def ensureAuthenticate(request: Request, next):
  print(request.__dict__)
  await next()