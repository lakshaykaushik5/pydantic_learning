from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    is_active:bool


data = {'id':1,'name':'name','is_active':True}

user = User(**data)
print(user)

if __name__ == "__main__":
    main()
