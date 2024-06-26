import binascii
import hashlib
from app.database import db
from fastapi import HTTPException, status
from app import schemas
from sqlalchemy.orm.session import Session
from typing import List
from app.models import Email_token, Usersignup
import os
import uuid
import datetime

get_db = db.get_db


def login(email, password, db):
    hash_password = hashlib.md5(password.encode())
    user = db.query(Usersignup).filter(Usersignup.email ==
                                       email, Usersignup.password == hash_password.hexdigest()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="email and password not found")
    return user.__dict__


def forgot_paswords_email_sent(user_id, email, db):
    # check user exist or not
    user = db.query(Usersignup).filter(
        Usersignup.id == user_id, Usersignup.email == email)
    userobj = user.first()
    if not userobj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="email and id not found")
    # create reset code and save to thr database
    reset_code = str(uuid.uuid1())
    current_time = datetime.datetime.utcnow()
    save_token = Email_token(
        email=email, reset_code=reset_code, status=True,  expired_in=current_time)
    db.add(save_token)
    db.commit()

    #sent email
    subject = "forgot password"
    recipient = [email]
    message = """
    <html>
        <body>
            <div>
                <h1>passsword reset token/{0:}</h1>
                
            </div>

        </body>
    </html>
    """.format(reset_code)
    return message


def change_password(id, oldpassword, newpassword, confirm_new_password, db):
    getuser = db.query(Usersignup).filter(Usersignup.id == id)
    user = getuser.first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    if user.password == oldpassword:
        if newpassword == confirm_new_password:
            getuser.update({"password": confirm_new_password})
            db.commit()
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="newpassword and confirm_new_password is not matched")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="oldpassword is not valid")
