import React from 'react'
import { useState, useEffect } from 'react'
import {  useHistory } from 'react-router-dom';

const Login = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const token = localStorage.getItem("token");
    const history = useHistory();
    
    

    
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


        fetch("/backend/auth/token",opts)
        .then(resp => {
            if(resp.status === 200) 
            {
                return resp.json();
                
            }
            else alert("Error to process!!")
            
        })
        .then((data) => {            
            localStorage.setItem("token",data.access_token);
            history.push("/show_data");
            props.sign_in(true)
            
        })
        .catch(error => {
            console.log(error)
        })
 
    }





    

    return (
        <>

            {(token && token !==null && token !== undefined) ? (
                "You are already logged in   " + token
            ) : (
                <div class="container-sm">
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="exampleInputEmail1"  value={email} onChange={(e)=> setEmail(e.target.value)}></input>
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputPassword1" className="form-label" >Password</label>
                    <input type="password" className="form-control" id="exampleInputPassword1" value={password} onChange={(e)=> setPassword(e.target.value)}></input>
                </div>
                <button type="submit" className="btn btn-primary" onClick={handleClick}> Submit </button>

               
                    
                
               

                </div>
            )}

        </>
    )
}

export default Login
