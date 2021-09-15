import React from 'react'
import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { validEmail, validPassword } from './Regex.js';

const Register = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirm_password, setConfirm_password] = useState('');
    const history = useHistory();
    const [emailErr, setEmailErr] = useState(false);
    const [pwdError, setPwdError] = useState(false);
    const [email_sent, setEmail_sent] = useState(false);


    const set_validated_email = (e) => {
        
        setEmail(e.target.value)
        
        if (!validEmail.test(email)) {
            setEmailErr(true);
         }else{
            setEmailErr(false);
         }
        
        return setEmail(e.target.value)
     };

    const set_validated_password = (e) => {
        
        setPassword(e.target.value)
        if (!validPassword.test(password)) {
            setPwdError(true);
         }else{
            setPwdError(false);
         }
        return setPassword(e.target.value)
     }; 


    const handleClick = () => {
        
        const opts = {
            method: "POST",
            headers: {
                "Content-Type":"application/json"                
            },
            body: JSON.stringify(
                {
                    "email":email, 
                    "password": password
                }
            )
        }
        if(password === confirm_password){
        fetch("/backend/auth/register",opts)
        .then(resp => {
            if(resp.status === 200) 
            {
                setEmail_sent(true)
                return resp.json();
                
            }
            else alert("Error to process!!")
            
        })
        .then((token) => {            
            //alert("Check your email to confirm your account")
            props.setValidate_email_token(token)
            history.push("/login");
            console.log(email_sent)
            
            
        })
        .catch(error => {
            console.log(error)
        })



         
    }}







    return (
 <>
<form className="container-sm ">
                
                {( emailErr === true  ) ? (
                    
                    <div className="md-3">
                        <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                        <input type="email" className="form-control is-invalid" id="validationemail" aria-describedby="validationemailfeedback" required value={email} onChange={(e) => set_validated_email(e)}></input>
                        <div id="validationemailfeedback" className="invalid-feedback">
                        The email format is not valid
                        </div>
                    </div>

                 ) : (
                    <div className="mb-3">
                        <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                        <input type="email" className="form-control" id="exampleInputEmail1" required  value={email} onChange={(e)=> set_validated_email(e)}></input>
                    </div>
                 )}


                {( pwdError === true  ) ? (  
                    <div className="md-3">
                        <label htmlFor="exampleInputEmail1" className="form-label">Password</label>
                        <input type="email" className="form-control is-invalid" id="validationpassword" aria-describedby="validationpasswordfeedback" required value={password} onChange={(e)=> set_validated_password(e)}></input>
                        <div id="validationpasswordfeedback" className="invalid-feedback">
                        The password must be long at least 6 characters. It must contain at least a number and a special caracter
                        </div>
                        </div>
                    ) : (
                    <div className="mb-3">
                        <label htmlFor="exampleInputPassword1" className="form-label" >Password</label>
                        <input type="password" className="form-control" id="exampleInputPassword1" required value={password} onChange={(e)=> set_validated_password(e)}></input>
                    </div>
                        )}


                {( password === confirm_password  ) ? (
                <>
                <div className="mb-3">
                    <label htmlFor="exampleInputPassword2" className="form-label" >Confrim Password</label>
                    <input type="password" className="form-control" id="validationpassword" required value={confirm_password} onChange={(e)=> setConfirm_password(e.target.value)}></input>
                </div>
                
                </>
                ) : (
                    <>

                
                <div className="md-3">
                    <label htmlFor="validationServer05" className="form-label">Confrim Password</label>
                    <input type="password" className="form-control is-invalid" id="validationServer05" aria-describedby="validationServer05Feedback" required value={confirm_password} onChange={(e)=> setConfirm_password(e.target.value)}></input>
                    <div id="validationServer05Feedback" className="invalid-feedback">
                    Passwords must match.
                    </div>
                </div>
                
                </>
                )

                

                }
                {
                    ( password !== confirm_password ||  emailErr === true ||  pwdError === true) ? ( 
                        <button type="submit" className="btn btn-primary" disabled > Register </button>
                    ) : (
                        <button type="submit" className="btn btn-primary" onClick={handleClick}> Register </button>
                    )
                }

                { email_sent && (
                    <>
                    
                    <div className="mb-3 mt-4"   >
                      <div class="alert alert-success" role="alert">
                      <p>Check your email account to register</p>
                    </div>
                    </div>
                    </>
                )}
                
                

                


                
                


</form>

 
 </>

    
    )
}

export default Register
