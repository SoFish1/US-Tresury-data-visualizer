import { useEffect } from 'react'
import { useState } from 'react'

const Confirmed_account = () => {
    const [confirmed_account, setConfirmed_account] = useState("");
    const token = window.location.href.replace("http://localhost:3000/confirmed_account/","")

    useEffect(() => {
        console.log(token)
        


        const opts = {
            method: "POST",
            headers: {
                "Content-Type":"application/json"                
            },
            body: JSON.stringify(
                {
                    "token":token, 
                    
                }

            )
        }

        fetch("/backend/auth/validate-email-token",opts)
        .then(resp => {
            if(resp.status === 200) 
            {
                setConfirmed_account("confirmed")
                return resp.json();
                
            }
            else alert("Error to process!!")
            
        })
        .then()
        .catch((error) => {
            setConfirmed_account("Not confirmed")
            console.log(error)
        })    


      });

    return (
        <div className="container">
          <div className="row">
            <div className="col-md-12">

              <div className="custom-alert">
                  
                    {confirmed_account === "confirmed" && (
                      <div class="alert alert-success" role="alert">
                        <p>Email Verification Done</p>
                      </div>
                    )}
                    
                    {confirmed_account === "Not confirmed" && (
                      <div class="alert alert-danger" role="alert">
                        <p>Email Verification Failed. Email may be already verified or the link is broken.</p>
                      </div>
                    )}

              </div>

            </div>
          </div>
        </div>
    )
}

export default Confirmed_account

