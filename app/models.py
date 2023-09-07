# models.py

#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column,String,Integer,create_engine,DateTime,UniqueConstraint,CheckConstraint,PrimaryKeyConstraint,desc
from sqlalchemy.orm import declarative_base,sessionmaker

Base =declarative_base()


class Student(Base):
    __tablename__="students"

    __table_args__=(
        UniqueConstraint('email',name='unique_email'),
        CheckConstraint("grade BETWEEN 1 AND 12", name="grade_between_1_and_12")
        
    )
    id=Column(Integer(),primary_key=True)
    name=Column(String())
    email=Column(String(50))
    grade=(Column(Integer()))
 
    enrolledDate=Column(DateTime(),default=datetime.now())
    age=Column(Integer())

    def __repr__(self):
        return f"name: {self.name}"\
        f"age:{self.age}"\
        




if __name__ =="__main__":
    try:
        engine=create_engine("sqlite:///migrations_test.db")
        Base.metadata.create_all(engine)

        Session=sessionmaker(bind=engine)
        session=Session()

        kimemia=Student(name="kimemia",age=22,email="kimemia@23gmail",grade=12)
        david=Student(name="david",age=15,email="david@23gmail",grade=23)
        
        session.add_all([kimemia,david])
        session.commit()


    except Exception as e:
        print("error is " ,str(e))    

  