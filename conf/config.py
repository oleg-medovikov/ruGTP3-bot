from starlette.config import Config

config = Config('/Users/oleg/git/ruGTP3-bot/.conf')

GPT3_SMALL = config('GPT3_SMALL', cast=str)
BOT_API    = config('BOT_API',    cast=str) 
