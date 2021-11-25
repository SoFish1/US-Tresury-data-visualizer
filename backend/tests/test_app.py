
from datetime import datetime
import pytest

def test_root(client):
    res=client.get("/backend/auth/")
    assert res.json.get("message") == "Hello World"
    assert res.status_code == 200



@pytest.mark.parametrize('email, password, expected_status_code', [
    ("email_test_1@gmail.com", "password_1", 200),
    ("email_test_2@gmail.com", "password_2", 200)
    ])
def test_submit_user_register_form(client,email,password,expected_status_code):
    res=client.post("/backend/auth/register",json={"email":email,"password":password }, follow_redirects=True)
    assert res.status_code == expected_status_code
    
    res=client.post("/backend/auth/register",json={"email":email,"password":password }, follow_redirects=True)
    assert res.status_code == expected_status_code
    assert res.json.get("message") == "This email is already used"




def test_confirm_account(client,usertable,email= "email_test_1@gmail.com",password = "password_1"):

    res=client.post("/backend/auth/register",json={"email":email,"password":password }, follow_redirects=True)
    token=res.json
    res=client.post("/backend/auth/validate-email-token", headers={"Content-Type":"application/json"} ,json={"token":token }, follow_redirects=True)
    assert res.status_code == 200 
    assert res.json.get("message") == "Account successfully confirmed!" 
    confirmed_account=usertable.query.get(1) 
    assert confirmed_account.email == email
    assert confirmed_account.email_confirmed_at.isoformat(timespec='minutes')  == datetime.now().isoformat(timespec='minutes')




def test_login(client,email= "email_test_1@gmail.com",password = "password_1"):

    #Registration
    res=client.post("/backend/auth/register",json={"email":email,"password":password }, follow_redirects=True)
    token=res.json

    #try to Login with a not confirmed account  
    res=client.post("/backend/auth/token", headers={"Content-Type":"application/json"} ,json={"email":email,"password":password  }, follow_redirects=True)
    assert res.status_code == 401
    assert res.json.get("message") == "The account is not activated"

    #Confirm the account
    res=client.post("/backend/auth/validate-email-token", headers={"Content-Type":"application/json"} ,json={"token":token }, follow_redirects=True)

    #Login successfully
    res=client.post("/backend/auth/token", headers={"Content-Type":"application/json"} ,json={"email":email,"password":password }, follow_redirects=True)
    assert res.status_code == 200

    #Login with bad password
    res=client.post("/backend/auth/token", headers={"Content-Type":"application/json"} ,json={"email":email,"password":password + "wrong_password" }, follow_redirects=True)
    assert res.status_code == 401
    assert res.json.get("message") == "Bad username or password"

    #Login with bad email    
    res=client.post("/backend/auth/token", headers={"Content-Type":"application/json"} ,json={"email":"wrong_email@gmail.com","password":password  }, follow_redirects=True)
    assert res.status_code == 401
    assert res.json.get("message") == "Bad username or password"


def test_load_show_data_page(client,email= "email_test_1@gmail.com",password = "password_1"):

    res=client.post("/backend/auth/register",json={"email":email,"password":password }, follow_redirects=True)
    token=res.json
    res=client.post("/backend/auth/validate-email-token", headers={"Content-Type":"application/json"} ,json={"token":token }, follow_redirects=True)
    res=client.post("/backend/auth/token", headers={"Content-Type":"application/json"} ,json={"email":email,"password":password }, follow_redirects=True)
    access_token=res.json.get("access_token")
    res=client.get("/backend/main/show_data", headers={"Authorization": f"Bearer {access_token}", "Content-Type":"application/json" } ,json={"email":email,"password":password }, follow_redirects=True)
    
    assert res.status_code == 200
    assert res.json
    
