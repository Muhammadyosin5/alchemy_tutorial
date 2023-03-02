from loader import *
import models
from datetime import datetime



#max,min,count,sum,avg

def main(db: Session):
    #or_
    # result = db.query(models.Category).where(or_(models.Category.category_id == 1,models.Category.name == 'Abror'))

    #and_select(func.count()).select_from(my_table)
    # result = db.query(func.max(models.Category.category_id)).all()
    # print(result)
    # result = db.query(func.max(models.Category.category_id)).scalar()
    #scalar() faqat aggregate functionlar uchun
    #one() bitta row va bir nechta column uchun

    # for i in result:
    #     print(i)

    # for i in result:
    #     print(i)
    # for i in result:
        # print(i)
    #not_
    # result = db.query(models.Category).where(not_(models.Category.category_id == 1))


    # for i in result:
    #     print(i)

    # for i in result:
    #     print(i)

    # cat: Table = models.Category.__table__
    # for i in cat.columns:
    #     print(i,i.type)
    
    # query = cat.insert().values(category_id=3,name='Abror',last_update=datetime.now())
    # query = cat.select()
    # result = con.execute(query)
    # res = result.fetchone()
    # print(res)
    con.commit()

if __name__ == '__main__':
    # models.Base.metadata.drop_all(engine)
    # models.Base.metadata.create_all(engine)
    main(session)