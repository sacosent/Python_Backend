from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    age: int
    email: str
    username: str
    password: str

users = [User(1,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(2,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(3,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(4,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(5,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(6,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta"),
         User(7,"Satiago Cosentino",28,"cosentinosantiago92@gmail.com","sacosent","queteimporta")]