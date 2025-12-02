import os
import requests
from tqdm import tqdm
from dotenv import load_dotenv

class BaseAnswer:
    
    _URL = "https://adventofcode.com/2025/day/{}/input"

    @classmethod
    def answer(data: list[str]):
        raise NotImplementedError

    @classmethod
    def run(cls, day: int):
        data = cls._load_txt(day)
        res = cls.answer(data)
        print(f"Result: {res}\n")
        return res

    @classmethod
    def _load_txt(cls, day: int) -> list[str]:

        load_dotenv()
        session_cookie = os.getenv("SESSION_COOKIE")
        
        try:
            session = requests.Session()
            session.cookies.set("session", session_cookie)
            response = session.get(cls._URL.format(day))
            data = response.text.strip().split("\n")
            return tqdm(data)
        
        except Exception as e:
            print(f"Error fetching the URL: {e}")
